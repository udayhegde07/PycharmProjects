class Obj:
    a = 10
    b = 20

    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)


    def __str__(self):
        return "%s %s"%(self.a, self.b)

a = Obj()
print(a)
print([a])