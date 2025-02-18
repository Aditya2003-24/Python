# def squar(x):
#     return x**2
# l1=eval(input('enter any numeric collection: '))

# res=map(squar,l1)
# print(res)
# print(list(res))

# def even():
#     if(x%2==0):
#         print(2+x)
#     else:
#         print()

# def add(x,y,z):
#     return x+y+z
# l1=eval(input('enter any numeric collection: '))
# l2=eval(input('enter any numeric collection: '))
# l3=eval(input('enter any numeric collection: '))

# res=map(add,l1,l2,l3)
# print(list(res))


def power(x,y):
    return x**y
l1=eval(input('enter no. '))
l2=eval(input('enter no. '))
res=map(power,l1,l2)
print(list(res))
