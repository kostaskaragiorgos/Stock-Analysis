from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog

import pandas as pd 

class Stock_Analysis ():
    def __init__(self,master):
        self.master = master
        self.master.title("Stock Analysis")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.filename = ""
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert a csv",command = self.insert_csv)
        self.file_menu.add_command(label  = "Close csv",command = self.closef)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.show_menu = Menu (self.menu,tearoff = 0)
        self.show_menu.add_command(label = "Show csv",command = self.showcsv)
        self.menu.add_cascade(label = "Show", menu = self.show_menu)

        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
    
    def showcsv(self):
        msg.showinfo("DATA FRAME" , str(self.df))

    
    def closef(self):
        pass


    def insert_csv(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        
        # csv file stracture : Date Open High Low Close Adj Volume
        if ".csv" in self.filename:
            msg.showinfo("SUCCESS","CSV FILE ADDED SUCCESSFULLY")
            self.df = pd.read_csv(self.filename)
        else:
            msg.showerror("ERROR" ,"NO CSV FILE ADDED ") 


    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    def aboutmenu(self):
        pass

def main():
    root=Tk()
    SA = Stock_Analysis(root)
    root.mainloop()
    
if __name__=='__main__':
    main()