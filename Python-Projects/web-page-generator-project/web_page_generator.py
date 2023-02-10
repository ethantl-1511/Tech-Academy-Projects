import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # label for 'custom text'
        self.labelEntry = Label(self.master,text="Enter custom text or click the Default HTML page button")
        self.labelEntry.grid(row=0,column=1,padx=(20,10),pady=(20,0),sticky=N+W)
        # entry bar for 'custom text'
        self.textEntry = Entry(self.master,text="", width=128)
        self.textEntry.grid(row=1,column=1,columnspan=3, padx=(25,10),pady=(10,0),sticky=W)

        # button for 'default html', left of 'submit custom'
        self.btn = Button(self.master, text="Default HTML Page", width=30,height=2, command=self.defaultHTML)
        self.btn.grid(row=2,column=2,padx=(10,10),pady=(10,10))

        # button for 'submit custom', right of 'default html'
        self.submitBtn = Button(self.master, text="Submit Custom Text", width=30,height=2, command=self.customHTML)
        self.submitBtn.grid(row=2,column=3,padx=(10,10),pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!" # variable with text
        htmlFile = open("index.html", "w") # opens index.html, allow you to 'write'
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>" # variable with HTML structure and variable content for htmlFile
        htmlFile.write(htmlContent) # writes the content from htmlContent
        htmlFile.close() # closes htmlFile
        webbrowser.open_new_tab("index.html") # opens a webbrowser, opens a new tab with index.html

    def customHTML(self):
        customText =  self.textEntry.get()
        htmlFile = open("index.html", "w") # opens index.html, allow you to 'write'
        htmlContent = "<html>\n<body>\n<h1>" + str(customText) + "</h1>\n</body>\n</html>" # variable with HTML structure and variable content for htmlFile
        htmlFile.write(htmlContent) # writes the content from htmlContent
        htmlFile.close() # closes htmlFile
        webbrowser.open_new_tab("index.html") # opens a webbrowser, opens a new tab with index.html

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()