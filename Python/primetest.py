n=int(input())
prime_count=0
composite_count=0
for i in range(n):
    k=int(input())
    count=0
    for m in range(1,k+1):
        if k%m==0:
            count+=1
    if count==2:
          prime_count+=1
    else: 
        composite_count+=1
print("prime numbers count:",prime_count)
print("composite numbers count:",composite_count)

