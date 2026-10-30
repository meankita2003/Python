import marvellous


def Addition(No1, No2):
   
    Ans = No1 + No2
    return Ans


def main():
    print("Enter First number :")
    value1 = int(input())

    print("Enter Second number :")
    value2 = int(input())

    Ret = marvellous.Addition(value1 , value2)          

    print("Addition is :",Ret)
if __name__ == "__main__":
    main()
