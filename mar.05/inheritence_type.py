# #1. single inheritence
# class Parent:
#     x=10
#     def home(self):
#         print('parent home')

# class Child(Parent):
#     y=10
#     def car(self):
#         print('child car')

# obj=Child()
# print(Child.x)  #this is correct way to call variable.
# obj.home()
# obj.car()

# # method over writing ko python sport krta hai.

# class Parent:
#     x=10
#     def home(self):
#         print('parent home')

# class Child(Parent):
#     y=10
#     def home(self):
#         super().home()   # this is use for called method over writing
#         print('child car')

# obj=Child()
# print(Child.x)  #this is correct way to call variable.
# obj.home()

#python me method over loading sport nhi hai


# MRO  =>  method resolution order  /  left first hot hai

#MULTI PAL INHERITENCE

# class Parent1:
#     def home(self):
#         print('parent1 home')

# class Parent2:
#     def home(self):
#         print('parent2 home')

# class Child1(Parent2,Parent1):
#     def car(self):
#         print('child car')

# obj=Child1()
# obj.home()



#multileval inhertence

class Grand_parent:
    def home(self):
        print('parent1 home')

class Parent(Grand_parent):
    def home(self):
        super().home()
        print('parent2 home')

class Child1(Parent):
    def car(self):
        print('child car')

obj=Child1()
obj.home()