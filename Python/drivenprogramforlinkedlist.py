class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
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
              temp=temp.next
          new_node.next=temp.next
          temp.next=new_node
      def display(self):
          temp=self.head
          while temp.next!=None:
              temp=temp.next
              print(temp.data,end="->")
l1=linkedlist()
q=int(input())
for i in range(q):
    op=list(map(int,input().split()))
    if op[0]==1:
        l1.insert_head(op[1])
    elif op[0]==2:
        l1.insert_end(op[1])
    elif op[0]==3:
        l1.insert_pos(op[1],op[2])
l1.display()

    