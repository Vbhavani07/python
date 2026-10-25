# q=[]
# q.insert(0,10)
# q.insert(0,20)
# q.insert(0,30)
# print(q)

# q=[]
# q.insert(0,10)
# q.insert(1,20)
# q.insert(0,30)
# q.insert(1,40)
# q.append(35)
# print(q)

#create a queue name it as queue with the size of 5 elements and print front and rear
# queue=[]
# a=len(queue)
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# queue.append(50)
# print("Front:",queue[0])
# print("Rear:",queue[-1])

#create a queue of fruits apple,guava,mango ,banana,pineapple print front and rear
# fruits=["apple","guava","mango","banana","pineapple"]
# print("Front:",fruits[0])
# print("Rear:",fruits[-1])
# list.index("apple")

# n=int(input())
# fruits=[]
# for i in range(n):
#     a=input()
#     fruits.append(a)
# print("Front:",fruits[0])
# print("Rear:",fruits[-1])


# queue=[]
# queue.insert(0,"apple")
# queue.insert(0,"banana")
# queue.insert(0,"pineapple")
# print(queue)
# print("fornt:",queue[0])
# print("Rear:",queue[-1])

#add an element in queue
# q=[]
# q.append(10)
# q.append(20)
# q.append(40)
# print(q)


#Remove an element
# q=[]
# q.append(10)
# q.append(20)
# q.append(40)
# q.pop(0)
# print(q)

# function to check isempyt() queue
# queue=[]
# queue.append(10)
# queue.append(20)
# if len(queue)==0:
#     print("empty")
# else:
#     print("not empty")

#size of queue
# queue=[]
# queue.append(10)
# queue.append(20)
# a=len(queue)
# print(a)

#initialize empty queue
# myQueue=[]
# myQueue.append(12)
# myQueue.append(13)
# print(myQueue)



# import queue
# q=queue.Queue()
# q.put("task1")
# q.put("task2")
# print(q.queue)


#check the string is palindrome or not using queue #ERROR
# s=input()
# l=list(s)
# f=l[0]
# r=l[-1]
# for i in l:
#     if f==r:
#       l.pop()
#       l.pop(0)
#       print("palindrome")
#       break
# else:
#     print("not palindrome")

# take a queue and print the reverse of a string in queue
# queue=[]
# s=input()
# for i in s:
#    queue.insert(0,i)
# print(*queue)

# (or)

# queue=[]
# s=input()
# for i in s:
#     queue.append(i)
# while queue:
#     print(queue.pop(),end="")



           #(or)

# import  queue
# q=queue.Queue()
# s=input()
# r=[]
# for i in (s):
#    q.put(i)
# print(q.queue)
# for i in q.queue:
#    r.insert(0,i)
# print(r)

#crete a queue with the name of queue class and write functions for all the operations of queue
# class queue:
#     def __init__(self):
#         self.queuee=[]
#     def enqueue(self,val):
#         self.val=val
#         self.queuee.append(val)
#         print("Enqueue:",self.val)
#     def dequeue(self):
#         self.queuee.pop()
#         print("Dequeue:",self.val)
# a=queue()
# a.enqueue(10)
# a.enqueue(20)
# a.dequeue()



# class railway:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,token):
#         self.token=token
#         self.queue.append(token)
#         print("Tokens:",self.token)
#     def dequeue(self):
#         self.queue.pop()
#         print("dequeue:",self.token)
#     def display(self,front,rear,size):
#         self.front=front
#         self.rear=rear
#         self.size=size
# a=railway()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
# a.dequeue()
# print("Front:",a.queue[0])
# print("Rear:",a.queue[-1])
# print("Size:",len(a.queue))


#priority queue not completed
# n=int(input())
# for i in range(n):
#     op=input().upper().split()
#     if op[0]=="ADD":
#         name=op[1]
#         priority=int(op[2])
#         pq.append((priority,name))
#         pq.sort()
#         print(pq)
#     elif op[0]=="NEXT":
#         if pq:
#             print("Next patient:")
  
# #max sum subarray ##error
# import queue
# q=queue.Queue()
# maxsum=q[0]
# for i in range(len(q)):
#     q.append(input())
#     current=0
#     for j in range(i,len(q)):
#         current+=q[j]
#         if current>maxsum:
#             maxsum=current
# print(maxsum)

                 #(or)
# #max sum subarray    
import queue
q = queue.Queue()
n = int(input("Enter size: "))
for i in range(n):
    q.put(int(input()))
arr = []
while not q.empty():
    arr.append(q.get())
maxsum = arr[0]
for i in range(len(arr)):
    current = 0
    for j in range(i, len(arr)):
        current += arr[j]

        if current > maxsum:
            maxsum = current
print("Maximum Subarray Sum =", maxsum)