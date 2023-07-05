import json
import operator
from typing import List, Any


def load_operation(filename: str) -> list:
    """
    Функция получения списка словарей из файла
    :param filename: имя файла
    :return: список словарей
    """
    with open(filename, 'r', encoding='utf-8') as f:
        operation: list = json.load(f)
    return operation


def sort_by_date(data) -> list:
    """
    Функция возвращает послдение 5 транзакций отсротированных по дате
    :param data: список транзакций (словари)
    :return: список последних 5 транзакци
    """
    data_new = [i for i in data if i.get('date') and i['state'] == 'EXECUTED']
    sorted_data_new = sorted(data_new, key=operator.itemgetter('date'), reverse=True)
    return sorted_data_new[:5]
