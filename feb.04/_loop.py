# n=int(input("enter no. :"))
# i=1

# while (i<=n):
#     if(i<n):
#         print(i,end=' ')
#     else:
#         print(i)

#     i+=1
# print('hello')


#armstrong number.
n=int(input("enter no. :"))
digit=0
x=n
y=n
while n>0:
    digit=digit+1
    n//=10
# print(digit)
# print(n)
sum=0
while x>0:
    last_difit=x%10
    sum=sum+last_difit**digit
    x//=10
if y==sum:
    print(f'this is armstrong no.{y}')
else:
    print(f'this is not armstron no.{y}') 




