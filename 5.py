#=============== =============== Math functions
# 10 function
import math

print(math.sqrt(4))      #op= 2.0    (4 square root =2)
print(math.ceil(1.9999)) #op=2       (1 greatest whole number)
print(math.floor(1.224)) #op=1       (1 only 1st value display)

# 5! factorial => 1*2*3*4*5
print(math.factorial(5))   #op=120

print(math.fabs(-5))   #op=5.0 it means negative number change possitive numbers

# power function
print(math.pow(2,3)) #op=8.0

print("-----------------------------------")
# ====================================type of Exception in python
print(dir(locals()['__builtins__'])) # it means error exception
print(len(dir(locals()['__builtins__']))) # op=158 exceptions

#=== mostly used exception
# 1.nameerror Exception

try:
    print(a)
except NameError as e:
    print(e)   # op= name 'a' is not defined (defauld computer writting)

    print("A is not defind") #op= A is not defind (me writting)
'''
try:
    print(10/0)
except ZeroDivisionError:
    print("denominator can't be zero")
'''

#======== value exception error
try:
    print(int("mano"))
except ValueError as e:
    print('pleace enter only numbers')

# op= pleace enter only numbers (because 'int' cannot convert strings)

# =====indexError 
try:
    a=[10,20,30,40]
    print(a[10])
except IndexError as e:
    print("Invalid index")

# op=Invalid index

# ============more exception
try:
    a=[10,20,30,40]
    print(a[0])             #op=10
    print(int("manoj"))     #op=enter only numbers
except IndexError:
    print("index invalid")
except ValueError:
    print("enter only numbers")

# =========================================PYTHON OOPS=====================================

# class attribute

class demo():

    name="manoj"
    age=22

# dot notation 
print(demo.name)  #op=manoj
print(demo.age)   #op=22


# new value set
demo.name="ovin mano"
print(demo.name)
# op=ovin mano (value set)

# new value add
demo.gender="male"
print(demo.gender)
# op=male

print(demo.__dict__) # it means data and functions dictionary formated stored...

# delete attribute
del demo.gender
print(demo.__dict__)
print("----------------------------------------")

# ================instance attribute
class user:

    course="java"

obj=user()

print(obj.__dict__)

print(obj.course)
obj.course="c++"

print(obj.__dict__)
print(obj.course)

obj2=user()
print(obj2.course)

'''
op=
{}
java
{'course': 'c++'}
c++
java

'''
# ===================class methods(without any object,any instance)
class student:
    name="ovin"
    age=22
    def printall():
        print("Name :",student.name)
        print("age:",student.age)

student.printall()
print(student.__dict__)

# =========instance method(self or any attribute using instance)

class student:
    name="ovin"
    age=22
    def printall(self,gender):
        print("Name :",student.name)
        print("age:",student.age)
        print("Gender:",gender)


obj=student()
# student.printall(obj)
obj.printall("male")

# ===============init method (that is constructor) v : 5:20
class user:
    def __init__(self,name):
        print("hai .....")
        self.name=name
    def printall(self):
        print("Name :",self.name)

obj1=user("mano")
obj1.printall()
obj2=user("ovin")
obj2.printall()

'''
hai .....
Name : mano
hai .....
Name : ovin

'''
# =======================property decorator
class user:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        self.msg=self.name+" is " + str(self.age) +" years old"

obj=user("mano",22) 
print(obj.msg)
# op=mano is 22 years old

# ===this age change
obj.age=45
print(obj.msg)
# op=mano is 22 years old (why this output age was changed 45 but 22 is out put ..this prblm solu...property decoration)

class user:
    def __init__(self,name,age) :
        self.name=name
        self.age=age

    def msg(self):
         return self.name+" is " + str(self.age) +" years old"

obj=user("mano",22) 
print(obj.msg())
obj.age=45
print(obj.msg())

'''
op=
mano is 22 years old
mano is 45 years old

'''

# ====but this code 1000 of attribute change the function its two late so easy way
class user:
    def __init__(self,name,age) :
        self.name=name
        self.age=age

    @property

    def msg(self):
         return self.name+" is " + str(self.age) +" years old"

obj=user("mano",22) 
print(obj.msg)
obj.age=45
print(obj.msg)

# same output (using @property and msg function ()-> this remove) 
'''
op=
mano is 22 years old
mano is 45 years old

'''