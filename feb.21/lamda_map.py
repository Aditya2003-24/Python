# l1=[1,2,3,4,5]
# res=list(map(lambda x: 'even' if x%2==0 else 'odd',l1))
# print(res)

# l1=[1,2,3,4,5]
# res=list(map(lambda x:x**2,l1))
# print(res)

# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]

# res=list(map(lambda x,y:x+y,l1,l2))
# print(res)

# l1=[1,2,3,4,5]
# res=list(filter(lambda x:'even' if x%2==0 else '',l1))
# print(res)

# l1=['neeraj','raj','jay']
# res=list(map(lambda x: x.upper(),l1))
# print(res)

# import functools

# l1=[1,2,3,4,5]
# res=functools.reduce(lambda x,y:x+y,l1)

# print(res)
x=5
y=6
# for i in range(1,5):
#     print(i.append([1,2,3,4]))
res=list(lambda x,y : [[j for j in range(1,x)] for i in range(1,y)])
print(res)
# for _ in range(1,5):
#     print('hi')
# print(res)