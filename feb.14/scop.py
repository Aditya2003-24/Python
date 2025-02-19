#scope of variable => there is two types of scops. 
#1. local scop
#2. global scop

# x=10                   #global variable
# def add():
#     y=20                #local variable
#     print(x)
#     print(y)

# add()
# print(x)
# print(y)  Error

# x=10                   #global variable
# def add():
#     global y             # this is use for change the scop
#     y=20                #local variable
#     print(x)
#     print(y)

# add()
# print(x)
# print(y)

# x=10                   #global variable
# def add():
#     global x  
#     print(x)          # this is use for change the scop
#     x=20                #local variable
#     print(x)

# add()
# print(x)

x=10                   #global variable
def add():
    global z,y
    z=40
    x=420
    y=40               #local variable
    print('value of global variable x:',globals()['x'])
    print(x)

add()
print(x)
print(z)

#global is keyword
#globals is a methoed