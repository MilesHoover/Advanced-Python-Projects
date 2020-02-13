# Modules

from tkinter import *
import tkinter as tk
from tkinter import filedialog

# Main window size & config

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.minsize(500, 100)
        self.master.maxsize(500, 100)
        self.master.title("Folder Selector")
        self.master.configure(bg="lightgray")

# File explorer button & entry field
        
        self.btn_FileExplorer = tk.Button(self.master, command=self.getAdir, width=12, bg="#e5e5e5", text="Browse...")
        self.btn_FileExplorer.grid(row=1, column=0, padx=(15,0), pady=(35,0), sticky=W)

        self.txtBox = tk.Text(self.master, height=1, width = 40)
        self.txtBox.grid(row=1, column=1, padx=(15,0), pady=(35,0), sticky=W)
        
# Retrieve file path

    def getAdir(self):
        self.Directory = filedialog.askdirectory(initialdir = "c:\\", title='Please select a directory')
        self.txtBox.insert('1.0', self.Directory)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
