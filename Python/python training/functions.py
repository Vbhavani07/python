# def add(x,y):
#     return x+y
# a=5
# b=6
# print(add(a,b))

# def add(x,y=50):
#     return x+y
# a=5
# b=6
# print(add(a))

# def add(x,y=0):
#     a=x+y
#     return a
# a=5
# b=6
# print(add(b))

# def add(x,y):
#     z=x+y
#     return z
# a=5
# b=6
# print(add(b,a))

#ip=22,divisors=1,2,11,add=1+2+11=14
# def div(x):
#     count=0
#     for i in range(1,x):
#         if x%i==0:
#             count+=i
#     return count
# x=22
# print(div(x))

def uprod(L):
    count=0
    for i in range(len(L)):
        for j in range(1,len(L)):
            if L[i]==L[j]:
                L.pop(i)
    else:
        count+=L[i]
        return count
L=[2,5,4,7,9,2,4,8]
print(uprod(L))