from utils import load_operation, sort_by_date, operation_by_print

if __name__ == '__main__':
    filename = '../operations.json'
    # получаем список словарей из файла
    card_transactions = load_operation(filename)
    # фильтруем, сортируем и получем 5 элементов списка для работы
    sorted_card_transactions = sort_by_date(card_transactions)
    # создаем новый список для рекомендованного вывода на экран
    card_transactions_print = operation_by_print(sorted_card_transactions)
    for i in card_transactions_print:
        print(f'{i["date"]} {i["description"]}')
        print(f'{i["from"]} -> {i["to"]}')
        print(f'{i["sum"]} {i["currency_name"]}')
        print('')
