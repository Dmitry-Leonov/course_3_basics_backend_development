from src.settings import OPERATION_DATA
from utils import load_operation, get_last_five_operations, get_operations_by_print

if __name__ == '__main__':
    # получаем список словарей из файла
    card_transactions = load_operation(OPERATION_DATA)
    # фильтруем, сортируем и получем 5 элементов списка для работы
    sorted_card_transactions = get_last_five_operations(card_transactions)
    # создаем новый список для рекомендованного вывода на экран
    card_transactions_print = get_operations_by_print(sorted_card_transactions)
    for i in card_transactions_print:
        print(f'{i["date"]} {i["description"]}')
        print(f'{i["from"]} -> {i["to"]}')
        print(f'{i["sum"]} {i["currency_name"]}')
        print('')
