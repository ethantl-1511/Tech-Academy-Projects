from tkinter import *
import tkinter as tk

# Import other modules
import phonebook_gui
import phonebook_func

# GUI frame
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame config
        self.master = master
        self.master.minsize(500,300) # height / width
        self.master.maxsize(500,300)
        # center_window method will center the app on the screen
        phonebook_func.center_window(self,500,300)
        self.master.title('Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0')
        # protocol method will catch if user clicks "X"
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in GUI widgets from separate module
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()

    