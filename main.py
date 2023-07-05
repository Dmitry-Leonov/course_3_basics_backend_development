from utils import load_operation

if __name__ == '__main__':
    filename = 'operations.json'
    card_transactions = load_operation(filename)
    print(card_transactions)

