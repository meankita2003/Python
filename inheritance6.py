class Base:
    def __init__(self):
        print("inside base1 gun")

        def gun(self):
         print("inside base2 fun")    

class Derived(Base):
     def __init__(self):
        super().__init__()
        print("inside derived sun")
bobj = Derived()

dobj.fun()
dobj.gun()
dobj.sun()