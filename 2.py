# ==============break statement
i=1
while i<=20:
    if(i==7):
        break
    print(i)
    i+=1
#=============== ============range in python
'''
1-5 => 1,2,3,4,5
0-5 =>2,4(even number)

'''
# list it's called constructor

a=list(range(5))
print(a)
# op=[0, 1, 2, 3, 4]

print(list(range(2,5))) # (last value (n-1) 5-1= 4...so 2 to 4 value printing)
# op=[2, 3, 4]

print(list(range(0,21,2))) # (0 to 20 even number.... 2 number increase)
# op=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(list(range(1,21,2))) #(0 to 20 Odd number...)
# op=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


#========= ========== For loop Using range in python(Even & Odd number)
for i in range(0,21,2):
    print(i)

for i in range(1,21,2):
    print(i)

# ===================nested for loop
for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
print("-------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

# task
'''
ABCDE
ABCDE
ABCDE
ABCDE

A-Z = 65-90
a-b = 97-122

'''
for i in range (65,70,1):
    print(chr(i))

'''op=
A
B
C
D
E
'''

for i in range (65,70,1):
    for j in range (65,70,1):
        print(chr(j),end="")
    print("")

# op=ABCDE
# =====================List in python
'''
Sequence type -> (its stored sequence value [1,2,3,4])
Mutable -> (Easy to change the value)

'''

# Sequence
a=[11,22,33,44]
print(a)
# mutable 0th position value change 100
a[0]=100
print(a)


# ====clear and copy in python
a=[1,2,3,4,5]
print(a)
a.clear()
print(a)

'''
op=[1, 2, 3, 4, 5]

[]

'''
# ========copy
a=[10,20,30,40,50]
print(a)
b=a.copy()
print(b)

'''
op =[10, 20, 30, 40, 50]

    [10, 20, 30, 40, 50]

'''
# =========count

a=[10,25,55,67,25,44,31,25]
print(a.count(25))

# op=3 (25 value 3times so count 3)

# ======index
a=[22,83,73,45,89,92,32]
print(a.index(83))

# op=1

# ========length ,max,and min value
a=[22,83,73,45,89,92,32]
print(len(a))
print(max(a))
print(min(a))

# op=7 (total values 7)
# op=92 (maximum values 92)
# op=22 (minimum values 22)

# =====Remove
a=[22,83,73,45,89,92,32] #Remove elements using index
a.pop(0)
print(a)
#  op=[83, 73, 45, 89, 92, 32]


a=[10,25,55,67,25,44,31,25] # Remove elements using Values 
a.remove(25)
print(a)
# op=[10, 55, 67, 25, 44, 31, 25]

# =====assending order
a=[10,66,87,22,12,45]
a.sort()
print(a)
# op=[10, 12, 22, 45, 66, 87]

# decending order

a.sort(reverse=True)
print(a)
# op=[87, 66, 45, 22, 12, 10]

# =======================tuple in python
"""
1.) Immutable -> (once assign the value dont chnge the value )
2.) surrounded by Round Brackes () -> (its using rounds bracket )

"""

a=(1,2.5,True,'Ram')
print(a)
print(type(a))

'''
op=(1, 2.5, True, 'Ram')
<class 'tuple'>

'''
#========== ==============nested tubles
a=(1,2,3,4)
b=(5,6,7,8)
c=(a,b)
print(c)
print(c[0])
print(c[0][1])
'''
op=
<class 'tuple'>
((1, 2, 3, 4), (5, 6, 7, 8))

(1, 2, 3, 4)

2

'''
# dummy data print 10times(tuble value single must use comma(,))
x=('mano',)*10
print(x)
# op=('mano', 'mano', 'mano', 'mano', 'mano', 'mano', 'mano', 'mano', 'mano', 'mano')

# ==============python set data type(un order ....unindexed data type) set using {}this bracket
names={"manoj","ovin","vijay","ajith","kumar"} 
print(names)

# accessing value using For loop
for name in names:
    print(name)

# Adding new element
names.add("dhanus")
print(names)

# update another set of data

a={"vikram","mathavan","rajini"}
names.update(a)
print(names)

names.remove("rajini")
print(names)

names.discard("vikram")
print(names) #it means some value discard no error

names.clear()
print(names)
# op=set()    empty set

del names
print(names)
# op= error msg name is not defind total value delete

