class MyClass:  
        number = 0       
        name = "noname"
  
def Main():
        me = MyClass()   
        me.number = 1337    
        me.name = "Harssh"
        print(me.name + " " + str(me.number))

if __name__=='__main__':  
        Main()