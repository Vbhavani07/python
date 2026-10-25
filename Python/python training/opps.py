# class student:
#     def college(cname):
#         cname="BVCITS"
#         print(cname)   
# a=student()
# a.college() 

# class employee:
#     def company(companyname):
#         companyname="TCS"
#         print(companyname)
# a=employee()
# a.company()

# class dog:
#     dog_type="Husky"  #CLASS VARIABLE
#     def __init__(self,name,age): # NAME AND AGE ARE INSTANCE VARIABLES
#         self.N=name
#         self.A=age
#         print(name,age)
#         print(self.dog_type)
# dog1=dog("nimmi",3)
# dog2=dog("bantu",7)
# dog1=dog("rocky",6)
        
# class car:
#     y=100  #class variable
#     def __init__(self,model,colour,speed): #model,colour,speed are instance variables 
#         self.m=model
#         self.c=colour
#         self.s=speed
#         x=10    # local variable
#         print(model,colour,speed)
#         print(self.y)
#         print(x)
# car1=car("BMW","red","60kMPH")
# car2=car("defender","black","45kmph")
# car3=car("toyota","blue","56KMPH")


# class flower:
#     def __init__(self,name,colour):
        
        
        
        
        
#create a class of student details with the function of display using the constructor init
#common parameters write in constructor
#different value parameters write in function
#constructor parameters called by class name
#function parameters called by function name
# class student:
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#         print(name,roll)
#     def display(self):
#         print("Name:",self.n)
# s1=student("bhavani",564)
# s1.display()
        
    
# class student:
#     def __init__(self,collegename,collegeaddress):
#         self.n=collegename
#         self.r=collegeaddress
#         print(collegename,collegeaddress)
#     def display(self,stdaddress,stdmobile):
#         print("Name:",self.n)
#         print("add:",stdaddress)
#         print("mobile:",stdmobile)
# s1=student("bhavani",564)
# s1.display("kothapeta",7416088779)

# class student:
#     def __init__(self,collegename,collegeaddress):
#         self.n=collegename
#         self.r=collegeaddress
#         print(collegename,collegeaddress)
#     def display(self,stdaddress,stdmobile):
#         print("Name:",self.n)
#         print("add:",stdaddress)#no need to use self.stdadress here because locally we use
#         print("mobile:",stdmobile)
# s1=student("bhavani",564)
# student.display(s1,"kothapeta",7416088779)

#create a class o all the properties of  the laptop with a specified function display consisting of size and a function colour consisting of colour 
# class laptop:
#     def __init__(self,storage,brand,version):
#         self.s=storage
#         self.b=brand
#         self.v=version
#         #print(storage,brand,version)
#     def display(self,size,colour):
#         print("STORAGE:",self.s)
#         print("brand:",self.b)
#         print("version:",self.v)
#         print("size:",size)
#         print("colour:",colour)
# l=laptop("120GB","dell",3.14)
# l.display("14inch","white")


#create  class for an company variable as  company name tcs and use a display for an employees,class variable name ascompany tcs and ose display function for displaying all the details of the employees common address is hyderabad
# class employees:
#     cname="TCS"
#     def __init__(self,name,salary):
#         self.n=name
#         self.s=salary
#     def display(self,id,mobile):
#         id=id
#         mobile=mobile
#         address="hyd"
#         print("Name:",self.n)
#         print("salary",self.s)
#         print("ID:",id)
#         print("MOBILE:",mobile)
#         print(self.cname)
#         print("ADDRESS:",address)
# s=employees("BHAVANI","10LPA")
# s.display(564,7416088779)

#single inheritance
# class parent:
#     def display(self):
#         print("Iam the parent and i have house")
# class child(parent):
#     def flash(self):
#       print("Iam daughter of satish,i have laptop")
# s=child()
# s.display()
# s.flash()
    
# question1) create a class as person with name and age which include student class with the all the properties of person and id,marks
# class person:
#     def display(self,name,age):
#         self.n=name
#         self.a=age
#         print("NAME:",self.n)
#         print("AGE:",self.a)
# class student(person):
#     def std(self,id,marks):
#         self.id=id
#         self.marks=marks
#         print("ID:",self.id)
#         print("Marks:",self.marks)
# c=student()
# c.display("bhavani",20)
# c.std(564,89)
        
