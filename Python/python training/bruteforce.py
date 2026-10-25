##max sum  and min sum of sub array using function
# def Bruteforcesum(arr):
#     maxsum=arr[0]
#     minsum=arr[0]
#     for i in range(len(arr)):
#         current=0
#         for j in range(i,len(arr)):
#             current+=arr[j]
#             if current>maxsum:
#                 maxsum=current
#             if current<minsum:
#                 minsum=current
#     return maxsum,minsum
# arr=list(map(int,input().split()))
# print(arr)
# r=Bruteforcesum(arr)
# print("maxsum",r[0])
# print("minsum",r[1])


# max and min product of subarray using function
# def Bruteforcesum(arr):
#     maxproduct=arr[0]
#     minproduct=arr[0]
#     for i in range(len(arr)):
#         current=1
#         for j in range(i,len(arr)):
#             current*=arr[j]
#             if current>maxproduct:
#                 maxproduct=current
#             if current<minproduct:
#                 minproduct=current
#     return maxproduct,minproduct
# arr=list(map(int,input().split()))
# print(arr)
# r=Bruteforcesum(arr)
# print("maxproduct",r[0])
# print("minproduct",r[1])

#TSP
n=int(input())
List=[]
cost=0
a=0
for i in range(n):
    row=list(map(int,input().split()))
    List.append(row)
for i in range(n):
    for j in range(n):
        a=List[i]+List[j]
        cost+=a
        print(List[i][j],end=" ")
    print(cost)
    print()
    

        