# def add(*n):
#     # print(n)
#     # print(type(n))
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum

# x=eval(input('ente any type'))
# result=add(*x)
# print(result)



def show_my_datail(**n):
    # print(n)
    # print(type(n))
    for k,v in n.items():
        print(f'my {k} is {v}')
    
x=eval(input('enter dict: '))

# show_my_datail()
y=show_my_datail(**x)
print(y)
# show_my_datail(name='aditya',age=22)
