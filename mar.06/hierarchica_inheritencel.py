class Parent:
    def home(self):
        print('from parent class')

class Child1(Parent):
    def home1(self):
        print('from child1 class')

class Child2(Parent):
    def hom2(self):
        print('from child2 class')

obj=Child1()
obj.home()
obj1=Child2()
obj1.home()