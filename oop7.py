class Demo:
    # class variable
    value1 = 10
    value2 = 20

    def __init__ (self):
        self.No1 = 11
        self.No2 = 21
    #   instance method
        def fun(self):
            print("Inside instance method named as fun")
            print(self.No1)
            print(self.No2)
            print(self.value1)
            print(self.value2)

           
        def gun(cls):  
             print("Inside instance method named as fun")
            #  print(self.No1)
            #  print(self.No2)
             print(cls.value1)
             print(cls.value2)

        @staticmethod 
        def  sun():
            print("Inside instance method named as sun")
            
            print(self.value1)
            print(self.value2)

         
Demo.sun()
