# x=10
# y=20
# z=30
# if(x>y and x>z):
#     print(f'{x} is greater')
# else:
#     if(z>y and z>x):
#         print(f'{z} is greater')
#     else:
#         print(f'{y} is greater')

a=int(input('enter first number: '))
b=int(input('enter second number: '))
c=int(input('enter third number: '))
if(a>c and a>b):
    print(f'{a} is greater')
elif(a==b and b==c):
    print('a,b and c is greater')
elif(b>c and b>c):
    print(f'{c} is greater')
elif(c>a and c>b):
    print(f'{c} is greater')

elif(a==b):
    print('a and b is greater')
elif(b==c):
    print('b and c is greater')
elif(c==a):
    print('a and c is greater')
