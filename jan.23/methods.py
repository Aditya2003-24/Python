str1='I love python'
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())

print(str1.find('z'))              #it's show -1
# print(str1.index('z'))    it's show error

print(str1.split('o',1))  
print(str1.split())  
# print(str1.join())  

l1=['neeraj','kunal','kartik']
print(','.join(l1))
print(type(','.join(l1)))
print(str1.count('o'))           #str me one word se count kar sakte hai
print(l1.count('kunal'))     #list me object hota hai object se count karta hai