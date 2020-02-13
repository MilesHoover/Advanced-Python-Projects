# modules
import os
import glob
import time

# Iterate through all files in directory
fPath = 'C:\\Users\\Miles\\Documents\\GitHub\\Advanced-Python-Projects\\fileCheck_Drill\\files\\'

dir_list = os.listdir(fPath) 
  
print("Files in '", fPath, "':\n")  
  
print(dir_list)

print("\n")

# Concatenate file name and path
fName = 'animalList.txt'

abPath = os.path.join(fPath, fName)

# Gather all .txt files in list, convert individual list elements to a string path,
# use that path to find when last modified 
os.chdir(fPath)
txtFiles = glob.glob('*.txt')

print("List of .txt files and when they were modified:\n")

i = 0
while i < len(txtFiles):
    txtFileString = "".join(txtFiles[i])

    txtFilePath = fPath + txtFileString

    modTimesinceEpoc = os.path.getmtime(txtFilePath)
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
 
    print(txtFileString + " was last modified on " + modificationTime)

    i += 1



    






