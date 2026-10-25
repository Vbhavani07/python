#take array find key element present in the array using binary search

# a=list(map(int,input().split()))
# k=int(input())
# start=0
# end=len(a)-1
# while start<=end:
#     mid=(start+end)//2
#     if k==a[mid]:
#         print("element found at index:",mid)
#         break
#     elif k<a[mid]:
#         end=mid-1
#     elif k>a[mid]:
#         start=mid+1
# else:
#     print("element not found")


#first occurence of the element in the array using binary search  #doubt

# a=list(map(int,input().split()))
# key=int(input())
# start=0
# end=len(a)-1
# while start<=end:
#     mid=(start+end)//2
#     if key==a[mid]:
#         if mid==0 or a[mid-1]!=key:
#            print("element found at index:",mid)
#            break
#         else:
#             end=mid-1
#     elif key<a[mid]:
#        end=mid-1
#     elif key>a[mid]:
#         start=mid+1
# else:
#     print("element not found")
  

#find the count of occurrence of key element in array using binary search
# a=list(map(int,input().split()))
# key=int(input())
# count=0
# start=0
# end=len(a)-1
# while start<=end:
#     mid=(start+end)//2
#     if a[mid]==key:
#         count+=1
#     if key<=a[mid]:
#         for i in range(0,mid-1):
#            end=mid-i
#            if key==a[mid-1]:
#             count+=1
#     if key>=a[mid]:
#         for i in range(mid+1,len(a)):
#               start=mid+i
#               if key==a[mid+1]:
#                count+=1
# print(count)

           #(or)
# a=list(map(int,input().split()))
# key=int(input())
# count=0
# start=0
# end=len(a)-1
# while start<=end:
#     mid=(start+end)//2
#     if a[mid]==key:
#         count+=1
#         for i in range(0,mid-1):
#             if a[i]==key: 
#               count+=1
#         for i in range(mid+1,len(a)):
#             if a[i]==key:
#                count+=1
#         print(count)
# else:
#     print("element not found")

#less element than key
# a = list(map(int,input().split()))
# key = int(input())

# low = 0
# high = len(a) - 1
# while low <= high:
#     mid = (low + high) // 2
#     if a[mid] >= key:
#         high = mid - 1
#     else:
#         low = mid + 1

# if high>= 0:
#     print("Element:", a[high])
# else:
#     print("No element found")

# #greater element than key
# a = list(map(int, input().split()))
# key = int(input("Enter key: "))
# a.sort()
# low = 0
# high = len(a) - 1
# while low <= high:
#     mid = (low + high) // 2
    
#     if a[mid] <= key:
#         low = mid + 1
#     else:
#         high = mid - 1
# if low < len(a):
#     print("Element:", a[low])
# else:
#     print("No element found ")

#using binary search peak element #wrong it gives only one side either left or right
# a=list(map(int,input().split()))
# a.sort()
# low=0
# high=len(a)-1
# # mid=(low+high)//2
# while low<=high:
#     mid=(low+high)//2
#     if a[mid-1]==a[mid]:
#        print("peak:",mid)
#        break
#     elif a[mid+1]==a[mid]:
#        print("peak:",mid)
#        break
#     else:
#       high=mid+1
     

#peak elemnet on unsorted array
a=list(map(int,input().split()))
low=0
high=len(a)-1
while low<=high:
    mid=(low+high)//2
    # for i in range(1,len(a)-1):
    if a[mid]>=a[mid+1] and a[mid]>=a[mid-1]:
        print(a[mid])
        break





