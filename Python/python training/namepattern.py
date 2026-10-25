# m=9
# n=5
# for i in range(0,m):
#     for j in range(0,n):
#         if i==0 or j==0 or i==m-1 or j==n-1 or i==m//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=5
# m=4
# for  i in range(0,n):
#     for j in range(0,m):
#         if i==0 or i==m//2 or i==n-1 or i==n//2 or i+j==n//2-1 or i+j==n+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()            


# i=int(input())
# e=i-1000
# f=i-e
# d=(i-1000)/100*3
# c=f/100*2
# total=c+d
# print(total)

i=int(input())
d=i-1000
for i in range(0,1000,100):
    i+=2
for j in range(0,d,100):
    j+=3
total=i+j
print(total)
    
    