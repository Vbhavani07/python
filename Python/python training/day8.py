#PATTERNS
n=int(input())
a=1
for i in range(n):
    for j in range(i):
        print(a,end="")
        a+=1
    for j in range(n-i):
        print("0",end="")
    print()
    
# n=int(input())
# a=1
# for i in range(n):
#     for j in range(n):
#         if i%2==0  and j!=j-1:
#              print(a,end=' ')
#              a+=1
#         elif i%2!=0 and j!=j-1:
#               print(a,end=" ")
#               a-=1
#     print()
#     a+=3      

# n=int(input())
# a=1
# for i in range(n):
#     for j in range(n):
#         if a%2!=0 :
#             print(a,end=" ")
#             a+=1 
#         else:
#             print(a**2,end=" ")
#             a+=1
#     print()

# rows=3
# col=4
# a=1
# for j in range(col):
#     for i in range(rows):
#         if j%2==0 and i!=rows-1:
#             print(a)
#             a+=1
#         elif j%2!=0 and i!=rows-1:
#             print(a**2)
#             a-=1
#     print()  
#     a+=3


            
# s=int(input())
# e=int(input())
# n=s+2
# while n<e:
#     print(n)
#     n+=2

n=int(input())
while n>1:
    for i in range(1,n+1):
        for j in range(1,i):
            if n%j==0:
                print("not prime")
                break
            else:
                print("prime")
    break