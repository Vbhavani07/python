class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # REGISTER
    def register(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def emergency(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def remove(self, name):
        if self.head is None:
            print("Animal Not Found")
            return

        if self.head.data == name:
            self.head = self.head.next
            print("Removed:", name)
            return

        temp = self.head

        while temp.next:
            if temp.next.data == name:
                temp.next = temp.next.next
                print("Removed:", name)
                return
            temp = temp.next

        print("Animal Not Found")

    def count(self):
        c = 0
        temp = self.head

        while temp:
            c += 1
            temp = temp.next

        print("Total Animals:", c)


    def display(self):
        if self.head is None:
            print("No Animals Registered")
            return

        print("Animals:", end=" ")
        temp = self.head

        while temp:
            print(temp.data, end="")
            if temp.next:
                print(" ", end="")
            temp = temp.next

        print()


ll = LinkedList()

n = int(input())

for _ in range(n):
    arr = input().split()

    if arr[0] == "REGISTER":
        ll.register(arr[1])

    elif arr[0] == "EMERGENCY":
        ll.emergency(arr[1])

    elif arr[0] == "REMOVE":
        ll.remove(arr[1])

    elif arr[0] == "COUNT":         
        ll.count()

    elif arr[0] == "DISPLAY":
        ll.display()

#input
# #10
# REGISTER Deer
# REGISTER Rabbit
# EMERGENCY Tiger
# DISPLAY
# COUNT
# REMOVE Rabbit
# DISPLAY
# REGISTER Peacock
# COUNT
# DISPLAY

#ouput
# Animals: Tiger Deer Rabbit
# Total Animals: 3
# Removed: Rabbit
# Animals: Tiger Deer
# Total Animals: 3
# Animals: Tiger Deer Peacock