# def even(x):
#     if x%2==0:
#         return x
# l1=eval(input('enter any value'))
# res=filter(even,l1)
# print(res)
# print(tuple(res))

# def even(x):
#     if x%2==0:
#         return 'even'
#     else:
#         return 'odd'
# l1=eval(input('enter any value'))
# res=map(even,l1)
# print(res)
# print(tuple(res))
# def even(x):
#    print(len(x))
#    if len(x)<=3:
      
#       return x
# l1=eval(input('enter any value'))
# res=filter(even,l1)
# print(res)
# print(tuple(res))

#reduce=>


import functools
def my_max(x,y):
   if x>y:
      return x
   else:
      return y
      
l1=eval(input('enter any value'))
res=functools.reduce(my_max,l1)
print(res)