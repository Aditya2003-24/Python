# add=lambda x,y : (x+y)
# p=eval(input('enter no. '))
# q=eval(input('enter no. '))

# print(add(p,q))


# n=eval(input('enter any no. '))
# check_number = lambda x:'even no' if x%2==0 else 'odd no'
# print(check_number(n))

# n=eval(input('enter any no. '))
# check_number = lambda x:'positive no' if x>0 else 'nagative no'
# print(check_number(n))

# n=eval(input('enter any no. '))
# check_number = lambda x:[i for i in range(1,x)]
# print(check_number(n))

x=lambda p,q : [[r for r in range(p)] for i in range(q)]
p=int(input('ente how many collection required'))
q=int(input('ente how many repetation required'))
print(x(p,q))