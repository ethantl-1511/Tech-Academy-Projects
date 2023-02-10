from tkinter import *
# assignment part 1-4
#win = Tk()
#f = Frame(win)
#b1 = Button(f, text="One")
#b2 = Button(f, text="Two")
#b3 = Button(f, text="Three")
#b1.pack(side=LEFT)
#b2.pack(side=LEFT)
#b3.pack(side=LEFT)
#l = Label(win, text="This label is over all buttons")
#l.pack()
#f.pack()
#
#def but1():
#    print("Button one was pushed")
#
#b1.configure(command=but1)

# assignment part 5
#win = Tk()
#v = StringVar()
#e = Entry(win, textvariable = v)
#e.pack()
##v.get() use in console
##v.set() use in console

# assignment part 6
win = Tk()
lb = Listbox(win, height=3) # creates listbox
lb.pack() # aligns box
lb.insert(END, "first entry") # adds to list
lb.insert(END, "second entry") # adds to list
lb.insert(END, "third entry") # adds to list
lb.insert(END, "fourth entry") # adds to list
sb = Scrollbar(win, orient=VERTICAL) # creates a vertical scrollbar
sb.pack(side=LEFT, fill=Y) # fits to left
sb.configure(command=lb.yview) # command to scroll
lb.configure(yscrollcomand=sb.set) # command to connect to lb listbox
#lb.curselection() # use in console, shows currently selected index
