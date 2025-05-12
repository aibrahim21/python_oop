from re import *
import os
myfile = r"/home/amira/Documents/vs/python day 3.1/file1.txt"




def read(filepath, options):
  
    if ( not os.path.exists(filepath)):
        print('this file path is not correct,Please check the file path and try again') 
    else :
        with open (filepath , 'r') as readthatfile:
        # if len(options) > 0:
            if options == "all":
                print(readthatfile.read() ) #read all lines
                #readthatfile.seek(0)
            elif options == "line": #reading starting from where the cursor ended 
                #cursor =readthatfile.tell()
                #readthatfile.seek(cursor)
                print(readthatfile.readline()) 
            elif  isinstance(options, int): #checking para is number
                 #change type to int in caase input 
                #filesize = os.path.getize(filepath) #getting file size in int
                # if num > filesize: #chescking if line number requested exist and not empty
                    # print(f" your request of line {num} doesn't exist inside the file, try again ranging from 0 to {filesize}")
                #else: 
                print(readthatfile.readline(options))  #read specific number of lines




#read(myfile ,'all') 
#read(myfile ,'line') 
#read(myfile ,3)


#================================================================
 #write function 
path1 = r"/home/amira/Documents/vs/python day 3.1/file2.txt"
path3 = r"/home/amira/Documents/vs/python day 3.1/file5.txt"
path4 = r"/home/amira/Documents/vs/python day 3.1/file6.txt"


def write(pathoffile ,content):
    #write function creates a new file if it doesn't exist ans clears the existing file 
    if  os.path.exists(pathoffile):
        print("this file is cleared and ready to use it for write")
    elif not os.path.exists(pathoffile):
          print("this file doesn't existn we gonna create one for you no worries")
    with open(pathoffile,'w') as filetowrite:
        filetowrite.write(content)
        print("Content written successfully.")
#write(path1 ,"hello there, je m'appele amira, ")

#=====================================================================
#append
path2 = r"/home/amira/Dochello there, je m'appele amira, uments/vs/python day 3.1/file3.txt"

def append(pathoffile ,content):
    #write function creates a new file if it doesn't exist ans clears the existing file 
    
    if not os.path.exists(pathoffile):
          print("this file doesn't existn we gonna create one for you no worries")
    with open(pathoffile,'a') as filetoappend:
        filetoappend.writelines(content)
        print("Content written successfully.")
        
append(path4 ,"the is a new line added to the file")


#========================================================================