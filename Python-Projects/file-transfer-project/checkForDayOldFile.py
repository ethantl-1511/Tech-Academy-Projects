# Python:   3.10.7
#
# Author:   Ethan LaRocca
#
# Purpose:  Snippet of code I created used for a function in a file transfer python project.

import os
from datetime import datetime, timedelta

curTime = datetime.now() # gets the local time
dir = os.listdir(path='C:\\Users\\Ethan\\Documents\\GitHub\\python-projects\\file-transfer-project\\Customer Source') # array of files in this path
for file in dir:
    if '.' in file:
        strPath = str(dir)
        fPath = os.path.join(strPath,file)
        lastModified = os.path.getmtime(fPath) # gets file's last modified apoch, sets as variable
        fileTime = datetime.fromtimestamp(lastModified) # gets time stamp from lastModified, sets as variable
        expiredFileTime = fileTime + timedelta(hours = 24) # the file will be considered old after 24 hours
        if curTime <= expiredFileTime: # if the current time is less than or equal to the expiredFileTime, transfer files.
            print("The file is less than or equal to EXACTLY 24 hours old. Automatically Transfer.")
        else:
            print("The file greater than 24 hours old. Do NOT Automatically Transfer.")