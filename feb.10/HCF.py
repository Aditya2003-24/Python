x=eval(input('enter the no.: '))
y=eval(input('enter the no.: '))
i=1
min=min(x,y)

while i<min:
    if(x%i==0 and y%i==0):
        hcf=i
    i=i+1
print(f'{hcf} is HCF')