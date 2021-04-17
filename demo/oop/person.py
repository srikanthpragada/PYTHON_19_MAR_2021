class Person:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def __str__(self):
        return f"{self.name} - {self.mobile}"

    def __eq__(self, other):
        return self.name == other.name and self.mobile == other.mobile

    def __gt__(self, other):
        return self.name > other.name


p1 = Person("A", "1234567890")
p2 = Person("A", "1234567890")
p3 = Person("B", "1112222222")

print(p1)  # p1.__str__()
print(p1.__str__())
print(p1 == p2)  # p1.__eq__(p2)
print(p3 > p2)   # p1.__gt__(p2)

persons = [Person("A", "123"), Person("X", "34844"), Person("C", "3443")]
for p in sorted(persons):
    print(p)
