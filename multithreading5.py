def SumEven(No):
   Sum = 0

   for i in range(2,No,2):
       Sum = Sum+i
       print("Summation of even :",Sum)
   def SumOdd(No):
      Sum = 0
        
   for i in range(1,No,2):
       Sum = Sum+i
       print("Summation of Odd :",Sum)


def main():
  
    SumEven(100000000)
    SumOdd(1000000000)


   if __name__ == "__main__" :
      main()