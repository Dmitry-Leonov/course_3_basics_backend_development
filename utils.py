import json
import operator
from datetime import datetime
from typing import List, Any


def load_operation(filename: str) -> list:
    """
    Функция получения списка словарей из файла
    """
    with open(filename, 'r', encoding='utf-8') as f:
        operation: list = json.load(f)
    return operation


def sort_by_date(data: list) -> list:
    """
    Функция возвращает последние 5 транзакций отсротированных по дате
    условие: словарь не пустой, транзакция EXECUTED и это не открытие вклда
    """
    data_new = [i for i in data if
                i.get('date') and i.get('state') == 'EXECUTED'
                and i.get('description') != 'Открытие вклада']
    sorted_data_new = sorted(data_new, key=operator.itemgetter('date'), reverse=True)
    return sorted_data_new[:5]


def operation_by_print(data_print: list) -> list:
    """
    Функция преобразования для вывода операции
    """
    list_by_print = []
    for i in data_print:
        data_by_print = {}
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
        data_by_print["date"] = date.strftime("%d.%m.%Y")
        data_by_print["from"] = operation_masked(i["from"])
        data_by_print["to"] = operation_masked(i["to"])
        data_by_print["description"] = i["description"]
        data_by_print["sum"] = i["operationAmount"]["amount"]
        data_by_print["currency_name"] = i["operationAmount"]["currency"]["name"]
        list_by_print.append(data_by_print)
    return list_by_print


def operation_masked(data_from_to, card_number=[], card_number_print=''):
    """Функция возвращает замаскированную номер карты или счета"""
    card_number = data_from_to.split()
    if len(card_number[-1]) == 20:
        card_number_print = card_number[0] + " **" + card_number[-1][-4:]
    else:
        card_number_print = card_number[0] + " " + card_number[1] + " " \
                            + card_number[-1][0:4] + " " + card_number[-1][4:6] \
                            + "** **** " + card_number[-1][-4:]
    return card_number_print


