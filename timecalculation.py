def Factorial(No):
 Fact = 1
 for i in range(1,No+1):
    Fact = Fact * i
 return Fact
def main():
 value = int(input("enter numbern: "))

Ret = Factorial(value)
print("Factorial is :" ,Ret)7

if __name__ == "__main__":
    main()