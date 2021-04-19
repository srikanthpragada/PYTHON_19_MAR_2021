class Student:
    courses = {'Python': 10000, 'Java': 12000, 'DS': 15000}

    @staticmethod
    def getcoursefee(course):
        if course in Student.courses:
            return Student.courses[course]
        else:
            return None

    def __init__(self, sno, name, course='Python', feepaid=0):
        self.sno = sno
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def getbalance(self):
        total = Student.getcoursefee(self.course)
        return total - self.feepaid

    def payment(self, amount):
        if amount > self.getbalance():
            raise ValueError("Excess fee being paid!")

        self.feepaid += amount

    @property
    def totalfee(self):
        return Student.getcoursefee(self.course)




s = Student(1, "Bill", course="DS", feepaid=5000)
s.payment(5000)
#s.payment(2000)
print(s.getbalance())
print(s.totalfee)  # Property
