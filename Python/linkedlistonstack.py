# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def pop(self):
#         if self.head==None:
#             print("Empty linkedlist underflow")
#             return
#         temp=self.head
#         print(temp.data,"deleted")
#         self.head=self.head.next
#     def peek(self):
#         if self.head==None:
#             print("Underflow")
#             return
#         else:
#             print("Top element",self.head.data)
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# obj=stack()
# obj.push(56)
# obj.push(70)
# obj.push(34)
# obj.pop()
# obj.peek()
# obj.display()

#create a stack using linkedlist find the highest data node and least data node(element)
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def max(self):
#        if self.head==None:
#            print("Underflow")
#            return
#        temp=self.head
#        maxx=temp.data
#        while temp!=None:
#             if temp.data>maxx:
#                maxx=temp.data
#             temp=temp.next
#        print("Max",maxx)
#     def min(self):
#         if self.head==None:
#             print("Underflow")
#             return
#         temp=self.head
#         minn=temp.data
#         while temp!=None:
#             if temp.data<minn:
#                minn=temp.data
#             temp=temp.next
#         print("Min",minn)
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next  
#         print("None")
# ob=stack()
# ob.push(56)
# ob.push(87)
# ob.push(34)
# ob.max()
# ob.min()
# ob.display()

#split the stack into even ,odd numbers stack using linkedlist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next  
#         print("None")
# s=stack()
# n=int(input("enter number of elements:"))
# for i in range(n):
#     x=int(input())
#     s.push(x)
# even=stack()
# odd=stack()
# temp=s.head
# while temp!=None:
#     if temp.data%2==0:
#         even.push(temp.data)
#     else:
#         odd.push(temp.data)
#     temp=temp.next
# print("original stack:")
# s.display()
# print("Even stack:")
# even.display()
# print("Odd stack:")
# odd.display()   


# #Browser history stack using linked list 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next  
        print("None")
back=stack()
forward=stack()
current="Home"
n=int(input())
print("1.(push),2.(pop),3.(peek)")
back=stack()
forward=stack()
while True:
    if choice==1:
        n=input("Enter a page:")
        current=



