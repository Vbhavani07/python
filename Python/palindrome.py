##!
# s=input()
# ans=""
# for i in range(len(s)-1,-1,-1):
#     ans=ans+s[i]
# if s==ans:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


##2
# s=input()
# ans=""
# ans=s[::-1]
# if s==ans:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

##3
# s=input()
# n=len(s)//2
# m=len(s)
# valid=True
# for i in range(n):
#     r=s[i]
#     l=s[m-1-i]
#     if l!=r:
#         valid=False
# if valid:
#     print("palindrome")
# else:
#     print("Not palindrome")

###FUNCTIONS
# def hai(m,n):
#     return m*n
# print(hai(2,3))
 
##table
# def table(n):
#     for i in range(1,11):
#         # print(f"{n} * {i}=",n*i)
#             ##or
#           print(n ,"*" ,i, "=", n*i)
# table(5)

# ab="@"
# print(ord(ab))
# a="A"
# print(ord(a))


##2D Array
# li=[[1,2,3],[4,5,6]]
# rows=len(li)
# col=len(li[0])
# for i in range(rows):
#     for j in range(col):
#         print(li[i][j])

##2D array columns first
# li=[[1,2,3],[4,5,6]]
# rows=len(li)
# col=len(li[0])
# for j in range(col):
#     for i in range(rows):
#       print(li[i][j])

#patterns
# n=int(input())
# for i in range(n):
#     for j in range(n):
#       print("@",end=" ")
#       if j!=n-1:
#         print("_",end=" ")
#     print() 


##patterns
# m=int(input())
# n=int(input())
# for i in range(m):
#     for j in range(n):
#       print("@",end=" ")
#       if j!=n-1:
#         print("_",end=" ")
#     print() 

    #output:
# 3
# 8
# @ _ @ _ @ _ @ _ @ _ @ _ @ _ @ 
# @ _ @ _ @ _ @ _ @ _ @ _ @ _ @ 
# @ _ @ _ @ _ @ _ @ _ @ _ @ _ @ 

# m=int(input())
# n=int(input())
# for i in range(m):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==m-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    #output
#4
# 4
# * * * * 
# *     * 
# *     * 
# * * * * 

# m=int(input())
# n=int(input())
# for i in range(m):
#     for j in range(n):
#         if j==0 or j==1 or j==2 or j==3:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# r=int(input())
# c=int(input())
# for i in range(r):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(c):
#         print("*",end=" ")
#     print()

#op
# 4
# 4
# * * * * 
#   * * * * 
#     * * * * 
#       * * * * 


r=int(input())
c=int(input())
for i in range(r):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(r):
    for  j in range(c,1,-1):
        print("*",end=" ")
    print()
