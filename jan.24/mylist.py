my_list=[10,10.5,'neeraj']
print(my_list)
print(type(my_list))
print(id(my_list))


list1=[10,20,30,40,50]
print(sum(list1))
print(id(list1))
print(type(list1))
print(min(list1))
print(max(list1))
print(len(list1))

# list.

# methods

# This is append method => in append method we add one object in list.
l1=[10,'aman',12,24,55]
l1.append('zaki')
print(l1)

l2=[10,'aman',12,24,55]
l2.extend(l1)
print(l2)


# insert method use for add object with help of indexing in anywhere.
l2.insert(0,'aman')
print(l2)