import json


def display_last_5_transactions(transactions):
    num_transactions = len(transactions)
    if num_transactions == 0:
        print("No transactions found.")
    else:
        print("Last 5 transactions:")
        for i in range(max(0, num_transactions - 5), num_transactions):
            transaction = transactions[i]
            print(f"{transaction['date']} {transaction['description']}")
            print(f"{transaction['from']} -> {transaction['to']}")
            print(f"{transaction['amount']} {transaction['currency']}")
            print()