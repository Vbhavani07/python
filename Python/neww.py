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
n=int(input())
while True:
    j=int(input())
    if j==1:
        a.add_song("a")
        a.add_song("b")
        a.add_song("c")
        a.add_song("d")
        a.dispaly()
    elif j==2:
        a.playnextsong()
    elif j==3:
        a.currentsong()
    elif j==4:
        a.lastsong()
    elif j==5:
        a.dispaly()
    else:
        break