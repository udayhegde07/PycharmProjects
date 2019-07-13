
class Iter:
    def __init__(self, val):
        self.val = val
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.val)-1:
            raise StopIteration
        self.index += 1
        return self.val[self.index]

a = Iter("Hello")
for char in a:
    print(char)