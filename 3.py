# ========================union

a={1,2,3,4}
b={"a","b","c","d"}
c=a.union(b)
print(c)
# ==update
a.update(b)
print(a)


#========= =====================inbuild methods
# 1.)  intersection
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)

# op={5} intersection means a ,b common value display
a.intersection_update(b)
print(a)
# op={5} not using c variables.... a,b analize and stored a variables

# 2.)  symentic_difference
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.symmetric_difference(b)
print(c)
# op={1, 2, 3, 4, 6, 7, 8, 9}

a.symmetric_difference_update(b)
print(a)
# op={1, 2, 3, 4, 6, 7, 8, 9}   not using c variables.... a,b analize and stored a variables

# ======================Dictionary (key valus pair)
user = {
    "name":"manoj",
    "age":21,
    "isAlive":True
}
print(user)
print(type(user))
# elements access
print(user["name"]) 
print(user.keys()) #only keys display
print(user.items()) #keys and values display
'''
op={'name': 'manoj', 'age': 21, 'isAlive': True}

<class 'dict'>

manoj

dict_keys(['name', 'age', 'isAlive'])

dict_items([('name', 'manoj'), ('age', 21), ('isAlive', True)])

'''
#==== for loop dict
for z in user:
    print(z,"",user[z])

'''
name  manoj
age  21
isAlive  True

'''
for y,z in user.items():
    print(y,z)

# op= same output

# ====update values

user.update({"gender":"male"})
print(user)

# op={'name': 'manoj', 'age': 21, 'isAlive': True, 'gender': 'male'}

#==== changin values
user["age"]=32
print(user)  
# op={'name': 'manoj', 'age': 32, 'isAlive': True, 'gender': 'male'}

# ===pop (particular index remove)
user.pop("age")
print(user)

# op={'name': 'manoj', 'isAlive': True, 'gender': 'male'}

# ==nested dictionary
users = {
    "user1 ": {
        "name":"manoj",
        "age":21,
        "isAlive":True
    },
    "user2 ": {
        "name":"kumar",
        "age":32,
        "isAlive":True
    }
}
print(users)
# op={'user1 ': {'name': 'manoj', 'age': 21, 'isAlive': True}, 'user2 ': {'name': 'kumar', 'age': 32, 'isAlive': True}}