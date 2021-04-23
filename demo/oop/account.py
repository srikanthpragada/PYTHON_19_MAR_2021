class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.message = f"Amount to withdraw is {amount}, but available balance is {balance}"

    def __str__(self):
        return self.message


class Account:
    # static or class attribute
    min_balance = 10000

    @staticmethod
    def getminbal():
        return Account.min_balance

    # Constructor
    def __init__(self, acno, customer, balance=0.0):
        # Object attributes
        self.acno = acno
        self.customer = customer
        self.__balance = balance

    # Method
    def show(self):
        print(self.acno, self.customer, self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - Account.min_balance >= amount:
            self.__balance -= amount
        else:
            raise InsufficientFundsError(self.__balance,amount)

    def getbalance(self):
        return self.__balance

    @property
    def availablebalance(self):
        return self.__balance - Account.min_balance


print(Account.getminbal())
a1 = Account(1, "Scott")  # Create an object
a1.deposit(100000)
a1.withdraw(200000)
print(a1.availablebalance)
print(a1.getbalance())

# print(a1._Account__balance)
print(a1.__dict__)
a1.show()
a2 = Account(2, "Jack", 10000)
a2.show()
