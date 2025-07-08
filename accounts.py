import datetime
import pytz

class Accounts:

    @staticmethod
    def _current_time():
        utc = datetime.datetime.now()
        return pytz.utc.localize(utc)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions_list = [(Accounts._current_time(),balance)]
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transactions_list.append((Accounts._current_time(), amount))
    def withdrawal(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions_list.append((Accounts._current_time(), -amount))
        else:
            print("Amount should be greater than zero or no more than your Aukaat")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}.".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transactions_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:10} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    A1 = Accounts("Piyush", 0)
    A1.show_balance()
    A1.deposit(4000)
    A1.show_transactions()
    A1.withdrawal(500)
    A1.show_transactions()
    print("\n")
    A2 = Accounts("Saloni", 300)
    A2.show_balance()
    A2.deposit(1000)
    A2.show_transactions()
    A2.withdrawal(200)
    A2.show_transactions()
