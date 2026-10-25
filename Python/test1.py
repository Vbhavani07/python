# #prime number between range
# s=int(input())
# e=int(input())
# for i in range(1,e):
#     if i>1:
#      for j in range(2,i):
#         if i%j==0:
#          break
#         else:
#          print(i,end=" ")
#          break


#prime factors
# n=int(input())
# print("prime factor are:")
# for i in range(2,n+1):
#   while n%i==0:
#     print(i)
#     n=n//i

#print the unique elemnets by comparig with one set as s and list as l
# l=list(map(int,input().split()))
# s={2,3,4}
# l1=[]
# for i in l:
#     if i not in s:
#         l1.append(i)
# print(l1)

#test hard sum
n,q=map(int,input().split())
mod=1000000007
arr=list(map(int,input().split()))
forb=set()
for num in arr:
    x=num
    for i in range(2,x+1):
        while x%i==0:
            forb.add(i)
            x=x//i
for y in range(q):
    l,r=map(int,input().split())
    primes=[]
    for i in range(l,r+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i>1:
                primes.append(i)
    com=[]
    for k in primes:
        if k not in forb:
            com.append(k)
    ans=0
    w=1
    for i in com:
        ans=ans+(i*w)
        w=w+1
    ans=ans%mod
    print(ans)
        





 