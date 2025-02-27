# class Student:
#     "student details"

#     def __init__(self):
#         print('constructor called')
#         print('self',id(self))

# print(dir(Student))
# print(Student.__doc__)
# print(Student)
# obj=Student   #this is not a object
# print(obj)

# x=Student()  #this is a object () =>  ye call krta h init ko.
# print(x)

# # print(object=Student)
# # print(obje=Student())

# print(id(x))

# class Student:
#     "student details"
#     def __init__(self,name,rol,marks):
#         self.x=name
#         self.y=rol
#         self.z=marks



# obj=Student('aditya',101,80)
# print(obj.x)
# print(obj.y)
# print(obj.z)

class Student:
    "student details"
    def __init__(self,name,rol,marks):
        self.x=name
        self.y=rol
        self.z=marks
    def __init__(self):
        print('constructor called')


obj=Student()
