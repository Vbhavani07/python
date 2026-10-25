# # n=int(input())
# # a=1
# # for i in range(n):
# #     for j in range(n):
# #         if j%2==0  and i!=i-1:
# #              print(a)
# #              a+=1
# #         elif i%2!=0 and j!=j-1:
# #               print(a)
# #               a-=1
# #     print()
# #     a+=3    
    
# # r=3
# # c=3
# # num=1
# # for row in range(r):
# #       for col in range(c):
# #           print(num,end=" ") 
# #           if col%2==0 and row!=r-1:
# #               num+=1
# #           elif col%2==1 and row!=r-1:
# #               val=-1
# #       print()
# #       val+=3
# # n=5
# # for i in range(0,n):
# #     for j in range(0,n):
# #         if i==0 or j==0 or i==n-1 or j==n-1:
# #             print("* ",end=" ") 
# #         else:
# #             print("  ",end=" ")
# #     print()
    
# n=int(input())
# temp=n
# s=0
# while n>0:
#     fact=1
#     i=1
#     while i<=temp%10:
#         fact*=i
#         i+=1
#         s+=fact
#         temp//=10
        
# if s==n:
#     print("it is a strong number")
# else:
#     print("not a strong number")
          
          
# n=3
# for i in range(n):
#     for j in range(n):
#         if j%2==0:
#             print(((j*n)+(n-i))**2,end=" ")
#         else:
#             print((j*n)+(i+1),end=" ")
#     print()
             
             
# n=int(input())
# a=1
# for i in range(n):
#     for j in range(n):
#         print(a,end=" ")
#         if j<n-1:
#             a+=1
#         if a>n:
#             a=1
#     print()

# n=int(input())
# a=1
# for row in range(n):
#     for col in range(n):
#         print(a,end=" ")
#         if col<n-1:
#             a+=1
#         if a>n:
#             a=1
#     print()
    
# n=int(input())
# for row in range(1,n):
#     for col in range(1,1+row):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for i in range(i+1): 
#         print("*",end=" ")  
#     print()   
        
# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=' ')
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for i in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for i in range(n-i-1):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    

# n=int(input())
# a=1
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print(a,end=" ")
#             a+=2
#         else:
#             print(" ",end=" ")    
#     print()
    
# n=int(input())
# a=10
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2 or i==j or i+j==n-1:
#             print(a,end=" ")
#             a+=1
#         else:
#             print(" ",end=" ")    
#     print()
    
