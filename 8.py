# ====================    FILE    =====================#
# important concept
# =======file read ==== try...catch
try:
    file=open("mano.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Error : File Not Found")
else:
    file.close()
'''
hai iam manoj
kovai
'''

# ===========readline & readlines
try:
    file=open("mano.txt","r")
    print(file.readline())
except FileNotFoundError:
    print("Error : File Not Found")
else:
    file.close()

# op=hai iam manoj (txt file 2line iruku....but line by line ah display pannum)

# readlines
try:
    file=open("mano.txt","r")
    print(file.readlines())
except FileNotFoundError:
    print("Error : File Not Found")
else:
    file.close()

# op=['hai iam manoj\n', 'kovai'] its used data science bulck dataset text formated easy get and analysized in python

#========= loop line by line in python file concept (line by line read)
try:
    file=open("mano.txt","r")
    for line in file:
        print(line)

except FileNotFoundError:
     print("Error : File Not Found")
else:
    file.close()

'''
op=
hai iam manoj
kovai
'''
# ======= write or overwrite a file in python(note)
# ==override file
'''
 try:
    file=open("mano.txt","w")
    file.write("iam learning in python")
    file.close()


    file=open("mano.txt","r")
    for line in file:
        print(line)

except FileNotFoundError:
     print("Error : File Not Found")
else:
    file.close()

'''
#  ==write a file in append modes
'''
try:
    file=open("mano.txt","a")

    file.write("iam learning in education")
    file.close()
    
    file=open("mano.txt","r")
    for line in file:
        print(line)

except FileNotFoundError:
     print("Error : File Not Found")
else:
    file.close()
'''


# ==delete file concept
import os

if os.path.exists("test.txt"):
    os.remove("test.txt")  #file delete
    
    # os.rmdir("folder name") --this is folder delete code
else:
    print("File not Fount")

"""
# virus draw

from turtle import*
speed(50)
color("red")
bgcolor("white")
b=200
while b>0:
    left(b)
    forward(b*3)
    b=b-1
    
"""
