arr=[23,67,41,45,78]
n=len(arr)
for i in range(n):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
    arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)