

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import os

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(481, 180) 
        self.master.maxsize(1000, 1000)
        self.master.title("Check Directory Path")
        self.master.configure(bg="#F0F0F0")

        for x in range(4):  
            self.master.grid_columnconfigure(x, weight=1)
            self.master.grid_rowconfigure(x, weight=1)
           
        self.browse1_string = StringVar()
        
        self.txt_browse1 = tk.Entry (self.master,textvariable=self.browse1_string)
        self.txt_browse1.grid(row=1, column=1,columnspan=3,padx=15, sticky='EW')
        
        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Folder Search',command=lambda:self.file_dialog(self.browse1_string))
        self.btn_browse1.grid(row=1)

        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program', command=lambda:self.ask_quit())
        self.btn_close.grid(row=2,column=3, padx=15,sticky = 'E')


    def file_dialog(self, txt_entry):
        txt_entry.set(filedialog.askdirectory())

    def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
            #This closes app
            self.master.destroy()
            os._exit(0)


if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
