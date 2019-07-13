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
        self.pay = self.pay * self.raiseamt

a = Employee("Robert", "Morris", 10000)
b = Employee("Steve", "Joseph", 90000)
print(a.fullname())
print(a.email)
print(Employee.fullname(b))
Employee.apply_raise(a)
print(a.pay)
print("\n")

print(b.__dict__)
print(Employee.__dict__)

print("\n")

print(Employee.empcount)

