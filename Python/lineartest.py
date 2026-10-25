n=int(input())
l=[]
count=0
for i in range(n):
    k=int(input())
    l.append(k)
m=int(input())
for i in range(len(l)-1,-1,-1):
    if k==l[i]:
        print(f"key element {l[i]} found at",i)
        break
    else:
        print("no element found")