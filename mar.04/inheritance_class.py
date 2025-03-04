class A:
    x=10
    y=20
    def name(self):
        print('have a name')

    def car(self):
        print('have a car')

class B(A):
    def new_name(self):
        print('new name')

obj=B()
obj.car()
print(B.y)