"""print("manoj")
print (25+25)
import keyword
print(keyword.kwlist)"""

'''name=input("Enter the name :")
print(type(name))
print(name)'''

# addition of 2 num
'''a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=a+b
print(c)
print(type(c))'''

# name split method

'''name1,name2,name3=input("enter the name:").split(',')
print("Name 1:",name1)
print("Name 2:",name2)
print("Name 3:",name3)'''

""""
para=["22","33","44"]
print(",".join(para))

"""
# multiline user input infinite type(enter double click and show result)
'''
para=[]
print("Enter the para:")
while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
output="\n".join(para)
print(output)

'''
# string and string function
t="ovin mano"
print(t) #op=ovin mano
print(t.upper()) #OVIN MANO(all capital letter)
print(t.title()) #Ovin Mano(paragraph 1st letter capital)
print(t.endswith("no")) #True (the name mano ending "no" so true )
print(t.capitalize()) #Ovin mano(only 1st letter capital)
print(t.count('o')) #2 (two o  letter)
print(t.find('n')) #3 (index position)
print(t.find('n',4)) #7 (second index position)
print(t.replace("mano","kumar")) #ovin kumar (replace the letter)

a="MANO"
print("Is Upper: ",a.isupper()) #Is Upper:  True
print("Is Upper: ",a.islower()) #Is Upper:  False

#===============================split

tee="he \nis \ngood"
print(tee)
"""
op= 
he
is
good
"""
print(tee.splitlines()) #['he ', 'is ', 'good']
print(tee.splitlines(True)) #['he \n', 'is \n', 'good']

w="   mano    "
print(len(w.strip())) #4 (unwanted space remove)
print(len(w.lstrip())) #8 (left side unwanted space only remove)
print(len(w.rstrip())) #7 (right side unwanted space only remove)

#=======================string manipulation
s="sample"
print(s)
print(s[0:2]) #op= sa (2 letter only print)
print(s[:5]) #op= sampl (5th position letter ignored)
print(s[1:]) #op= ample (1st letter was ignore)
print(s[::-1]) #op= elpmas (reverse printing)

#====================Arithmetic operator
'''

+ addition 
- subtraction 
* multiplication
/ division 
% madulus
** Exponentiation
// floor division

'''
a=123
b=10
print(a+b) #133
print(a-b) #113
print(a*b) #1230
print(a/b) #12.3
print(a//b) #12 (// it means floor 12.3 (.3)-ignore)
print(a%b) #3 (// it means reminder 12.3 (12)-ignore)
print(2**3) #8 (// it means 2power3 =8 double star means power)

# bitwise operator

'''

&   AND
|   OR
^   NOT
~   XOR
<<  ZERO FILL LEFT SHIFT
>>  SIGNED RIGHT SHIT

'''
# ============bitwise and

a=10
b=11
print(a&b) #op=10

#==================== if statement
# 
n=int(input("Enter the Even numer :"))

if n % 2 == 0 :
    print(n,"Is even number")
else :
    print(n,"Is Odd number")

# ================ if else statement
# write a program to check vote eligiblity by enter his/her name and age

name=input("Enter the name :")
age=int(input("Enter the age :"))

if age >= 18 :
    print(name,"age is",age,"eligible for vote")
else :
    print(name,"age is",age,"Not eligible for vote")

#============================== elif statement
'''
one member go to library book return late fine 

0       No fine 
1-5     0.5
5-10    1
10-30   5
>30     membership cancel

'''
days=int(input("Enter the days :"))

if (days==0) :
    print("No fine")
elif (days>=1 and days<=5):
    print("Your fine 0.5") 

elif (days>5 and days<=10):
    print("Your fine 1") 

elif (days>10 and days<=30):
    print("Your fine 5") 
else :
    print("Membership cancel")

#======================== nested if statement
"""
3 marks as input
total
average
result
if pass grade
90-100  A
80-89   B
70-79   c
else    D

"""
m1 =int(input("Enter the Mark-1:"))

m2 =int(input("Enter the Mark-2:"))

m3 =int(input("Enter the Mark-3:"))

total=m1+m2+m3
average=total/3.0
print("Total :",total)
print("Average :",average)
if (m1>=35 and m2>=35 and m3>=35) :
    print("Result : Pass")
    if(average>=90 and average<=100):
        print("Grade : A")
    if(average>=80 and average<=89):
        print("Grade : B")
    if(average>=70 and average<=79):
        print("Grade : C")
else :
    print("Result : fail")
    print("Grade : No Grade ")

# ========================While loop
'''
1. While loop
2. For loop

'''
i=1
while i<=10:
    print(i)
    i+=1
print("-----------------")

#================== Odd number

i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue;
    print(i)
    i +=2
