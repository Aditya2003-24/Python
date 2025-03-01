class Aditya:
   
    age=24
    def __init__(self,a,b):
        Aditya.lastname='Yadav'
        name='aman'
        self.x=a
        self.y=b
        print(name)

    def show(self):
        print(Aditya.lastname,self.x,self.y,)


print(Aditya.age)
obj=Aditya('ak',22)
obj.show()

# dacorater