#question1)another method -2
# class person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# class student(person):
#     def __init__(self,marks,id):
#         person.__init__(self,name,age)
#         self.m=marks
#         self.i=id
# name=(input())
# age=int(input())
# marks=int(input())
# id=int(input())
# s=student(marks,id)
# print("name:",name)
# print("age:",age)
# print("marks:",s.m)
# print("id:",s.i)

#multilevel inheritance
# class school:
#     def __init__(self,schoolname,address):
#         self.s=schoolname
#         self.a=address
# class classroom(school):
#     def __init__(self,block,cname):
#         school.__init__(self,schoolname,address)
#         self.b=block
#         self.c=cname
# class student(classroom):
#     def __init__(self,name,age,marks):
#         classroom.__init__(self,block,cname)
#         self.n=name
#         self.age=age
#         self.m=marks
# schoolname=input()
# address=input()
# block=int(input())
# cname=input()
# name=input()
# age=int(input())
# marks=int(input())
# s=student(name,age,marks)
# print("Schoolname",schoolname)
# print("address",address)
# print("block",block)
# print("cname:",cname)
# print("name:",s.n)
# print("age:",s.age)
# print("marks:",s.m)


#multiple inheritance
# class father:
#     def f(self):
#         print("pillar")
# class mother:
#     def m(self):
#         print("supporter")
# class child(father,mother):
#     def b(self):
#         print("me")
# s=child()
# s.f()
# s.m()
# s.b()

#multiple inheritance
# class sports:
#     def __init__(self,sportsname,smarks):
#         self.sn=sportsname
#         self.s=smarks
# class subjects:
#     def __init__(self,subname,credits):
#         self.sub=subname
#         self.cr=credits
# class students(sports,subjects):
#     def __init__(self,studentname,age,classroom):
#         sports.__init__(self,sportsname,smarks)
#         subjects.__init__(self,subname,credits)
#         self.stdn=studentname
#         self.a=age
#         self.classroom=classroom
# sportsname=input()
# smarks=int(input())
# subname=input()
# credits=input()
# studentname=input()
# age=int(input())
# classroom=input()
# s=students(studentname,age,classroom)
# print("sportsname:",sportsname)
# print("smarks:",smarks)
# print("subname:",subname)
# print("credits:",credits)
# print("studentname:",s.stdn)
# print("age:",s.a)
# print("classroom:",s.classroom)

# for more number of students
# class sports:
#     def __init__(self,sportsname,smarks):
#         self.sn=sportsname
#         self.s=smarks
# class subjects:
#     def __init__(self,subname,credits):
#         self.sub=subname
#         self.cr=credits
# class students(sports,subjects):
#     def __init__(self,studentname,age,classroom):
#         sports.__init__(self,sportsname,smarks)
#         subjects.__init__(self,subname,credits)
#         self.stdn=studentname
#         self.a=age
#         self.classroom=classroom
# l=[]
# for i in range(2):
#    sportsname=input()
#    smarks=int(input())
#    subname=input()
#    credits=input()
#    studentname=input()
#    age=int(input())
#    classroom=input()
#    l.append(i)
#    s=students(studentname,age,classroom)
#    print("sportsname:",sportsname)
#    print("smarks:",smarks)
#    print("subname:",subname)
#    print("credits:",credits)
#    print("studentname:",s.stdn)
#    print("age:",s.a)
#    print("classroom:",s.classroom)


#hierarchical inheritance
# class parent:
#     def p(self,money,jewellery):
#         self.m=money
#         self.j=jewellery
#         print(money,jewellery)
# class child1(parent):
#     def c1(self):
#         print("I have a car")
# class child2(parent):
#     def c2(self):
#         print("I have a laptop")
# s=child1()
# s.c1()
# s.p("50000/-","bangles")
# t=child2()
# t.c2()
# t.p("40000/-","earrings")


#hybrid inheritance
# class office:
#     def __init__(self,name,address):
#         self.n=name
#         self.a=address
# class employee(office):
#     def __init__(self,id):
#         self.i=id
# class manager:
#     def __init__(self,projectname):
#         self.p=projectname
#         employee.__init__(self,id)
# class developer:
#     def __init__(self,tool,software):
#         self.t=tool
#         self.s=software
#         employee.__init__(self,id)
# name=input()
# address=input()
# projectname=input()
# tool=input()
# software=input()
# m=manager(projectname)
# d=developer(tool,software)
# print("name:",m.n)
# print("address:",m.a)
# print("projectname",m.p)
# print("tool:",d.t)
# print("software:",d.s)