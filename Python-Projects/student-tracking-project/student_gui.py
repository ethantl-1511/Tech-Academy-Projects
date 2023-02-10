from tkinter import *
import tkinter as tk

import student_main
import student_func

def load_gui(self):
    # first name label/text
    self.labelfirstName = tk.Label(self.master,text='First Name:')
    self.labelfirstName.grid(row=0,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.textfirstName = tk.Entry(self.master,text='', width=32)
    self.textfirstName.grid(row=1,column=0,rowspan=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
    # last name label/text
    self.labellastName = tk.Label(self.master,text='Last Name:')
    self.labellastName.grid(row=2,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.textlastName = tk.Entry(self.master,text='')
    self.textlastName.grid(row=3,column=0,rowspan=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
    # phone label/text
    self.labelPhone = tk.Label(self.master,text='Phone Number:')
    self.labelPhone.grid(row=4,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.textPhone = tk.Entry(self.master,text='')
    self.textPhone.grid(row=5,column=0,rowspan=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
    # email label/text
    self.labelEmail = tk.Label(self.master,text='Email Address:')
    self.labelEmail.grid(row=6,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.textEmail = tk.Entry(self.master,text='')
    self.textEmail.grid(row=7,column=0,rowspan=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
    # course label/text
    self.labelCourse = tk.Label(self.master,text='Current Course:')
    self.labelCourse.grid(row=8,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.textCourse = tk.Entry(self.master,text='')
    self.textCourse.grid(row=9,column=0,rowspan=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
    # student label
    self.labelStudent = tk.Label(self.master,text='Students:')
    self.labelStudent.grid(row=0,column=4,padx=(25,0),pady=(10,0),sticky=N+W)

    # scrollbar and list
    self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
    self.list1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar.set,width=32)
    self.list1.bind('<<ListboxSelect>>',lambda event: student_func.onSelect(self,event))
    self.scrollbar.config(command=self.list1.yview)
    # scrollbar and list placement
    self.scrollbar.grid(row=1,column=20,rowspan=9,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.list1.grid(row=1,column=4,rowspan=9,columnspan=13,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    # buttons
    self.buttonSubmit = tk.Button(self.master,width=10,height=2,text='Submit',command=lambda: student_func.onSubmit(self))
    self.buttonSubmit.grid(row=10,column=0,padx=(15,0),pady=(45,8),sticky=W)
    self.buttonDelete = tk.Button(self.master,width=10,height=2,text='Delete',command=lambda: student_func.onDelete(self))
    self.buttonDelete.grid(row=10,column=1,padx=(15,0),pady=(45,8),sticky=W)

    student_func.create_db(self)
    student_func.onRefresh(self)

if __name__ == "__main__":
    pass