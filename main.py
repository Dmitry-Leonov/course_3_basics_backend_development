from utils import load_operation, sort_by_date, operation_by_print

if __name__ == '__main__':
    filename = 'operations.json'
    card_transactions = load_operation(filename)
    sorted_card_transactions = sort_by_date(card_transactions)
    for i in sorted_card_transactions:
        print(f'{i["date"]} {i["description"]}')
        print(f'{i["from"]} -> {i["to"]}')
        print(f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}')
        print('')

    sorted_card_transactions = operation_by_print(sorted_card_transactions)
    for i in sorted_card_transactions:
        print(f'{i["date"]} {i["description"]}')
        print(f'{i["from"]} -> {i["to"]}')
        print(f'{i["sum"]} {i["currency_name"]}')
        print('')
