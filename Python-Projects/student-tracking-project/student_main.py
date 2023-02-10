# Python:   3.10.7
# Author:   Ethan LaRocca
# Purpose:  Student-tracking project, using a GUI that will 
#           allow a user to add a student's details to a 
#           database list, view it, and delete entries.

from tkinter import *
import tkinter as tk

import student_gui
import student_func

# Frame
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)   
        # defime master frame config
        self.master = master
        self.master.minsize(525,350) # max width / height
        self.master.minsize(525,350) # min size
        self.master.title('Student Tracking') # page title label
        self.master.configure(bg='#F0F0F0') # page background color
        arg = self.master
        student_gui.load_gui(self) # load GUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()