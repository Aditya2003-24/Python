# str1='python'
# print(str1.index('p'))
# print(str1.index('o'))
# # print(str1.index('O'))   error
# # print(str1.index('p',1))
# print(str1.index('p',0,1))
# print(str1.index('python'))
# print(str1[0])
# print(str1[-1])
list1 = ['aditya',10,20,30,40,50.5,10]
print(list1.index(10))
print(list1.index(10,1))
print(list1.index(10,2))
print(list1.index(10,2,7))

tuple1 = ('aditya',10,20,30,40,50.5,10)
print(tuple1.index(10,1,4))      #we check the 10 in tuple 10 is there or not.