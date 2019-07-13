class Employee:
    raiseamt = 1.04
    empcount = 0
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+lname+"@email.com"
        Employee.empcount += 1
    def fullname(self):
        return f'{self.fname} {self.lname}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseamt)

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raiseamt = amt

    @classmethod
    def from_string(cls,emp_string):
        fname, lname, pay = emp_string.split(":")
        pay = int(pay)
        return cls(fname,lname,pay)

    @staticmethod
    def isweekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

b = Employee.from_string("Simon:Joseph:100000")
c = Employee.from_string("Michael:Doe:90000")

import datetime

day = datetime.date(2019,7,13)
print(Employee.isweekday(day))

print(b.email)

b.apply_raise()
print(b.raiseamt)
print(c.raiseamt)

Employee.set_raise_amt(1.05)

print(Employee.raiseamt)
print(b.raiseamt)
print(c.raiseamt)