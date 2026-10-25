class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_head(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.tail = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        new.prev = self.tail
        self.tail = new

    def insert_position(self, pos, data):
        if pos == 1:
            self.insert_head(data)
            return
        new = Node(data)
        temp = self.head
        for i in range(pos - 2):
            temp = temp.next
        new.next = temp.next
        new.prev = temp
        if temp.next != None:
            temp.next.prev = new
        else:
            self.tail = new
        temp.next = new

    def delete_head(self):
        if self.head == None:
            print("List is Empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if self.head == None:
            print("List is Empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
    def delete_position(self, pos):
        if self.head == None:
            print("List is Empty")
            return
        if pos == 1:
            self.delete_head()
            return
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        if temp == self.tail:
            self.delete_end()
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
    def display_forward(self):
        if self.head == None:
            print("List is Empty")
            return
        temp = self.head
        while temp != None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
    def display_backward(self):
        if self.tail == None:
            print("List is Empty")
            return
        temp = self.tail
        while temp != None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


dll = DoublyLinkedList()
dll.insert_head(20)
dll.insert_head(10)
dll.insert_end(40)
dll.insert_end(50)
dll.insert_position(3, 30)

print("Forward")
dll.display_forward()
print("Backward")
dll.display_backward()
dll.delete_head()
print("After Delete Head")
dll.display_forward()
dll.delete_end()
print("After Delete End")
dll.display_forward()
dll.delete_position(2)
print("After Delete Position")
dll.display_forward()