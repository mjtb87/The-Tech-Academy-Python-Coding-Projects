

from tkinter import *
import tkinter as tk


#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(481, 180) 
        self.master.maxsize(1000, 1000)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        for x in range(4):  
            self.master.grid_columnconfigure(x, weight=1)
            self.master.grid_rowconfigure(x, weight=1)
           

        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse')
        self.btn_browse1.grid(row=1)
        self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse')
        self.btn_browse2.grid(row=2)
        self.btn_check_files = tk.Button(self.master,width=12,height=2,text='Check for files...')
        self.btn_check_files.grid(row=3)
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
        self.btn_close.grid(row=3,column=3, padx=15,sticky = 'E')

        self.txt_browse1 = tk.Entry (self.master,text='')
        self.txt_browse1.grid(row=1, column=1,columnspan=4,padx=15, sticky='EW')
        self.txt_browse2 = tk.Entry (self.master,text='')
        self.txt_browse2.grid(row=2, column=1,columnspan=4,padx=15, sticky='EW')
      
        



if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
