# Python:   3.10.7
# Author:   Ethan LaRocca
# Purpose:  File Transfer project, using a GUI that will allow a user to select 
#           a Source directory and Destination directory, clicking the Transfer 
#           Files button will automatically transfer files from Source to 
#           Destination if the files are less than 24 hours old.

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        # create button to select files from source dir
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0,column=0, padx=(20,10),pady=(30,0))
        # create entry for source dir selection
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0,column=1,columnspan=2, padx=(20,10),pady=(30,0))

        # create button to select destination files from destination dir
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1,column=0, padx=(20,10),pady=(15,10))
        # create entry for destination dir selection
        self.dest_dir = Entry(width=75)
        self.dest_dir.grid(row=1,column=1,columnspan=2, padx=(20,10),pady=(15,10))

        # create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2,column=1, padx=(200,0),pady=(0,15))

        # create exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2,column=2, padx=(10,40),pady=(0,15))
    
    # function to select source dir
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # clears content that is inserted into Entry. allows path to be insert into entry.
        self.source_dir.delete(0, END)
        # inserts user selection to source_dir entry
        self.source_dir.insert(0, selectSourceDir)
    
    # function to select destination dir, similar to above sourceDir
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.dest_dir.delete(0, END)
        self.dest_dir.insert(0, selectDestDir)

    # create function to transfer files
    def transferFiles(self):
        # get things
        source = self.source_dir.get() # gets the source path
        destination = self.dest_dir.get() # gets the destination destionation
        source_files = os.listdir(source) # arrray of files in directory
        # run through each file in source dir
        for file in source_files:
            if '.' in file:
                curTime = datetime.now() # gets the local time
                fPath = os.path.join(source,file)
                lastModified = os.path.getmtime(fPath) # gets file's last modified apoch, sets as variable
                fileTime = datetime.fromtimestamp(lastModified) # gets time stamp from lastModified, sets as variable
                expiredFileTime = fileTime + timedelta(hours = 24) # the file will be considered old after 24 hours
                if curTime <= expiredFileTime: # if the current time is less than or equal to the expiredFileTime, transfer files.
                    shutil.move(source + '/' + file, destination)
                    print(file + ' was successfully transferred.')
                else:
                    print(file + ' was older than 24 hours and NOT transferred.')

    # create function to exit program
    def exit_program(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()