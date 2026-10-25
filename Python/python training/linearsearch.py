##linear search
# l=list(map(int,input().split()))
# k=int(input())
# for i in l:
#     if i==k:
#         print("element found")
#         break
# else:
#     print("element not found")


#find second least element using linear search and index of element #not completed
# l=list(map(int,input().split()))
# first=l[0]
# second=l[1]
# if second<first:                 
#     first,second=second,first
# for i in l:
#     if i<first:
#         second=first
#         first=i
#     elif i<second and i!=first:
#         second=i
# print(second)

#first non repeating element 
# s=input()
# for i in range(len(s)):
#     c=0
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             c+=1
#     if c==1:
#         print(s[i])
#         break

# #find first and highest repeating character in string using linear search #not completed
# s=input()
# for i in range(len(s)):
#     c=0
#     # a=s.count(i)
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             c+=1
#             # if c>1 and c<a:
#             #     print("most repeated",s[i])
# if c>1:
#     print(s[i])
    
                
#highest repeating character in string
# s=input()
# max=0
# max_i=""
# for i in s:
#     a=s.count(i)
#     if a>max:
#         max=a
#         max_i=i
# print("most repested element",max_i)
# print(max)
 

#find the highest consecutive repeating character in the string
# s=input()
# max_c=0
# c=0
# max_s=s[0]
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c=c+1
#     else:
#         c=0
#     if c>max_c:
#         max_c=c
#         max_s=s[i]
#         print(max_c)
# print(max_s)

#remove duplicate characters in th estring and print unique characters string
# s=input()
# a=set(s)    direct method
# print(*a)

s=input()
a=[]
for i in s:
    if i not in a:
        a.append(i)
print(*a)