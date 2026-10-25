#function overloading
# l=[1,2,4,5]
# print(max(l))
# s="bhavani"
# print(max(s))

#operator overloading
# l1=[1,2,3]
# l2=[4,5,6]
# a=10
# b=5
# print(a+b)
# print(l1+l2)

#function overloading (min,max,type,sorted,len)
# l=[1,2,"hello"]
# s='BHAVANI'
# print(len(l))
# print(len(s))

#method overloading
# class addition:
#     def add(self,*args):
#         print(sum(args))
# o=addition()
# o.add(1,2,5)
# o.add(6,7,8,9,15)

#overriding
# class father:
#     def show(self):
#         print("iam father")
# class son(father):
#     def show(self):
#         print(" iam son")
# class daughter(father):
#     def show(self):
#         print("iam daughter")
# s=son()
# s.show()
# d=daughter()
# d.show()

# with super keyword we can  access parent class
# class father:
#     def show(self):
#         print("iam father")
# class son(father):
#     def show(self):
#         super().show()
#         print("iam son")
# class daughter(father):
#     def show(self):
#         print("iam daughter")
# s=son()
# s.show()
# d=daughter()
# d.show()

#error
# class father:
#     def __init___(self,name):
#         self.n=name
# class son(father):
#     def __init__(self,name,id):
#         self.id=id
#         super().__init__(name)
# class daughter(father):
#     def __init__(self):
# s=son()
# print("id:",s.id)
# print("name:",s.n)


