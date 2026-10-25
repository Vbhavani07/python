class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
       self.head=None
    def insert_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
          temp=self.head
          while temp.next!=None:
            temp=temp.next
          temp.next=new_node
    def insert_pos(self,pos,data):
        new_node=Node(data)
        if pos==0:
          new_node.next=self.head
          self.head=new_node
          return
        temp=self.head
        for i in range(pos-1):
            if temp==None:
                print("Invalid Position")
                return
            temp=temp.next
        if temp==None:
            print("Invalid Position")
            return
        new_node.next=temp.next
        temp.next=new_node
    def delete_head(self):
        if self.head==None:
           print("List is empty")
           return
        self.head=self.head.next
    def delete_end(self):
        if self.head==None:
          print("empty List")
          return
        if self.head.next==None:
          self.head=None
          return
        temp=self.head
        while temp.next.next!=None:
          temp=temp.next
        temp.next=None
    def delete_pos(self,pos):
       if self.head==None:
          print("list is empty")
          return
       temp=self.head
       for i in range(pos-1):
          temp=temp.next
       if temp==None or temp.next==None:
          print("invalid position")
          return
       temp.next=temp.next.next
    def display(self):
        temp=self.head
        while temp!=None:
          print(temp.data,end="->")
          temp=temp.next
        print("None")
ob=linkedList()
ob.insert_head(10)
ob.insert_head(20)
ob.insert_end(30)
ob.insert_pos(2,50)
ob.delete_head()
ob.delete_end()
ob.delete_pos(1)
ob.display()
  

