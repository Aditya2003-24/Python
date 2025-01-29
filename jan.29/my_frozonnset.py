s='aditya'
s=frozenset(s)
print(type(s))

# we use frozenset in ever data type like int,list,tuple,dict and set also  
# we use frozenset for frize the data.

print(s)
a={2,3,4,5,6,9}
b={1,2,3,4,5,6,7,8}


x=frozenset(a)
print(x.union(b))
print(x.intersection(b))
print(x.difference(b))
print(x.symmetric_difference(b))
print(x.isdisjoint(b))  #ye dono comman nahi hai

c={1,3,5}
v={2,4,6}
print(c.isdisjoint(v)) # we can check the element agar dono me comman huye to false nahi huye to true

h={1,2,3}
g={1,2,3,4,5,6,7}
print(h.issubset(g))  # ye dono elemnet check karte hai agar comman hai to subset hai or superset hai.
print(g.issuperset(h))

l1=[10,20,2,4,6,8,10,20,30]
print(l1[:][::-1][1:7][::-1])