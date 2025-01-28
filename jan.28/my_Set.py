my_set={'aditya',10,20,'aman',40}
print(my_set)
print(type(my_set))



s1={'neeraj','raj','rahul'}
s2={10,20,30,40,50}

print(max(s1),max(s2))
print(min(s1),min(s2))
print(type(s1),type(s2))
print(sum(s2))
s1.clear()
print(s1)
s2.add(90)
print(s2)
s2.update(my_set)
print(s2)

s2.pop()
print(s2)
s2.remove(90)
print(s2)

s2.discard(90)#this is better  then remove so use this not remove.
print(90)
# s2.update(1,2,3,4,5)
# print(s2)  nhi chala

s4={1,2,3,4,5,6}
s5={1,2,7,8,9}
print(s4.union(s5)) #unic hold karega. 
print( s4.intersection(s5)) # jo bhi comman hai bo output me ayega. 
# s4.intersection(s5)
# print(s4)

print(s4.difference(s5))  # s4-s5  jo comman hoga bo hi mainas hoga or ye sirf s4 ko print karega.


print(s4.symmetric_difference(s5))  # ye new set dega or ye s4 or s5 ko print kardega or jo comman hai usko hata dega.

s4.difference_update(s5) # ye sirf s4 ko print karega or jo s5 me comman hai usko hata dega.
print(s4)