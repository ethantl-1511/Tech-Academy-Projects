from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

import student_main
import student_gui

#============================
# create student database
def create_db(self):
    conn = sqlite3.connect('student-tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            firstName TEXT, \
            lastName TEXT, \
            fullName TEXT, \
            phone TEXT, \
            email TEXT, \
            course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('student-tracking.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (firstName,lastName,fullName,phone,email,course) VALUES (?,?,?,?,?,?)""", ('Example','Student','Example Student','000-000-0000','email@email.com','course000'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count

# function to Select item in ListBox
def onSelect(self,event):
    # call event self.list1 widget
    varList1 = event.widget
    select = varList1.curselection()[0]
    value = varList1.get(select)
    conn = sqlite3.connect('student-tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT firstName,lastName,phone,email,course FROM tbl_students WHERE fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # returns a tuple we can slice into 5 parts using data[] during iteration
        for data in varBody:
            self.textfirstName.delete(0,END)
            self.textfirstName.insert(0,data[0])
            self.textlastName.delete(0,END)
            self.textlastName.insert(0,data[1])
            self.textPhone.delete(0,END)
            self.textPhone.insert(0,data[2])
            self.textEmail.delete(0,END)
            self.textEmail.insert(0,data[3])
            self.textCourse.delete(0,END)
            self.textCourse.insert(0,data[4])

def onSubmit(self):
    var_firstName = self.textfirstName.get()
    var_lastName = self.textlastName.get()
    # normalize data
    var_firstName = var_firstName.strip() # remove any blanks before/after
    var_lastName = var_lastName.strip() # remove any blanks before/after
    var_firstName = var_firstName.title()
    var_lastName = var_lastName.title()
    var_fullName = ('{} {}'.format(var_firstName,var_lastName)) # combine name
    print("var_fullname: {}".format(var_fullName))
    var_phone = self.textPhone.get().strip() # remove any blanks before/after 
    var_email = self.textEmail.get().strip() # remove any blanks before/after
    var_course = self.textCourse.get().strip() # remove any blanks before/after
    if not '@' or not '.' in var_email:
        print("Incorrect email format.")
    if (len(var_firstName) > 0) and (len(var_lastName) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('student-tracking.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(fullName) FROM tbl_students WHERE fullName = '{}'""".format(var_fullName))
            count = cursor.fetchone()[0]
            checkName = count
            if checkName == 0:
                print("checkName: {}".format(checkName))
                cursor.execute("""INSERT INTO tbl_students (firstName,lastName,fullName,phone,email, course) VALUES (?,?,?,?,?,?)""",(var_firstName,var_lastName,var_fullName,var_phone,var_email,var_course))
                self.list1.insert(END, var_fullName)
                onClear(self)
            else:
                messagebox.showerror("Name Error","'{}' already exists. Choose a different name.".format(var_fullName))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure data is entered into all fields.")


def onDelete(self):
    var_select = self.list1.get(self.list1.curselection())
    conn = sqlite3.connect('student-tracking.db')
    with conn:
        cur = conn.cursor()
         # check count to ensure this is not the last record in the database
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","Are you sure you want to delete ({})?".format(var_select))
            if confirm:
                conn = sqlite3.connect('student-tracking.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE fullName = '{}'""".format(var_select))
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","There must be one record in the database.\nCreate another record to delete ({}).".format(var_select))
    conn.close()
    
def onDeleted(self):
    self.textfirstName.delete(0,END)
    self.textlastName.delete(0,END)
    self.textPhone.delete(0,END)
    self.textEmail.delete(0,END)
    self.textCourse.delete(0,END)
    try:
        index = self.list1.curselection()[0]
        self.list1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.textfirstName.delete(0,END)
    self.textlastName.delete(0,END)
    self.textPhone.delete(0,END)
    self.textEmail.delete(0,END)
    self.textCourse.delete(0,END)

def onRefresh(self):

    self.list1.delete(0,END)
    conn = sqlite3.connect('student-tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT fullName FROM tbl_students""")
            varList1 = cursor.fetchall()[i]
            for item in varList1:
                self.list1.insert(0,str(item))
                i = i + 1
    conn.close()

if __name__ == "__main__":
    pass
