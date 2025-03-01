class Student:
    school='shss'
    count=0

    def __init__(self,name,roll):
        self.x=name
        self.y=roll
        Student.s_code=123
        Student.count=Student.count+1

    def new(self):
        Student.city = 'bhopal'

    def show(self):
        print(Student.school,Student.s_code,Student.city,Student.subject)

Student.subject='pcm'
obj=Student('aditya',101)
obj.new()
obj.show()
print(Student.count)
obj1=Student('aditya',102)
print(Student.count)
print(Student.z)