class School:
    def add(self,a,b):
        self.x=a
        self.y=b
        self.z=self.x+self.y
        return self.z
    def min(self,c):
        self.d=c
        return self.x-self.d

obj=School()
print(obj.add(4,8))
print(obj.min(2))
obj1=School()
print(obj1.add(9,9))