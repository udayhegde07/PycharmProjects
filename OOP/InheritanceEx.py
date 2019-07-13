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

class Developer(Employee):
    raiseamt = 1.10

    def __init__(self,fname,lname,pay,prgming_lng):
        super().__init__(fname,lname,pay)
        self.prgming_lng = prgming_lng


class Manager(Employee):
    raiseamt = 1.20

    def __init__(self, fname, lname, pay, emp = None):
        super().__init__(fname, lname, pay)
        if emp is None:
            self.emp = []
        else:
            self.emp = emp

    def add_employee(self,emp):
        if emp not in self.emp:
            self.emp.append(emp)
        else:
            return

    def remove_employee(self,emp):
        if emp in self.emp:
            self.emp.remove(emp)
        else:
            return

    def print_employee(self):
        for i in range(len(self.emp)):
            print(self.emp[i].fullname())


e = Developer("Uday", "Hegde", 40000, "Python")
e2 = Developer("Will", "Smith", 50000,"C++")
m = Manager("Mark", "Antoni", 100000, [e2])
m.add_employee(e)
m.remove_employee(e2)
print(issubclass(Developer,Employee))
print(m.print_employee())