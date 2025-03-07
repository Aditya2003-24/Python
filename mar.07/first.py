
# open

# f=open('n1.txt','x')   we use x for create file
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n1.txt','w')     we use w for write somthing but thers is no need to use this mode/ it's also creat file
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n1.txt','a')    we use a for write somthing and it's alos create file and we use this ealy
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n1.txt','r')       for reed file
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())


#write => insert data

# f=open('n5.txt','w')
# data='this is python'
# f.write(data)
# f.close()



f=open('n5.txt','a')
data=['\nthis "is" python\n','learn python\n']
f.writelines(data)
f.close()
print(f.closed)


