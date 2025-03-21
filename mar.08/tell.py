# f=open('c1.txt','a')
# print(f.tell())
# f.write('hello')
# print(f.tell())


f=open('c1.txt','rb')
data=f.read()
print(data)
print(f.tell())
# data=f.read()
# print(data)   khali dega
print(f.seek(-10,2))
print(f.read())


