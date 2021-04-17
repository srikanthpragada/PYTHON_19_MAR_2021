class Account:
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
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient Funds")

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Scott")  # Create an object
a1.deposit(10000)
a1.withdraw(5000)
print(a1.getbalance())

# print(a1._Account__balance)
print(a1.__dict__)
a1.show()
a2 = Account(2, "Jack", 10000)
a2.show()
