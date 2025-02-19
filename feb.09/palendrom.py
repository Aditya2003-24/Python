n=eval(input('enter any value: '))
x=str(n)

if(x==x[::-1]):
    print(f'{n} is palindrome')
else:
    print(f'{n} is not palindrome')


# n=eval(input('enter any value: '))
# l=len(n)
# x=''
# for i in range(l-1,-1,-1):
#     x=x+n[i]
# if n==x:

#     print(f'{n} is palindrome')
# else:

#     print(f'{n} is not palindrome')
