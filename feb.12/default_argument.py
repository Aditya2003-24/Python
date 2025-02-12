# default argument=>


# def fun_name(x=0,y=0,z=0):
#     p=x+y+z
#     print('hi')
#     # return p
# print(fun_name(1,2,3))



# def fun_name(x=0,y=0,z=0):
#     p=x+y+z
#     print('hi')
#     return p

# t=fun_name()
# print(t)

# def fun_name(x=0,y=0,z=0):
#     print('x=',x)
#     print('y=',y)
#     print('z=',z)
#     p=x+y+z
#     print('hi')
#     return p

# t=fun_name(5)
# print(t)

# def fun_name(x=0,y=0,z=0):
#     print('x=',x)
#     print('y=',y)
#     print('z=',z)
#     p=x+y+z
#     print('hi')
#     return p

# t=fun_name(5,2,4)
# print(t)



# variable-length argument(*single star or (args))

def add(*n):    #(for taking all value so we use (*n)
    print(n)
    print(type(n))
    sum=0
    for i in n:
        for x in i:
          sum=sum+x
    return sum
y=eval(input('enter you no.: '))
x=add(y)
print(x)