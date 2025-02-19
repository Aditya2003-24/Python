# #function => two type of function
# 1.in-built function
# 2. user-define function


#positional argument

# def fun_name(x,y):
#         "This function for add two variables"
    
#         return x+y
    

# z= fun_name(8,4)
# print(z)

#key-word argument
def fun_name1(x,y):
        "This function for add two variables"

        print( 'value of ',x)
        print('value of',y)
    
        return x+y
    
m= fun_name1(y=8,x=4)
print(m)
print(fun_name1.__doc__)  #this is for check what is doc string.
print(dir(fun_name1))    #we use ( dir )for checking magic mathed
