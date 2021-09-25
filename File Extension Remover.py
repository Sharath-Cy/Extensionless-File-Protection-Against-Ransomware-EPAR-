import os
import tkinter as tk
from tkinter import simpledialog

#Creating an Instance of tKinter
ROOT = tk.Tk()

#Removes the window from the screen (without destroying it
ROOT.withdraw()

# Code help from https://djangocentral.com/creating-user-input-dialog/
# dialogue to recieve the path to monitor
folderPath = simpledialog.askstring(title="Path", prompt="Please Enter The Folder Path To Monitor:")

#to get list of all files in specified folder and subfolders within it.
#Code help https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
def getListOfFiles(folderPath):

    listOfFiles = os.listdir(folderPath)
    allTheFiles = list()
    # Iterate through all the entries
    for entry in listOfFiles:
        # Create the complete path by joining the given folderName Path with the entries (fileNames)
        fullPath = os.path.join(folderPath, entry)
        # if the fullPath is directory then get the list of all the files
        if os.path.isdir(fullPath):
            allTheFiles = allTheFiles + getListOfFiles(fullPath)
        else:
            allTheFiles.append(fullPath)
                
    return allTheFiles  

while True:
   
    listOfFiles = getListOfFiles(folderPath)
    for files in listOfFiles:
        try:
            # 1. splits the extension from the file name and rename it without extensions.
            # 2. Renames the file name without extensions
            newpath = os.path.splitext(files)[0]
            os.rename(files, newpath)
        except Exception:
            pass