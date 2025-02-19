# n=eval(input('enter the no.: '))
# sum=0
# x=n
# while n>0:
#     last_digit=n%10
#     sum = sum+last_digit
#     n=n//10
# print(sum)
# print(n)
# if x%sum==0:
#     print(f'this is harshat no. {x}')
# else:
#     (f'this is not harshat no. {x}')


#sorting



# def are_anagrams(word1, word2):
#     # print(sorted(word1),sorted(word2))
#     return sorted(word1) == sorted(word2)


# n=eval(input('enter any thing'))
# x=eval(input('enter any thing'))


# if sorted(n) == sorted(x):
#     print('it is anogram')
# else:
#     print('this is not anogram')


# # Example Usage
# # print(are_anagrams(n,x))  # Output: True
# # print(are_anagrams("hello", "world"))    # Output: False


# n=eval(input('enter any no.'))
# y=n
# x=n*n
# sum=0

# while x>0:
#     last=x%10
#     sum=sum+last
#     x=x//10
# if(sum==n):
#     print('true')
# else:
#     print('false')

# n=eval(input('enter any number: '))
# x=n
# sum=0
# total=0	
# while n>0:
# 	last=n%10
# 	y=last
# 	t=last
# 	while y-1>0:
# 	    z=t*(y-1)
# 	    t=z
# 	    total=z
# 	    y=y-1
# 	if(last==1):
# 	    total=last
# 	sum=sum+total
# 	n=n//10
# if(x==sum):
# 	print('true')
# else:
# 	print('false')


# n=eval(input('enter any no.'))
# y=n
# sum=0
# product=0

# while n>0:
#     last=n%10
#     sum=sum+last
#     product=product*last
#     n=n//10
# if(sum==product):
#     print('true')
# else:
#     print('false')

# n=eval(input('enter any no.'))

# x=n+1
# square=int(x**0.5)
# print(square)
# square=square*square
# print(square)
# if(square==x):
#     print(f'{x} is sunny number')
# else:
#     print(f'{x} is not sunny number')


# n=eval(input('enter any no.'))
# x=n
# sum=0
# while(n>0):
#     last_digit=n%10
#     digit=last_digit*last_digit*last_digit
#     sum=digit+sum
#     n=n//10
# if (sum==x):
#     print(f'{sum} yes')
# else:
#     print(f'{sum} no')


# n=eval(input('enter any no.'))
# x=n
# sum=0
# while(n>0):
#     last_digit=n%10
#     sum=(sum*10)+last_digit
#     n=n//10
# if (sum==x):
#     print(f'{sum} yes')
# else:
#     print(f'{sum} no')


#fibonacci

n=eval(input('enter any no.'))
a=0
b=1
tmp=0
while n>0:
    tmp=a+b
    a=b
    b=tmp
    
    print(a,end=',')
    n=n-1
