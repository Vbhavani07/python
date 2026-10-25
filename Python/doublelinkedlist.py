class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_head(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head==None:
           self.head=new_node
           return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node 
        new_node.prev=temp
    def insert_pos(self,pos,data):
        new_node=Node(data)
        if pos==0:
            self.insert_head(data)
            return
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        new_node.prev=temp
        if temp.next!=None:
            temp.next.prev=new_node
        temp.next=new_node
    def delete_head(self):
        if self.head==None:
           return
        if self.head.next==None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if self.head==None:
            print("List is empty")
            return
        if self.head.next==None:
            self.head=None
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.prev.next=None
    def delete_pos(self,pos):
        if self.head==None:
          print("list is empty")
          return
        temp=self.head
        if temp==None:
          print("invalid position")
          return
        for i in range(pos-1):
          temp=temp.next
        if temp.next!=None:
           temp.next.prev=temp.prev
        temp.prev.next=temp.next
    def display(self):
        temp=self.head
        while temp!=None:
           print(temp.data,end="<->")  
           temp=temp.next
        print("None")
ob=doublelinkedlist()
ob.insert_head(40)
ob.insert_head(30)
ob.insert_end(49)
ob.insert_end(14)
ob.insert_pos(3,50)
ob.delete_head()
ob.delete_end()
ob.delete_pos(2)
ob.display()