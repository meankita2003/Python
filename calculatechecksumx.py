import sys
import os
import hashlib

def calculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobjj = hashlib.md5()

    buffer = fobj.read(1000)

while(len(Buffer) > 0):
    hobj.update(Buffer)
    buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def main():
   Ret = CalculateCheckSum("Demo.txt")

   print("Checksum of file is :",Ret)

if __name__ == "__main__":
    main()