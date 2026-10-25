# # List=list(map(int,input().split()))
# # print(List)

# #Append is used to add element at end
# # List=list(map(int,input().split()))
# # List.append(9)
# # print(List)

# #Insert is used to insert values based on index
# # List=list(map(int,input().split()))
# # k=7
# # List.insert(2,k)
# # print(List)

# #Ascending order of elements in the list
# # List=list(map(int,input().split()))
# # for i in range(len(List)-1):
# #     for j in range(len(List)-i-1):
# #         if List[j]>List[j+1]:
# #             List[j],List[j+1]=List[j+1],List[j]
# # print(List)

# #Descending order of elements in the list
# # List=list(map(int,input().split()))
# # for i in range(len(List)-1):
# #     for j in range(len(List)-i-1):
# #         if List[j]<List[j+1]:
# #             List[j],List[j+1]=List[j+1],List[j]
# # print(List)


# #Only for storing
# # List=list(map(int,input().split()))
# # List.sort
# # print(List)

# #To sort the list using sorted function
# # List=list(map(int,input().split()))
# # print(sorted(List))

# # L1=list(map(int,input().split()))
# # L2=list(map(int,input().split()))
# # check=True
# # if len(L1)==len(L2):
# #     for i in range(len(L1)):
# #         if L1[i]<L2[i]:
# #             check=False
# #         if check:
# #             print("compatible")
# #         else:
# #             print("Not compatible")
# # else:
# #     print("Not compatible")
            
# # Zero's in list add at last          
# # L=list(map(int,input().split()))
# # for i in range(len(L)):
# #     if L[i]==0:
# #         L.remove(0)
# #         L.append(0)
# # print(L)

# #Second largest occurrence count
# # L=list(map(int,input().split()))
# # max=L[len(L)-1]
# # sec_max=0
# # count=0
# # for i in L:
# #     if i<max and sec_max<max:
# #         sec_max=i
# # for i in L:
# #     if sec_max==i:
# #         count+=1
# # print(count)

# #Sum of even numbers and odd numbers in a list
# # L=list(map(int,input().split()))
# # e=0
# # o=0
# # for i in range(len(L)):
# #     if L[i]%2==0:
# #         e+=L[i]
# #     else:
# #         o+=L[i]
# # print(e)
# # print(o)

# #2D LIST
# # n=int(input())
# # List=[]
# # for i in range(n):
# #     row=list(map(int,input().split()))
# #     List.append(row)
# # print(List)

# # n=int(input())
# # List=[]
# # for i in range(n):
# #     row=list(map(int,input().split()))
# #     List.append(row)
# # for i in range(n):
# #     print(List[i])

# # n=int(input())
# # List=[]
# # for i in range(n):
# #     row=list(map(int,input().split()))
# #     List.append(row)
# # for i in range(n):
# #     for j in range(len(List)):
# #         print(List[i][j],end=" ")
# #     print()

# # n=int(input())
# # List=[]
# # check=True
# # for i in range(n):
# #     row=list(map(int,input().split()))
# #     List.append(row)
# # for i in range(n):
# #     for j in range(n):
# #         print(List[i][j],end=" ")
# #     print()
# # for i in range(1,n):
# #     for j in range(i):
# #         if List[i][j]!=0:
# #             check=False
# # if check:
# #     print("Upper tiangle")
# # else:
# #     print("Not a upper triangle")


# # n=int(input())
# # k=1
# # m=0
# # L=list(map(int,input().split()))
# # L.reverse()
# # print(*L)
# # for i in range(n):
# #     for j in range(n):
# #        if L[j]==0:
# #            del L[j]
# #            L.insert(j,k)
# #        else:
# #            del L[j]
# #            L.insert(j,m)
# # print(*L)


# #Reverse
# # n=int(input())
# # List=[]
# # for row in range(n):
# #     L=list(map(int,input().split()))
# #     List.append(L)
# # for row in range(0,n):
# #     for col in range(n-1,-1,-1):
# #         print(List[row][col],end=" ")
# #     print()
    
# #90 degree's angle
# # n=int(input())
# # List=[]
# # for row in range(n):
# #     L=list(map(int,input().split()))
# #     List.append(L)
# # for col in range(0,n):
# #     for row in range(n-1,-1,-1):
# #         print(List[row][col],end=" ")
# #     print()
    
# n=3
# L=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(n):
#      for j in range(n):
#         if i==j:
#             s=0
#             count=0
#             for x in range(i-1,i+2):
#                 for y in range(j-1,j+2):
#                     if x==i and y==j:
#                         continue
#                     if 0<=x<n and 0<=y<n:
#                         s+=L[x][y]
#                         count+=1
#             print(s,count)

# L=[5,6,7,8,14,23,20]
# key=15
# L.sort()
# start=0
# end=len(L)-1
# while start<=end:
#     mid=(start+end)//2
#     if L[mid]==key:
#         print(f"position of key:{mid}")
#         break
#     elif L[mid]>key:
#         end=mid-1
#     else:
#         .start=mid+1    


# L=[5,8,6,4,7,11,1]
# k=7
# for i in L:
#     if i==k:
#         print('element found')
#         break
# else:
#     print('not element found')    

#Zig-Zag pattern
# m=3
# n=3
# List=[]
# s=0
# for i in range(n):
#     L=list(map(int,input().split()))
#     List.append(L)
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1 or i==0 or i==n-1:
#              s+=List[i][j]
#     print(s)

# reverse even row
# n=3
# m=4
# List=[]
# for i in range(n):
#     row=list(map(int,input().split()))
#     List.append(row)
# for i in range(n):
#     for col in range(m):
#         if i%2!=0:
#             print();
            
# a,*b,c=(1,2,3,4,5)

# print(b);