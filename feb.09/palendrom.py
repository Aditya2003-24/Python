n=eval(input('enter any value: '))
x=str(n)

if(n==x[::-1]):
    print(f'{n} is palendrom')
else:
    print(f'{n} is not palendrom')


# n=eval(input('enter any value: '))
# l=len(n)
# x=''
# for i in range(l-1,-1,-1):
#     x=x+n[i]
# if n==x:

#     print(f'{n} is palendrom')
# else:
#     print(f'{n} is not palendrom')
