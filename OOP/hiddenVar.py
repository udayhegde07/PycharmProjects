class Hide:
    __secret = 10

    def add(self, val):
        return (self.__secret + val)

h = Hide()
print(h.add(2))
print(h._Hide__secret)