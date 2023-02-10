import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

# Import other modules
import phonebook_main
import phonebook_gui

def center_window(self, w, h): # pass in the frame (master) and w / h
    # get user's screen width / height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x y coords to center app on user screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# catch if user clicks "X", check if they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program","Okay to exit application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)

#=================================
# create phonebook database
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@gmail.com'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

# Select item in ListBox
def onSelect(self,event):
    # calling event self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # this returns a tuple we can slice into 4 parts using data[] during iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize data to keep it consistent
    var_fname = var_fname.strip() # remove any black spaces before/after user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine normalized names into fullname
    print("var_fullname: {}".format(var_fullname)) # console print check to ensure it worked
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: # will use this soon
        print("Incorrect email format!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): # enforces user to provide both names
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            # check database for existance of fullname, if so, alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname)) #,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0, there is no existance of fullname - add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update listbox with new fullname
                onClear(self) # call function to clear all textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name".format(var_fullname))
                onClear(self) # call function to clear all textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")
        
def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # listbox's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure this is not the last record in the database
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All information associate with, ({}) \nwill be permanently deleted from the database. \n\nProceed with deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # call function to clear all textboses and selected index of listbox
######              onRefresh(self) # update the listbox of the changes
                conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
        conn.close()

def onDeleted(self):
    # clear the text in these textboxes
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)
###         onRefresh(self) # update the listbox of the changes
        try:
            index = self.lstList1.curselection()[0]
            self.lstList1.delete(index)
        except IndexError:
            pass

def onClear(self):
    # clear the text in these textboxes
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)

def onRefresh(self):
    # populate listbox, coinciding with database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()

if __name__ == "__main__":
    pass