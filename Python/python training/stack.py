#Display original list
# n=int(input())
# List=[]
# for i in range(n):
#    v=int(input())
#    list.append(v)
# print(list)

#add value at end
# l=list(map(int,input().split()))
# l.append(50)
# print(l)

#insert value 50 at index 2
# n=int(input())
# list=[]
# for i in range(n):
#     v=int(input())
#     list.append(v)
# list.insert(2,50)
# print(list)

#extend the list with another list
# n=int(input())
# list=[]
# for i in range(n):
#     v=int(input())
#     list.append(v)
# list.extend([15,30,19])
# print(list)

#count how many times 45 appears in the list
# n=int(input())
# list=[]
# for i in range(n):
#     v=int(input())
#     list.append(v)
# a=list.count(45)
# print(list)
# print(a)

#index position of 90
# n=int(input())
# list=[]
# for i in range(n):
#     v=int(input())
#     list.append(v)
# list
# print(list)
#remove first occurance of 45




#reverse
# n=int(input())
# list=[]
# for i in range(n):
#     v=int(input())
#     list.append(v)
# list.reverse()
# print(list)


#find max,min,sum,avg
# n=int(input())
# list=[]
# for i in range(n):
#     v=int(input())
#     list.append(v)
# print(max(list))
# print(min(list))
# print(sum(list))
# print((list))


#create stack using list with size 5
# stack=[]
# stack.append(12)
# stack.append(9)
# stack.append(4)
# stack.append(3)
# stack.append(7)
# print(stack)

# stack=[]
# n=int(input())
# for i in range(n):
#    v=int(input())
#    stack.append(v)
# print(stack)

#peek an element from a stack and display stack
# stack=[]
# n=int(input())
# for i in range(n):
#    v=int(input())
#    stack.append(v)
# print(stack)
# print(stack[-1])
#pop
# stack=[]
# n=int(input())
# for i in range(n):
#    v=int(input())
#    stack.append(v)
# print(stack)
# print(stack.pop())


#stack operations
# class stack:
#     def __init__(self):
#       self.list=[]
#     def push(self,v):  #push elements using append
#        self.list.append(v)
#     def pop(self):   # pop elements
#        self.list.pop()
#        print(self.list)
#     def peek(self):  # top element of stack
#        self.list[-1]
#        print(self.list)
#     def length(self):  #size of stack
#        self.list
#     def empty(self):  #is empty checking
#        self.list
#        if len(s.list)==0:
#           print("empty")
#        else:
#           print("not empty")
# s=stack()
# s.push(4)
# s.push(7)
# s.push(8)
# print(s.list)
# s.pop()
# print(s.list)
# print(len(s.list))
# s.empty()

# class stack:
#     def __init__(self):
#       self.list=[]
#     def push(self,v):  #push elements using append
#        self.list.append(v)
#        print("pushed element:",v)
#     def pop(self):   # pop elements
#         if len(self.list)==0:
#           print("stack underflow")
#         else:
#            print("popped element",self.list.pop())
#     def peek(self):  # top element of stack
#        self.list[-1]
#        print(self.list)
#     def display(self):
#        self.list
#        print(s.list)
#     def exit(self):
#        self.exit


#stack operations
# s=[]
# n=4
# print("1(push),2.(pop),3.(peek),4.(display),5.(exit)")
# while True:
#    choice=int(input("enter your choice:4"))
#    if choice==1:
#     for i in range(n):
#         v=int(input("enter element:"))
#         s.push(v)
#    elif choice==2:
#     s.pop()
#    elif choice==3:
#     s.peek()
#    elif choice==4:
#     s.display()
#    elif choice==5:
#      s.exit()
#      break
#    else:
#      break

#implement stack overflow and underflow conditions #wrong error happen
# class stack:
#     def __init__(self):
#         self.list=[]
#     def overshow(self,l):
#         self.l
#         n=int(input()) 
#         choice=int(input())
#         print("1(push),2.(pop)")
#         if choice==1:
#           if len(self.list)==n:
#             print("stack overflow")
#           else:
#             l=int(input("enter element"))
#             self.list.append(l)
#             print("element pushed",l)
#     def undershow(self):
#         if choice==2:
#            if len(self.list)==0:
#             print("underflow")
#            else:
#             print("pop element:",stack.pop())
# s=stack()
# s.overshow
# s.undershow

#implement stack overflow and underflow conditions
# n=int(input())
# stack=[]
# print("1(push),2.(pop),3.(peek),4.(display),5.(exit)")
# while True:
#    choice=int(input("enter your choice:"))
#    if choice==1:
#     if len(stack)==n:
#       print("stack overflow")
#       break
#     else:
#          list=int(input("enter element:"))
#          stack.append(list)
#          print("Element pushed")
#    elif choice==2:
#        if len(stack)==0:
#           print("Stack underflow")
#        else:
#          a=stack.pop()
#          print("popped element",a)


#paranthesis are matching or not
s = input("Enter brackets: ")
stack = []
is_matching = True

for i in s:
    if i == "(" or i == "{" or i == "[":
        stack.append(i)
    elif i == ")":
        if len(stack) == 0 or stack.pop() != "(":
            is_matching = False
            break
    elif i == "}":
        if len(stack) == 0 or stack.pop() != "{":
            is_matching = False
            break
    elif i == "]":
        if len(stack) == 0 or stack.pop() != "[":
            is_matching = False
            break
if is_matching and len(stack) == 0:
    print("Matching")
else:
    print("Not Matching")




    
   
   
# #reverse a string using stack 
# string = input("Enter a string: ")
# stack = list(string)
# reversed_string = ""

# while stack:
#     reversed_string += stack.pop()

# print("Reversed string:", reversed_string)


# #reverse a number using stack
# number_input = input("Enter a number: ")
# stack = list(number_input)
# reversed_number_str = ""

# while stack:
#     reversed_number_str += stack.pop()

# reversed_number = int(reversed_number_str)
# print("Reversed number:", reversed_number)



#check whether an expression contain duplicate paranthesis #((a+b)) #duplicate found
# expression = input("Enter an expression: ")
# stack = []
# has_duplicate = False

# for char in expression:
#     if char != ')':
#         stack.append(char)
#     else:
#         elements_inside = 0
#         while stack and stack[-1] != '(':
#             stack.pop()
#             elements_inside += 1
        
#         if stack:
#             stack.pop() 
            
#         if elements_inside <= 1:
#             has_duplicate = True
#             break

# if has_duplicate:
#     print("Duplicate parentheses found!")
# else:
#     print("No duplicate parentheses found.")

