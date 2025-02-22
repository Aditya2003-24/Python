# def even(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             print(i)
#         i+=1
# x=even(10)
# print(x)
# print(type(x))


# def new():
#     return 5
# x=new()
# print(x)
# print(type(x))

def new():
    yield 10

x=new()
# print(x)
# print(type(x))
# print(list(x))
# print(x.__next__())
print(next(x))


def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
x=even(10)
# print(x)
# print(list(x))

a=next(x)
b=next(x)
c=next(x)
print(a,b,c)
