# arr=list(map(int,input().split()))
# dep=list(map(int,input().split()))
# a=arr+dep
# l=[]
# c_sum=[]
# sum=0
# a.sort()
# print(a)
# for i in a:
#     if i in arr:
#         l.append(1)
#     else:
#         l.append(-1)
# print(l)
# for i in l:
#       sum+=i
#       c_sum.append(sum)
# print(max(c_sum))
si=list(map(int,input().split()))
si.sort()
l=[]
final=[]
a=0
cost=0
for i in range(len(si)):
     l.append(si[i])
     a=sum(l)
     final.append(a)
print(sum(final)-si[0])  



