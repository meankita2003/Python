import threading

def Display(No):
   print(f"Inside Display :",threading.get_ident())
def main():
   print("Inside Display :",threading.get_ident())

   tobj = threading.Thread(target=Display)
   tobj.start()
   
    


   if __name__ == "__main__" :
      main()