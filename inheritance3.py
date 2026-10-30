class Base:
    def __init__(self):
        print("inside base constructor")

class Derived(Base):
     def __init__(self):
        super().__init__()
        print("inside base constructor")
bobj = Derived()
