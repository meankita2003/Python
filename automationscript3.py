import sys
def main():


    if(len(sys.argv) ==2):
     if(sys.argv[1] == "--h"):
        print("Help")
     elif(sys.argv[1] == "--u"):
        
     print("DirectoryName is : ",DirectoryName)
    DirectoryName = sys.argv[1]

    print(len(sys.argv))
else:
print("Invalid number of argunment")
print("please use --h or --u for more information")
    

if __name__ == "__main__":
    main()