# Python: 3.10.7
#
# Author: Ethan LaRocca
#
# Purpose:  For this assignment, you will need 
#           to write a script that creates a database and 
#           adds new data into that database.

import sqlite3

conn = sqlite3.connect('.database.db') # connects to 'database.db', if it doesn't exist it gets created

# Creating a table with 2 fields
with conn: # opens database file
    cur = conn.cursor() # operators database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit() # commits changes
conn.close() # closes database file

conn = sqlite3.connect('.database.db') # connecting again
# File list for assignment, slightly modified but still contains the two .txt files
fileList = ('information.docx','hello.txt','myImage.png', \
            'myMovie.mp4','world.txt','data.pdf','myPhoto.jpg')

# Loop to check for .txt
for item in fileList:
    if item.endswith('.txt'):
        with conn: # open database file
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (item,)) # insert the info into table
            print(item) # print to console
conn.close # close database 