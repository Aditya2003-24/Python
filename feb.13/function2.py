# def show(**n):
#     l=[]
#     for k in n.keys():
#         l.append(k)
    
    
#     return l
# x=eval(input('enter any dict'))
# y=show(**x)
# print(y)
# def show(**n):
#     l=[]
#     for k in n.values():
#         l.append(k)
    
    
#     return l
# x=eval(input('enter any dict'))
# y=show(**x)
# print(y)

def show(**n):
    
    for k,v in n.items():
        print(f'my {k} is {v}')
    return 0
          
x=eval(input('enter any dict'))
y=show(**x)
print(y)

