d1={'name':'aditya','age':22,'quali':'mca'}
print(max(d1))
print(min(d1))
print(len(d1))
print(type(d1))
print(id(d1))

#methods
print(id('name'))
d1.clear()
print(d1)
print(id(d1))


d2={'name':'aditya','age':22,'quali':'mca'}
d2.copy()
d4=d2.copy()
print(d4,d2)

#get value 


print(d2.get('name'))

#items,keys,values.
print(d2.keys())
print(d2.values())
print(d2.items())

#popitem,pop.

print(d2.popitem())   # ye last bale ko hata deta hai
print(d2.pop('name'))   #ye jis key ka nam denge usko hata dega.

print(d2)

#setdefault.

print(d2.setdefault('name','adi'))
print(d2)

#update
d1={'new':'guest'}
d1.update(d2)

print(d1)