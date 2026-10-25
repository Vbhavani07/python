# stack=[]
# postfix=input("Enter post fix expression")
# for ch in postfix:
#     if ch.isalpha():
#         print("Enter value for ",ch)
#         val=float(input("enter val"))
#         stack.append(val)
#     elif ch=='+':
#         p=stack.pop()
#         q=stack.pop()
#         stack.append(q+p)
#     elif ch=='-':
#         p.stack.pop()
#         q=stack.pop()
#         stack.append(q-p)
#     elif ch=='/':
#         p.stack.pop()
#         q.stack.pop()
#         stack.append(q/p)
# print("Expression value is",stack.pop())

#prefix 
# stack=[]
# prefix=input("Enter prefix expression")
# length=len(prefix)
# for i in range(length-1,-1,-1):
#      ch=prefix[i]
#      if ch.isalpha():
#           print("Enter value for",ch)
#           val=float(input("enter val"))
#           stack.append(val)
#      elif ch=='+':
#           p=stack.pop()
#           q=stack.pop()
#           stack.append(p+q)
#      elif ch=='-':
#           p=stack.pop()
#           q=stack.pop()
#           stack.append(p-q)
#      elif ch=='/':
#           p=stack.pop()
#           q=stack.pop()
#           stack.append(p/q)
# print("Expression value is ",stack.pop())

#postfix to prefix
# import sys
# stack=[]
# oprs=['+','-','*','/']
# postfix=input("Enter postfix expression")
# for ch in postfix:
#     if ch.isalpha():
#         stack.append(ch)
#     else:
#         if ch in oprs:
#             opr1=stack.pop()
#             opr2=stack.pop()
#             stack.append(ch+opr2+opr1)
#         else:
#             print("Invalid symbol")
#             sys.exit()
# print("Prefix expression is",stack.pop())

# #prefix to postfix not completed
# import sys
# stack=[]
# oprs=['+','-','*','/']
# prefix=input("Enter postfix expression")
# for i in range(len(potfix)):
#     ch=prefix[i]
#     if ch.isalpha():
#         stack.append(ch)
#     else:
#         if ch in oprs:
#             opr1=stack.pop()
#             opr2=stack.pop()
#             stack.append(opr1+opr2+ch)
#         else:
#             print("Invalid symbol")
#             sys.exit()
# print("Prefix expression is",stack.pop())

# #infix to postfix
def prec(c):
 if c=='^':
    return 3
 elif c=='/'or c=='*':
    return 2
 elif c=='+'or c=='-':
    return 1
 else:
    return -1
def infixToPostfix(s):
   st=[]
   res=[]
   for c in s:
      if c.isalpha():
         res.append(c)
      elif c=='(':
        st.append('(')z  

      elif c==')':
        while st and st[-1]!='(':
            res.append(st.pop())
        st.pop()
      else:
          while st and st[-1]!='(' and (prec(st[-1]>=prec(c))):
             res.append(st.pop())
          st.append(c)
    while st:
      res.append(st.pop())
      

`1