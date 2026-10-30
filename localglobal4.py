no = 11

def Display():
    global no
    no =  21

    print("From Dispaly : ",no)
    
    print("Before : ",no)
    Display()
    print("after :",no)