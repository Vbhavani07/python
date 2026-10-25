#SERIES
# n=6
# while n!=1:
#    print(n, end=" ,") 
#    if n%2==0:
#        n=n//2
#    else:
#        n=n*3+1
# print(1)

#ADDING DIGITS
# a=392
# s=0
# while a>0:
#     d=a%10
#     s+=d
#     a//=10
# print(s)

# n=int(input())
# a=0
# s=0
# while n>0:
#     a+=n%10
#     n//=10
# print(a)
 
# SUM OF DIGITS UNTIL SINGlE DIGIT    
# n=int(input())
# s=0
# while n>9:
#     s=0
#     while n>0:
#       d=n%10
#       s+=d
#       n//=10
#     n=s
# print(n)

#ADDING DIGITS UNTIL SINGLE DIGIT
# n=int(input())
# while n>9:
#     s=0
#     while n>0:
#         d=n%10
#         s+=d
#         n//=10
#     n=s
# print(s)

#ADDING DIGITS UNTIL SINGLE DIGIT
# n=int(input())
# s=0
# if n>1:
#     s=1+(n-1)%9
# print(s)

# n=int(input())
# for i in range(1,n+1):
#    print(i)
   
# n=int(input())
# for i in range(1,n):
#     if i==6:
#         continue
#     print(i,end=" ")
#     n=n-1
# else:
#     print(n)
#     print("done")

# n=int(input())
# for i in range(1,n):
#    if n==6:
#        break
#    print(i,end=" ")
# else:
#     print("Done")
 
# n=int(input())
# for num in range(2,n+1):
#     for i in range(2,num):
#           if num%i==0:
#             break 
#     else:
#         print(num, end=" ")       
        
# SERIES 0.5 1.5 4.5 13.5 40.5 121.5     
# n=6
# a=0.5
# i=1
# while(i<=n):
#   print(a, end=" ")
#   a=a*3
#   i=i+1

