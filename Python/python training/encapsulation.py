# class A:
#     _a="protected"
#     def show(self):
#       print(self._a)
# class B(A):
#     pass
# s=A()
# s.show()

#private access specifier
# class A:
#     __a="private"
#     def __show__(self):
#       print(self.__a)
# class B(A):
#     print("protected")
    
# s=A()
# s.__show__()

class bank:
    def __init__(self):
        self.__balance=50000
    def show_balance(self):
        print(self.__balance)
class customer(bank):
    def __init__(self):
        bank.__init__(self)
        self.__balance=10000
        pass
b=customer()
b.show_balance()
        