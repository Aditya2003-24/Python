def outer_fun(fun1):
    def inner_fun():
        print('Before modification')
        fun1()
        print('After modification')
    return inner_fun
def fun():
    print('This is from main function')
res=outer_fun(fun)
res()