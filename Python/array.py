# import array as ar
# a=ar.array('i',[1,2,3,4,5])
# print(a)


#APPEND AN ELEMENT
# import array as ar
# a=ar.array('i',[1,2,3,4,5])
# print(a)
# k=7
# a.append(k)
# print(a)
# print(a.typecode)

#INSERT
# import array as ar
# a=ar.array('f',[2.5,7,3.4])
# k=67
# a.insert(1,k)
# print(a)

# #POP
# import array as ar
# a=ar.array('i',[2,4,5,6,9])
# # a.pop()
# # a.pop(2)
# # print(a)
# #DELETE
# del a[2]
# print(a)
# del a[1:3]
# print(a)

#SMALLEST ELEMENT 
# import array as ar
# a=ar.array('f',list(map(float,input().split())))
# s=a[0]
# for i in a:
#     if i<s:
#         s=i
# print(int(s))

#LARGEST ELEMENT
# import array as ar
# a=ar.array('f',list(map(float,input().split())))
# s=a[0]
# for i in a:
#     if i>s:
#         s=i
# print(int(s))

#SECOND smallest ELEMENT D
# import array as ar
# a=ar.array('i',list(map(int,input().split())))
# sorted(a)
# s=a[0]
# for i in a:
#     if s<a[i+1] and a[i]<a[i+2]:
#         s=i
# print(a)


#reverse of an element
# import array as arr
# a=arr.array('i',[2,5,7,1])
# print(a[::-1])


# FREQUENCY OF AN ELEMENT D
# import array as ar
# a=ar.array('i',[4,4,6,7,7,5,5,5])
# s=1
# for i in a:
#    if a[i]==a[i+1]:
#     s+=1
#    print(a[i],s)

#FREQUENCY OF A NUMBER
# import array as ar
# a=ar.array('i',[4,4,6,7,7,5,5,5])
# d=[]
# for i in a:
#     if a not in d:
#        print(i,a.count(i))
#        d.append(i)

#REMOVING DUPLICATES
# import array as ar
# a=ar.array('i',[4,4,6,7,7,5,5,5])
# d=[]
# for i in a:
#     if a not in d:
#        d.append(i)
# print(i)

#k-ROTATION\
# import array as ar
# a=ar.array('i',list(map(int,input().split())))
# k=int(input())
# print(a)
# print(a[-k:])
# print(a[:k])
# print(a[-k:]+a[:-k])

#REPEATING ELEMENTS
# import array as ar
# a=ar.array('i',list(map(int,input().split())))
# d=[]
# for i in a:
#     if i not in d:
#           d.append(i)
#     else:
#         print(i)
        
#NON REPEATING
 # import array as ar
 # a=ar.array('i',list(map(int,input().split())))
# d=[]
# for i in a:
#     if i not in d:
#           d.append(i)
#     else:
#         print(i)

#MEDIAN OF ARRAY
# a=list(map(int,input().split()))
# n=int(input())
# a.sort()
# if n%2==0:
#     print(a[n//2-1])
# else:
#     print(a[n//2])
      
#sub array
# n1=list(map(int,input().split()))
# n2=list(map(int,input().split()))
# f=True
# for i in n2:
#     if i in n1:
#         pass
#     else:
#         f=False
#         break
# if f==True:
#     print("Yes")
# else:
#     print("No")
    
#search
# n1=list(map(int,input().split()))
# k=int(input())
# for i in n1:
#     if k in n1:
#         print("element found")
#     else:
#         print("element not found")
#     break


#MISSING NUMBER
# n=int(input())
# a=list(map(int,input().split()))
# n=len(a)
# for i in range(1,n+1):
#    if i not in a:
#        print(i)


# n=int(input())
# a=list(map(int,input().split()))
# for i in a:
#     if i>a
#         Print(i)


# n = int(input())
# s= set()
# for _ in range(n):
#     a, b = map(int, input().split())
#     if (b, a) in s:
#         print(min(a, b), max(a, b))
#         s.add((a, b))
        
    
# pairs = ["1 2", "3 4", "2 1", "5 6", "4 3"]
# s = set()
# for p in pairs:
#     a, b = map(int, p.split())
#     if (b, a) in s:
#         print(min(a, b), max(a, b))
#         s.add((a, b))


# try:
#     x=int(input("enter a numberr:"))
#     print(10/x)

#Zero division error
# x=int(input())
# print(10/x)

#syntax error
# x=str(input()
# print(10/x)

#value error
# x=int(input())
# print(10/x)

#index error
# a=list(map(int,input().split()))
# print(a[10])

# try:
#     x=int(input())
#     print(int(10/x))
# except:
#     print("zero division error")
    
# try:
#     x=int(input())
#     print(x)
# except:
#     print('INVALID INPUT')
# finally:
#     print("done")

#2
# try:
#     x=int(input())
#     y=int(input())
#     print(x/y)
# except ZeroDivisionError:
#     print("zero Division error")
# except:
#     print("error")
# finally:
#     print("done")

# try:
#     a=int(input())
#     b=int(input())
#     o=input("+,*,/,-:")
#     if o=="+":
#         print(a+b)
#     elif o=="-":
#         print(a-b)
#     elif o=="*":
#         print(a*b)
#     elif o=="/":
#         print(a/b)
#     else:
#         print("invalid operator")
# except ValueError:
#     print("Invalid input")
# except:
#     print("INVALID OPERATOR")
# finally:
#     print("done")
        
    
#key error
# dict={1:"Bhavani",2:"suma",3:"sailu"}
# print(dict[4])

#4
# try:   
#   dict={1:"Bhavani",2:"suma",3:"sailu"}
#   print(dict[4])
# except KeyError:
#     print("KEY ERROR")

#5
# try:
#     age=int(input())
#     if age<0:
#         raise Exception("INVALID NUMBER")
#     elif age>=18:
#         print("major")
#     else:
#         print("minor")
# except Exception as e:
#     print(e)

# try:
#     p=input()
#     if len(p)<8:
#         raise Exception("Not a strong password")
#     else:
#         print("stong password")
# except Exception as e:
#     print(e)

# try:
#     age=int(input())
#     if age<18:
#         raise Exception("age must above or equal to 18")
# except Exception as e:
#     print(e)
# except:
#     print("invalid number")
# else:
#     print("eligible")
# finally:
#     print("done")


n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))

len1 = len(n1)
len2 = len(n2)
found = False

# Slide the window across n1
for i in range(len1 - len2 + 1):
    # Take a piece of n1 starting at index 'i' with the same length as n2
    window = n1[i : i + len2]

    # Check if this piece matches n2 exactly
    if window == n2:
        found = True
        break  # Match found! No need to check further.

if found:
    print("Yes")
else:
    print("No")
