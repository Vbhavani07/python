# d={2:'b',3:'d',5:'k'}
# d[3]="L"
# a=d.pop(2)
# print(d)

# d={2:'b',3:'d',5:'k'}
# d[3]="L"
# a,b=d.popitem()
# print(f"key: {a},value: {b}")
# print(d)


# d={2:'b',3:'d',5:'k'}
# d[3]="L"
# d[9]="Bhavani"
# print(d)

# d={3:"bhavani",4:"krishna",6:"Dhana"}
# for key in d:
#     print(key,end=" ")

# d={3:"bhavani",4:"krishna",6:"Dhana"}
# for key in d:
#     print(key,end=" ")
# print()
# for val in d.values():
#     print(val,end=" ")
# print()
# for val,key in d.items():
#     print(f"{val}:{key}",end=" ")
# print()


#NESTED DICTIONARY
# d={3:"bhavani",4:"krishna",6:"Dhana",7:{1:'a',2:'b',3:'c'}}
# del d[7][1]
# # del d[4]
# # print(d)

# #palindrome
# n="{[(121))]}"
# d={')':'(',']':'[','}':'{'}
# a=[]
# for ch in n:
#     if ch in "{[(":
#        a.append(ch)
#     elif ch in ")}]":
#         if not a or a[-1]!=d[ch]:
#             print("not symmetric")
#             break
#         a.pop()
# if not a:
#     print("symmetric")



#number of houses visited
# n=4
# d=[2,1,3,1]
# a=0
# index=1
# for i in range(1,n):
#     if index<=n:
#         index=index+d[i]
#         a+=1
# print(a)

# a = list((1, 2, 3, 'apple', 4.5))  
# print(a)

# b = list((1,'GFG'))
# print(b)

# a = [x for x in range(5)] 
# b = [x for x in range(7) if x in a and x%2==0] 
# print(b)