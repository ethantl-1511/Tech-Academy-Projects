# Python: 3.10.7
#
# Author: Ethan LaRocca
#
# Purpose:  For this assignment, you will need to write a script 
#           that will check a specific folder on the hard drive, verify 
#           whether those files end with a “.txt” file extension and, 
#           if they do, print those qualifying file names 
#           and their corresponding modified time-stamps to the console.

import os

def checkFiles():
    # Use listdir() to get contents of directory, set to variable dir
    dir = os.listdir(path='C:\\Users\\Ethan\\My Folder\\__College\\Tech Academy\\07 Python') # This becomes an array of the files within this directory
    # Check the contents for ".txt"
    for file in dir:
        if '.txt' in file:
            ogPath = "C:\\Users\\Ethan\\My Folder\\__College\\Tech Academy\\07 Python"
            # Join path with the file
            fPath = os.path.join(ogPath, file)
            # Get the modified time-stamp
            modTime = os.path.getmtime(fPath)
            # Print path and time-stamp
            print(fPath + "\nLast Modified: " + str(modTime))
checkFiles()