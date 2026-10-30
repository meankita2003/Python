import sys

import os
import time
import schedule
##########################################################
#
# functio name :      mmain
# Input :             Command 
#
#
#
##########################################################

def DirectoryScanner(DirectoryPath):
   timesamp = time.ctime()


   logfileName = "Marvellous%s.log"%(timestamp)
   logfileName = logfileName.replace(" ","_")
   logfileName = logfileName.repalce(";","_")

   Ret = False

   Ret= os.path.exists(DirectoryPath)
   if(Ret == False):
    print("Marvellous Automation Error : There is no such directory with name,DirectoryPath")
    return

   Ret= os.path.isdir(DirectoryPath)
   
   if(Ret == False):
      print("Marvellous Automation Error : it is not a directory with name")
      return
   

   print("Log file gets created with name : ",LogfileNam)

   fobj = open(LogFileName,"w")
   print("filename is : ",logfileName)
   fobj = open("Marvellouslog.txt","w")
   fobj.write("Marvellous Automation script \n")
   fobj.write("files from the directory are :")



   for FolderName, FileName in os.waalk(DirectoryPath):
      for Fname in FileName :
         fname = os.path.join(folderName,fName)
      fobj.write(fname+"\n")

      fobj.write("Total file scanned :" + TotalFiles+"\m")
      fobj.write("Total empty files found and deleted :" +EmptyFile+"\n")


      totalfiles = 0
      EmptyFiles = 0


      print(f"file name{fname}==0")
      EmptyFile = EmptyFile + 1
print(fname)

def main():
   Border= "-"*40
print("")


def main():












    if(len(sys.argv) !=2):
     print("DirectoryName is : ",DirectoryName)
     print("DirectoryName")
    DirectoryName = sys.argv[1]

    print(len(sys.argv))
    else:


 Schedule.every.(1).minute.do(DirectoryScanner)

while True:
   schedule.run_pending()
   time.sleep(1)

print("Invalid number of ")
    


print("________________________")
print("_________ Marvallous Automation script ___________")
print("________________________________")













##########################################################
#
# functio name :      mmain
# Input :             Command
#
#
#
########################################################




if __name__ == "__main__":
    main()