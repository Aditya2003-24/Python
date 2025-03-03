class Book:
    price=100
    total_pages=500           #static variable/class variable
    def __init__(self,title,outhor):
        self.title=title
        self.outhor=outhor
    @classmethod
    def update(cls,new_price,new_page_count):
        cls.price=new_price
        cls.total_pages=new_page_count

    @classmethod
    def add_new(cls,outhor):
        cls.outhor=outhor

    def show_data(self):
        print(self.title,self.outhor,Book.price,Book.total_pages)

obj=Book('python','Aditya')
Book.update(110,550)
obj.show_data()
