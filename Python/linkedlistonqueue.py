class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
     self.head=None
    def enqueue(self,data):
       new_node=Node(data)
       if self.head==None:
          self.head=new_node
          return
       else:
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def delete_head_dequeue(self):
       if self.head==None:
        print("queue underflow")
        return
       self.head=self.head.next
    # def peek(self):
    #    if self.head==None:
    #     print("queue is empty")
    #     return
    #    else:
          
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

ob=queue()
ob.enqueue(10)
ob.enqueue(20)
# ob.delete_head_dequeue()
ob.display()
