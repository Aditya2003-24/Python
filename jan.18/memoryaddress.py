# inter

x=10
y=10
print(id(x))
print(id(y))


# immutable nature

# string
x1='neeraj'
y1='neeraj'
print(id(x1))
print(id(y1))
# tuple
x2=(10,20,30,'neeraj')
y2=(10,20,30,'neeraj')
print(id(x2))
print(id(y2))
print(" ")

# multable nature
print('''
multable nature
list
dicitonary
set
           ''')
# list

l1=[10,20,30,'neeraj']
l2=[10,20,30,'neeraj']

print(id(l1))
print(id(l2))

# dicitionary

d1 = {'name':'aditya','age':22,'city':'bhopal'}
d2 = {'name':'aditya','age':22,'city':'bhopal'}
print(id(d1),id(d2))

# set

s1 = {10,20,'neeraj',30}
s2 = {10,20,'neeraj',30}
print(id(s1),id(s2))
print(" ")
# frozenset

fset1=frozenset({10,20,'neeraj',30})
fset2=frozenset({10,20,'neeraj',30})

print(id(fset1),id(fset2))