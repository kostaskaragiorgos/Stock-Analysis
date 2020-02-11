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
        
        #menu

        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert a csv",command = self.insert_csv)
        self.file_menu.add_command(label  = "Close csv",command = self.closef)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.show_menu = Menu (self.menu,tearoff = 0)
        self.show_menu.add_command(label = "Show csv",command = self.showcsv)
        self.menu.add_cascade(label = "Show", menu = self.show_menu)

        self.range_menu = Menu (self.menu,tearoff = 0)
        self.range_menu.add_command(label = "Show Date Range", command = self.daterange)
        self.menu.add_cascade(label = "Range", menu = self.range_menu)

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

        """ shows the whole dataset """ 

        if self.filename == "":
            msg.showinfo("ERROR","NO CSV FILE")
        else:
            msg.showinfo("DATA FRAME" , str(self.df))

    
    def daterange(self):
        if self.filename == "":
            msg.showinfo("ERROR","NO CSV FILE")
        else:
            from1= self.df.iloc[0]['Date']
            to1 =  self.df.iloc[-1]['Date']
            msg.showinfo("Date Range","From: "+str(from1) +"\nTo: " +str(to1) )


    def closef(self):
        pass


    def insert_csv(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        
        # csv file stracture : Date,Open,High,Low,Close,Adj Close,Volume
        if ".csv" in self.filename:
            self.df = pd.read_csv(self.filename)
            if all([item in self.df.columns for item in ['Date','Open','High','Low','Close','Adj Close','Volume']]) == TRUE:
                msg.showinfo("SUCCESS","CSV FILE ADDED SUCCESSFULLY")
            else:
                self.filename = ""
                msg.showerror("ERROR" ,"NO PROPER CSV ") 
        else:
            msg.showerror("ERROR","NO CSV IMPORTED")


    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass

    def aboutmenu(self):
        msg.showinfo("About", "Version 1.0")

def main():
    root=Tk()
    SA = Stock_Analysis(root)
    root.mainloop()
    
if __name__=='__main__':
    main()