class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class sll:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def sort(self):
        temp = self.head
        while temp != None:
            index = temp.next
            while index != None:
                if temp.data > index.data:  
                    temp.data, index.data = index.data, temp.data
                index = index.next
            temp = temp.next

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,id(temp.next),id(temp),id(temp.prev))
            temp = temp.next
obj = sll()
n = int(input())
for i in range(n):
    m = int(input())
    obj.create(m)

obj.sort()
obj.display()
