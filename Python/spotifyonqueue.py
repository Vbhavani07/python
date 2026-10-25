class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
    def add_song(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            temp=self.head
        while temp.next!=None:
            temp=temp.next
            temp.next=new_node
    def playnextsong(self):
        if self.head==None:
            print("no song ton play")
            return
        print("delete a song:",self.head.next)
    def currentsong(self):
        print(self.head.data,'is the current song')
    def lastsong(self):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        print(temp.data,'is the last added sond')
    def dispaly(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
a=queue()
print("1.add song")
print("2.playnextsong")
print("3. ")
print("4. Exit")
while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        page = input("Enter Page Name: ")
        back.push(current)
        current = page
        print("enter opening page:",current)
        forward.clear()
    elif choice == 2:
        if back.top == None:
            print("No Previous Page")
        else:
            forward.push(current)
            current = back.pop()
            print("backward:",current)
    elif choice == 3:
        if forward.top == None:
            print("No Forward Page")
        else:
            back.push(current)
            current = forward.pop()
            print("forward:",current)
    elif choice == 4:
        break
    else:
        print("Invalid Choice")
        break
