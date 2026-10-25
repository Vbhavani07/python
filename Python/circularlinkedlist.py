class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_head(self,data):
        newnode=Node(data)
        if self.head==None:
             self.head=newnode
             self.tail=newnode
             self.tail.next=self.head
             return
        newnode.next=self.head
        self.tail.next=newnode
        self.head=newnode
    def insert_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
            return
        self.tail.next=newnode
        self.tail=newnode
        self.tail.next=self.head
       
    def pos(self,pos,data):
        if pos==1:
            self.insert_head(data)
            return
        newnode=Node(data)
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        newnode.next=temp.next    
        temp.next=newnode
        if temp==self.tail:
            self.tail=newnode
            self.tail.next=self.head
    def delete_head(self):
        if self.head==self.tail:
            self.head=None
            self.tail=None
            return
        self.head=self.head.next
        self.tail.next=self.head
    def delete_end(self):
        if self.head==None:
            print("linkedlist is empty")
            return
        if self.head==self.tail:
            self.head=None
            self.tail=None
            return
        temp=self.head
        while temp.next!=self.tail:
                temp=temp.next
        temp.next=self.head
        temp.tail=temp  
    def delete_pos(self,pos):
        if pos==1:
            self.delete_head()
            return
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        delete_node=temp.next
        temp.next=delete_node.next
        if delete_node==self.tail:
            self.tail=temp
            self.tail.next=self.head
    def display(self):
        if self.head==None:
            print("linkedlist is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
              break
        print("Head")
ob=circularlinkedlist()
ob.insert_head(34)
ob.insert_head(23)
ob.insert_head(56)
ob.insert_end(90)
ob.pos(2,45)
# ob.delete_head()
# ob.delete_end()
ob.delete_pos(3)
ob.display()



