import json
import operator
import re
from datetime import datetime


def load_operation(filename: str) -> list:
    """
    Получение списка словарей из файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def check_valid_operation(operation):
    """
    Задает условие для фильтрации словаря:
    словарь не пустой, транзакция EXECUTED и это не открытие вклда
    """
    return operation.get('date') \
        and operation.get('state') == 'EXECUTED' \
        and operation.get('description') != 'Открытие вклада'


def get_executed_operations(operations: list) -> list:
    """
    Возвращает список словарей по заданным условиям
    """
    return [
        operation for operation in operations
        if check_valid_operation(operation)
    ]


def get_last_five_operations(operations: list) -> list:
    """
    Возвращает последние 5 транзакций отсортированных по дате
    """
    sorted_data_new = sorted(get_executed_operations(operations), key=operator.itemgetter('date'), reverse=True)
    return sorted_data_new[:5]


def get_operations_by_print(operations: list) -> list:
    """
    Функция преобразования для вывода операции
    """
    list_by_print = []
    for operation in operations:
        data_by_print = {}
        date = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
        data_by_print["date"] = date.strftime("%d.%m.%Y")
        data_by_print["from"] = operation_masked(operation["from"])
        data_by_print["to"] = operation_masked(operation["to"])
        data_by_print["description"] = operation["description"]
        data_by_print["sum"] = operation["operationAmount"]["amount"]
        data_by_print["currency_name"] = operation["operationAmount"]["currency"]["name"]
        list_by_print.append(data_by_print)
    return list_by_print


def operation_masked(data_from_to):
    """Функция возвращает замаскированную номер карты или счета"""
    card_number = data_from_to.split()
    if len(card_number[-1]) == 20:
        card_number_print = card_number[0] + " **" + card_number[-1][-4:]
    else:
        number = card_number.pop(-1)
        hidden_number = number[:6] + '******' + number[-4:]
        card_number_print = ' '.join(card_number) + ' ' + ' '.join(re.findall('(.{%s}|.+$)' % 4, hidden_number))
    return card_number_print
