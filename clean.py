# import the necessary modules
import os
from pathlib import Path
import shutil
#sets a path variable with the value of the current directory
#Path are used to navigate between folders in the computer
path = Path.cwd()
#creates a class with the necessary functions
class Folder :
    
    def __init__(self,name, ):
        #sets the path name for the new folder to be created
        self.new_path = path / name
        
    def move_file(self,extension):
        #move files of a certain file type to the new path created in create function
        for item in path.glob('*.' + extension):
            shutil.move(item, self.new_path)
       
    def create(self,name):
        #creates a new file path (creates a new folder)
        os.makedirs(self.new_path)
    
    def check(self):
        #checks if the new folder to be created is already there
        if os.path.isdir(self.new_path):
            return True
        else:
            return False
        
 #creates a list of variables with the folder names of the folders to be created       
i = 0       
excel = ''
text = ''
PNGimages = ''
Documents = ''
JPGimages = ''
PDFfiles = ''
Filmora = ''    
variable_list =[excel,text,PNGimages,Documents,JPGimages,   PDFfiles,Filmora] 
#in the list below each file type is assigned its extension
list = {"Excel" : "xlsx", "textFiles":"txt", "PNGimages" :"png","Documents":"docx", "JPGimages":"jpg","PDFfiles":"pdf","Filmora":"wfp"}
#moves the files to the folders
for item in list:
    variable_list[i] = Folder(item)#creates folder instances
    if variable_list[i].check():
        variable_list[i].move_file(list[item])
    else:
        variable_list[i].create(item)
        variable_list[i].move_file(list[item])
    
        
        
    
    