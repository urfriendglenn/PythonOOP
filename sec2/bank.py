class account():
    def __init__(self, transactions=0):
        self.transactions = [transactions]

account_1 = account()
account_2 = account()

def transaction(account,amount):
    account.transactions.append(amount)

def account_desc(account):
    num_transactions = len(account.transactions)
    total = sum(account.transactions)
    average = total / num_transactions

    print(f"Summary of Account:")
    print(f"Total: {total}")
    print(f"Number of Transactions: {num_transactions}")
    print(f"Average of Total: {average}")
    print("-------------")

transaction(account_1, 400)
transaction(account_1, -20)
transaction(account_1, -50)

transaction(account_2, 500)
transaction(account_2, -35)
transaction(account_2, -45.40)
transaction(account_2, -100)

account_desc(account_1)
account_desc(account_2)