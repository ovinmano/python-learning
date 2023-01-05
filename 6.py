# ====================property decorator getter setter
class student:
    def __init__(self,total):
        self.total=total
    def average(self):
        return self.total/5.0

obj=student(450)
print("Total :",obj.total)
print("Average :",obj.average())

'''
Total : 450
Average : 90.0

'''
# data encopsulation....(python no private and public data....but nameing conversion using private and public using data)
class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        self._total=t

obj=student(450)
print("Total :",obj.total)
print("Average :",obj.average())
obj.total=250
print("Total :",obj.total)
print("Average :",obj.average())

'''
Total : 450
Average : 90.0
Total : 250
Average : 50.0

'''
print("-----------------------------------------------------------")
#(another way) =====property method 

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0

    def getter(self):
        return self._total

    def setter(self,t):
        self._total=t
    total=property(getter,setter)
        

obj=student(350)
print("Total :",obj.total)
print("Average :",obj.average())
obj.total=150
print("Total :",obj.total)
print("Average :",obj.average())

'''
Total : 350
Average : 70.0
Total : 150
Average : 30.0

'''
# ==========class method decorator
# student attendance

class student:

    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count +=1

    def printDetails(self):
        print("Name :",self.name,"Age :",self.age)

    @classmethod
    def total(cls):
        return cls.count


obj=student("kumar",22)
obj.printDetails()

obj=student("ram",52)
obj.printDetails()

print("Total students :",obj.total())
print("Total students :",student.total())

'''
Name : kumar Age : 22
Name : ram Age : 52
Total students : 2
Total students : 2

'''
# =======================static method in python

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetails(self):
        print("Name :",self.name,"Age :",self.age)
    
    @staticmethod
    def welcome():
        print("welcome to my code")
        # this message all users and commonly display (welcome to my code) so its static method
    
s1=student("rocky",34)
s1.printDetails()
s1.welcome()
print("-------------------------------------------------------------")
# ===================  Data Abstraction & Data encapsulation (v 5:45)
'''
data abstraction:
    it refers to providing only essential information to the outside world and hiding their background details.
    (ex: TV)
data encapsilation:
    is a process of wrapping code and data together into a single unit. class=> variables,and then methods, functions
    (ex: tablets capsuel ,because different kemicals in one capsuel) 
'''
class library:

    def __init__(self,books):
        self.books=books

    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)

    def borrow_books(self,borrow_books):
        if borrow_books in self.books:
            print("get a book now")
            self.books.remove(borrow_books)
        else:
            print("books not available")

    def recieve_books(self,recieve_books):
        print("you have return the book")
        self.books.append(recieve_books)

books = ['c','c++','java']
obj = library(books)

msg='''
    1.)Display books
    2.)Borrow books
    3.)Return books
'''         
while True:
    print(msg)
    ch=int(input("Enter Your choice :"))
    if ch==1:
        obj.list_books()
    elif ch==2:
        book =input("Enter the book Name to borrow :")
        obj.borrow_books(book)
    elif ch==3:
        book =input("Enter the book Name to return :")
        obj.recieve_books(book)
    else:
        print("thank you come again")
        quit()
