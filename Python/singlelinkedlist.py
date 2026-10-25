# Singly Linked List with Dynamic Input

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # Insert at Position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # Delete at Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next


    # Delete at End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None


    # Delete at Position
    def delete_position(self, position):

        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp.next is None:
                print("Invalid Position")
                return
            temp = temp.next

        temp.next = temp.next.next


    # Display List
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program

ll = SinglyLinkedList()

while True:

    print("\n--- Singly Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:
        data = int(input("Enter value: "))
        ll.insert_beginning(data)


    elif choice == 2:
        data = int(input("Enter value: "))
        ll.insert_end(data)


    elif choice == 3:
        data = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        ll.insert_position(data, pos)


    elif choice == 4:
        ll.delete_beginning()


    elif choice == 5:
        ll.delete_end()


    elif choice == 6:
        pos = int(input("Enter position: "))
        ll.delete_position(pos)


    elif choice == 7:
        ll.display()


    elif choice == 8:
        print("Program terminated")
        break


    else:
        print("Invalid choice")