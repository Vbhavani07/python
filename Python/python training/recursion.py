#recursion
# def sample():       
#     print("x")                   # in pyton recursion stop with some limit with recursive error 
#     sample()
# sample()


# def  print_numbers(n):
#     if n==0:
#         return
#     print_numbers(n-1)
#     print(n)
# n=int(input())
# print_numbers(n)
    

# def even_numbers(n):
#     if n<0:
#         return
#     even_numbers(n-2)
#     print(n)
# n=int(input())
# even_numbers(n)


##even numbers
# def even_numbers(n):
#     if n<0 :
#         return
#     # if n%2==0:
#     #   print(n)          ##reverse order
#     even_numbers(n-1)
#     if n%2==0:
#       print(n)           # # starting form 0
# n=int(input())
# even_numbers(n)


# ##odd numbers
# def even_numbers(n):
#     if n<0 :
#         return
#     # if n%2!=0:
#     #   print(n)          ##reverse order
#     even_numbers(n-1)
#     if n%2!=0:
#       print(n)            ## starting from 0   #this print is called call stack
# n=int(input())
# even_numbers(n)


#sum of n mumbers
# def sum_numbers(n):
#     if n==1:
#         return 1
#     return n+sum_numbers(n-1)
# n=int(input())
# print(sum_numbers(n))

#find the factorial of a number
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# n=int(input())
# print(factorial(n))

# find the fibonaci series using recursion
# def fibonaci(n):
#     if n==0 or n==1:
#         return 1
#     return fibonaci(n-1)+fibonaci(n-2)
# n=int(input())
# print(fibonaci(n))
# for i in range(n):
#  print(fibonaci(i))

##fibanoci series from 0
# def fibonaci(n):
#     if n==0:
#         return 0
#     if n==1:
#        return 1
#     return fibonaci(n-1)+fibonaci(n-2)
# n=int(input())
# print(fibonaci(n))
# for i in range(n):
#  print(fibonaci(i))

#revere of a string using recursion
# def reverse(s):
#    if s=="":
#       return ""
#    return reverse(s[1:])+s[0]
# s=input()
# print(reverse(s))

# #palindrome or not using recursion
# def palindrome(s):
#    if s=="":
#       return ""
#    elif s==s[::-1]:
#       print("palindrome")
#    else:
#       print("not palindrome")
# s=input()
# palindrome(s)


# #find the reverse of a number using recursion/wrong
# def reverseofnum(n):
#    if n=="":
#       return "" 
#    s=n%10
#    return reverseofnum(s)
# n=int(input())
# print(reverseofnum(n))

#count the number of digits using recursion
# def numofdigits(n):
#    if n=="":
#       return "" 
#    while n==0:
#     s=n%10
#     c+=1
#    return numofdigits(c)
# n=int(input())
# print(numofdigits(n))

#sum of digits using recusion
def numofdigits(n):
   if n=="":
      return "" 
   while n==0:
    a+=n%10
    return numofdigits(a)
n=int(input())
print(numofdigits(n))

#product of digits using recursion
#find GCD using recursion # use gcd formula