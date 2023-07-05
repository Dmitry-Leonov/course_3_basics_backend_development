from utils import load_operation, sort_by_date

if __name__ == '__main__':
    filename = 'operations.json'
    card_transactions = load_operation(filename)
    sorted_card_transactions = sort_by_date(card_transactions)
    for i in sorted_card_transactions:
        print(i)

