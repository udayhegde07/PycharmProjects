class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __index__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def pushMiddle(self,data):
        new  = Node(data)

        new.prev = None
        new.next = self.head
        self.count += 1

        if self.count == 1:
            self.mid = new
        else:
            self.head.prev = new
            if self.count%2 != 0:
                self.mid = self.mid.prev
        self.head = new

    def popMiddle(self):


