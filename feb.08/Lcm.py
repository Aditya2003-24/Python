x=eval(input('enter first no.: '))
y=eval(input('enter second no.: '))

max_no=max(x,y)
while True:
    if (max_no%x==0 and max_no%y==0):
        break
    max_no=max_no+1
print(f'LCM of {x} and {y} is {max_no}')