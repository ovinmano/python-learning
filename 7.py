# ===========================   Inheritance(one class property access another class acessed inheritance)
# single inheritance
class samsung: #==base class
    company="samsung"
    website="www.samsung-india.com"

    def contact(self):
        print("Address : coimbatore ,Gandthipuram")
class samsunga11(samsung): #==derived class

    def __init__(self):
        self.name="samsunga11"
        self.year=2001
    def product_details(self):
        print("Name :",self.name)
        print("year :",self.year)
        print("company :",self.company)
        print("website :",self.website)
mobile=samsunga11()
mobile.product_details()
mobile.contact()

# ==multiple inheritance
class father:           #base class
   def fishing(self):
    print("fishing in rivers")

   def chess(self):
    print("playing chess from father")

class mother:           #base class
   def cooking(self):
    print("cooking in housewife")
    
   def chess(self):
    print("playing chess from mother")

class son(father,mother):   #derived class
    def ride(self):
        print("riding bicycle")

obj=son()
obj.ride()   #riding bicycle
obj.chess()  #playing chess from father....class son parameter la 1st mother nu potta (playing chess from mother)

# === Multi level inheritance
class GrandFather:
    def ownHouse(self):
        print("Grandfather house")

class father(GrandFather):
    def ownBike(self):
        print("father's bike")

class son(father):
    def book(self):
        print("son have a bike")

obj=son()
obj.ownHouse()  #Grandfather house
obj.ownBike()   #father's bike
obj.book()      #son have a bike

# ===============Function overriding
class Employee:

    def workingHours(self):
        self.hrs=50

    def totalhours(self):
        print("Total working working hours :",self.hrs)

class trainee(Employee): 

    def workingHours(self):
        self.hrs=60

    def restHours(self):
        super().workingHours()

obj=Employee()
obj.workingHours()
obj.totalhours()

obj=trainee()
obj.workingHours()
obj.totalhours()
# reset hours
obj.restHours()
obj.totalhours()

'''
Total working working hours : 50
Total working working hours : 60
Total working working hours : 50

'''
# ========diamond prblm inheritance
class A:
    def disply(self):
        print("I am the display of class A")
class B(A):
    def disply(self):
        print("I am the display of class b")
class C(A):
    def disply(self):
        print("I am the display of class c")
class D(B,C):
    pass
    # def disply(self):
    #     print("I am the display of class D")
obj=D()
obj.disply()

# =============== Operator overloading(polymorphism)
a=10
b=20
print(a+b)
# op=30

a="manoj"
b="kumar"
print(a+b)
# op=manojkumar 
# (it means + this symbal acting 2 operation...int number add & string value concat....so op overloading)

class addition:
    def __init__(self,a):
        self.a=a
    # magic method addition
    def __add__(z1,z2):
        return z1.a + z2.a
    # magic method subtraction
    def __sub__(z1,z2):
        return z1.a - z2.a


obj1 = addition(20)
obj2 =addition(10)

print("Total :",obj1 + obj2)
print("difference :",obj1 - obj2)
# op=Total : 30

# ================abstract method & abstract base class
from abc import ABC, abstractmethod

class bank (ABC):

    @abstractmethod
    def loan(self): pass

    @abstractmethod
    def credit(self): pass

    @abstractmethod
    def debit(self): pass

class HDFC(bank):

    def loan(self):
        print("7.5% Intrest loal")

    def credit(self):
        print("HDFC provide credit")

    def debit(self):
        print("HDFC provide debit")
    #additional function
    def card(self):
        print("HDFC provide cards") 

obj=HDFC()
obj.loan()
obj.credit()
obj.debit()
obj.card()

'''
7.5% Intrest loal
HDFC provide credit
HDFC provide debit
HDFC provide cards

'''