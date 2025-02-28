#instance

class Student:
    def __init__(self,name,roll,marks):
        self.x=name
        self.y=roll                          #inside the class instance variable
        self.z=marks
    def add_new(self,city):                   #insstance method
        self.p=city

    def show(self):
        print(self.x,self.y,self.z,self.p,self.school_name)  

obj1=Student('Aditya',101,85)
obj1.school_name='SHSS'            #outside the class instance variable

obj1.add_new('pera')
obj1.show()

print(obj1.x,obj1.y,obj1.school_name,obj1.p,obj1.z)

#instance variable me object change karne ke sath uski value bhi change kar sakte hai usko instance variable bolte hai.



