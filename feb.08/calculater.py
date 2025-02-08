# while True:
#     print(' 1. add\n 2. sub \n 3. multi \n 4. div \n 5. off')
#     n=eval(input('enter a no.: '))
#     if n==1:
#         x=eval(input('enter a no.: '))
#         y=eval(input('enter a no.: '))
#         z=x+y
#         print(f'Addition of {x} and {y} is {z}')
#     elif n==2:
#         x=eval(input('enter a no.: '))
#         y=eval(input('enter a no.: '))
#         z=x-y
#         print(f'subtraction of {x} and {y} is {z}')
#     elif n==3:
#         x=eval(input('enter a no.: '))
#         y=eval(input('enter a no.: '))
#         z=x*y
#         print(f'multiplay of {x} and {y} is {z}')
#     elif n==4:
#         x=eval(input('enter a no.: '))
#         y=eval(input('enter a no.: '))
#         z=x/y
#         print(f'divide of {x} and {y} is {z}')
#     elif n==5:
#         break
#     else:
#         print('please enter valid option')


while True:
    print(' 1. add\n 2. sub \n 3. multi \n 4. div \n 5. off')
    n=eval(input('enter a no.: '))
    p=(1,2,3,4)
    if(n in p):
         x=eval(input('enter first no.: '))
         y=eval(input('enter second no.: '))
         if n==1:   
           z=x+y
           print(f'addition of {x} and {y} is {z}')
         if n==2:   
           z=x-y
           print(f'subtraction of {x} and {y} is {z}')
         if n==3:   
           z=x*y
           print(f'multiplay of {x} and {y} is {z}')
         if n==4:   
           z=x/y
           print(f'divide of {x} and {y} is {z}')
    elif n==5:   
        break
    else:
       print('please enter valid option')

         

