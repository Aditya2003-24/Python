# def outer_fun(fun1):
#     def inner_fun():
#         print('Before modification')
#         fun1()
#         print('After modification')
#     return inner_fun
# @outer_fun
# def fun():
#     print('This is from main function')
# fun()


# def outer_fun(fun1):
#     def inner_fun(r,s,t):
#         r=r+5
#         s=s+5
#         t=t+5
        
#         a=fun1(r,s,t)
#         print(a)
#     return inner_fun
# @outer_fun
# def fun(x,y,z):
#     return x+y+z
# x=10
# y=20
# z=30
# fun(x,y,z)


def outer_fun(fun1):
    def inner_fun(r,s,t):
        r=r+5
        s=s+5
        t=t+5
        
        print(fun1(r,s,t))
        
    return inner_fun
@outer_fun
def fun(x,y,z):
    return x+y+z
x=10
y=20
z=30
fun(x,y,z)
