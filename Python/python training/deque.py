# from collections import deque
# d=deque()
# d.append(6)
# d.append(7)
# d.append(5)
# d.append(4)
# print(d)
# print(d.pop())
# print(d.popleft())

# from collections import deque
# d=deque()
# d.append("google")
# d.append("youtube")
# print("visit:",d[0])
# print("visit:",d[-1])
# print("Back:",d[0])
# print("current:",d[0])


#browser history
from collections import deque
n=int(input())
history=deque()
for i in range(n):
    op=input().upper().split()
    if op[0]=="VISIT":
        history.append(op[1])
        print(history)
    elif op[0]=="CURRENT":
        if len(history)>1:
            t=history.pop()
            history.append(t)
            print("current:",t)
    elif op[0]=="BACK":
        if len(history)==0:
            print("no page")
        else:
            print("back",history[0])
    elif op[0]=="FORWARD":
        if len(history)==0:
            print("no pages")
        else:
            print("forward:",history[1])
            


##  check the string is palindrome or not using deque 
# from collections import deque
# s=input()
# d=deque(s)
# #   a=list(s)
# #   for i in a:
# #     d.append(i)
# if  d[0]==d[-1]:
#     while len(d)>1:
#         d.pop()
#         d.popleft()
#         print("palindrome")
#         break
# else:
#     print("not palindrome") 

               #(or)
# from collections import deque
# s=input()
# d=deque(s)
# is_pal=True
# while len(d)>1:
#     if d.popleft()!=d.pop():
#         is_pal=False
#         break
# if is_pal==True:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



#find the highest sub array sum in the queue(consecutive sum)
# arr=[-1,3,7,-5,-7]
# max=0
# c=arr[0]
# for i in range(len(arr)):
#    if arr[i]>c+arr[i]:
#       print(c+arr[i])
      

#second highest element implement using deque
# from collections import deque
# d=deque([10,20,30,50,70])
# first=d[0]
# second=d[1]
# # if second>first:                 ##not mandory this condition
# #     first,second=second,first
# for i in d:
#     if i>first:
#         second=first
#         first=i
#     elif i>second and i!=first:
#         second=i
# print(second)
      
#max sum subarray using deque
# from collections import deque
# d=deque(list(map(int,input().split())))
# hmax=d[0]
# for i in range(len(d)):
#     current=0
#     for j in range(i,len(d)):
#         current+=d[j]
#         hmax=max(hmax,current)
# print(hmax)    





