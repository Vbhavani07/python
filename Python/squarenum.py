n=int(input())
l=[]
count=0
for i in range(n):
    k=int(input())
    l.append(k)
for j in l:
    if int(j**0.5)**2==j:
        count+=1
        print(j,end=" ")
if count==0:
    print("No elements Found")