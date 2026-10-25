# # Longest sequence of 1's count
# def seq(a):
#     max = 0
#     current= 0
#     for i in a:
#         if i == '1':
#             current+= 1
#             if current > max:
#                 max = current
#         else:
#             current= 0
    
#     return max

# a = "1011111011010101"
# print(seq(a))


## count of unique characters
# def unique(a):
#     count=0
#     for i in a:
#         count+=1
#     return count
# a={"a","b","c","d","a","b","c"}
# print(unique(a))

#ascending order of a matrix.
# def matrix(m,n):
#     List=[]
#     for i in range(m):
#         row =list(map(int,input().split()))
#         List.append(row)
#     List.sort()
#     for i in range(m):
#         for j in range(n):
#             print(List[i][j],end=" ")
#     return list
# m=3
# n=4
# print(matrix(m,n))   

 #Lambda function 
# List=[1,2,3,4,5,6]
# even=filter(lambda x: x%2==0,List)
# print(list(even))

# use of reduce
# from functools import reduce
# List=[1,2,3,4,5,6]
# mul=reduce(lambda x,y:x*y,List)
# print(mul)

# map with updating values
# List=[1,2,3,4,5,6,]
# even=map(lambda x: x*2,List)
# print(list(even))
    
# a=1
# b=2
# calc=lambda x,y:(x+y,y-x)
# print(calc(a,b))

#1
n=int(input())
a=[2,3,5,7,8]
b=[3,3,7,9,10]
a.append()

