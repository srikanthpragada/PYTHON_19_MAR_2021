class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"


class Employee(Person):
    def __init__(self, name, email, job):
        super().__init__(name, email)
        self.job = job

    def __str__(self):
        return super().__str__() + f" - {self.job}"


class Player(Person):
    def __init__(self, name, email, game):
        super().__init__(name, email)
        self.game = game


e = Employee("Ben", "ben@gmail.com", "Programmer")
print(e)
