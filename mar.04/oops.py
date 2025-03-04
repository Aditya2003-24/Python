# oop's
# 1. abstraction class   => ye data ko hide karta hai 
from abc import ABC , abstractmethod
class BankApp(ABC):
    def login(self):
        print('user login.....')
    def logout(self):
        print('user logout.......')
    def userdata(self):
        print('user.details......')

    @abstractmethod
    def database(self):
        pass
class Webpage(BankApp):
          #inharit kar liya abstractclass ko
    def database(self):
        print('database connected........')

obj=Webpage()
obj.database()
obj.userdata()


# data ko rape karna encopsulation kehte hai / single unit class me rakhne ko encopsulation kehte hai


#advantages =>
# parent ki property child ke pas a jati hai inheritence me or ye time save karta hai and reduce.redandency (same code kam ho jayega jisko bar bar use kar rahe hai)