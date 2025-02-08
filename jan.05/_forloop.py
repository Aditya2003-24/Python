# n=input("enter your string")
# for i in n:
#     x=ord(i)+4
#     y=chr(x)
#     print(y,end=' ')

# n=input("enter your string")
# if n==n[::-1]:
    # print('this is palendrom')


#range(start,stop,darection)

# x=int(input("enter your string"))
# y=range(1,x+1,2)
# print(list(y))

x=input("enter your string")
l=len(x)
y=''
for i in range(l-1,-1,-1):
    y = y + x[i]
if y==x:
    print('it is palendrom')
else:
    print('it is not palendrom')