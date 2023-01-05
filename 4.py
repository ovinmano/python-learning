#====== ============================function

# python function create using     "def"    keyword

def welcome():
    print("welcome to manoj")

welcome()
welcome()
welcome()

'''
op=
welcome to manoj
welcome to manoj
welcome to manoj

'''
#============== there are 9types of function
# 1.) No Return Type Without Argument Function
def add():
    a=(int(input("enter the A of value:")))
    b=(int(input("enter the B of value:")))
    c=a+b
    print("total:",c)
add()

# ===return type with argument
def sub(a,b):
    c=a-b
    return c
x=sub(12,5)   
print("sub",x)

# 2.)===Arbitary argument function(*)

def class_10(*student):
    print(student)
class_10("ovin","mano","kumar","raja")
# op=('ovin', 'mano', 'kumar', 'raja')

# ==keyword args function
def message(name,age):
    print(name,"age is ",age)
message(age=22,name="mano")
# op=mano age is  22

# 3.)====== Arbitary Keyword args function
def bioData(**data):
    print(data)
bioData(name="manoj", age=22, gender="male")

# op={'name': 'manoj', 'age': 22, 'gender': 'male'}

# 4.)======Default parameter function
def user(name,city="kovai"):
    print(name,"is from",city)
user("mano","chennai")
user("ram")
# opo=mano is from chennai
# op=mano is from chennai(default parameter.....default city name)

# passing list as an args function
def total(marks):
    return sum(marks)
print(total([33,44,65,77]))

# op=219

# 5.)==recursive function (this function work finish autometically called recursion)
# 1* 2* 3* 4* 5
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1)) #x-1 it means next number
print("factorial :",factorial(5))

# op=factorial : 120
'''
factorial (5)
5* factorial (4)
5*4 factorial (3)
5*4*3 factorial (2)
5*4*3*2 factorial (1)
5*4*3*2*1

'''
# ==================================Date and time 
import datetime as dt

current_date=dt.date.today()
print(current_date)

# op=2022-12-02

new=dt.date(2001,11,20)
print(new)

# op=2001-11-20
print("YEAR :",new.year)
print("MONTH :",new.month)
print("DAY :",new.day)
'''
op=
YEAR : 2001
MONTH : 11
DAY : 20
'''
print("--------------------------------")

a=dt.time(11,45,5)
print(a)
print("HOUR :",a.hour)
print("MINUTE :",a.minute)
print("SECOND :",a.second)

'''
op=
HOUR : 11
MINUTE : 45
SECOND : 5
'''
print("--------------------------------")
# =========current time
current_time=dt.datetime.now()
print("current time :",current_time)

# op=current time : 2022-12-03 11:20:10.500697

print("--------------------------------")

current = dt .datetime .now()
new_year = dt.datetime(2023,1,1)
difference=new_year-current
print(difference)
# op=28 days, 12:30:28.662568

print("--------------------------------")
# different style
current = dt .datetime .now()
style=current.strftime("%A %B %d %m %Y")
print(style)
# op=Saturday December 03 12 2022

















