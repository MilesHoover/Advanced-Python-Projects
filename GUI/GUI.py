from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Main window size & config
        
        self.master = master
        self.master.minsize(500, 175)
        self.master.maxsize(500, 175)
        self.master.title("Check files")
        self.master.configure(bg="#e9e9e9")

        # Browse1 button & entry field
        
        self.btn_Browse1 = tk.Button(self.master, width = 12, bg="#e5e5e5", text = "Browse...")
        self.btn_Browse1.grid(row=1, column=0, padx=(15,0), pady=(40,0), sticky=W)

        self.btn_Browse1 = tk.Entry(self.master, width = 60, text = "")
        self.btn_Browse1.grid(row=1,column=1, padx=(15,0), pady=(40,0), sticky=W)

        # Browse2 button & entry field
        
        self.btn_Browse2 = tk.Button(self.master, width = 12, bg="#e5e5e5", text = "Browse...")
        self.btn_Browse2.grid(row=2, column=0, padx=(15,0), pady=(12,0), sticky=W)

        self.btn_Browse2 = tk.Entry(self.master, width = 60, text = "")
        self.btn_Browse2.grid(row=2, column=1, padx=(15,0), pady=(12,0), sticky=W)

        # Check button
        
        self.btn_Check = tk.Button(self.master, width = 12, height = 2, bg="#e5e5e5", text = "Check for files...")
        self.btn_Check.grid(row=3, column=0, padx=(15,0), pady=(12,0), sticky=W)

        # Close button
        
        self.btn_Close = tk.Button(self.master, width = 12, height = 2, bg="#e5e5e5", text = "Close Program")
        self.btn_Close.grid(row=3, column=1, padx=(285,0), pady=(12,0), sticky=W)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
