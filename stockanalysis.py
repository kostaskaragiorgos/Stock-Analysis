"""Analysis of stocks"""
from tkinter import Menu, messagebox as msg, filedialog, Tk
import csv
import pandas as pd
import matplotlib.pyplot as plt
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Import a csv file and gain info about stocks")
def aboutmenu():
    """ about menu function"""
    msg.showinfo("About", "Version 1.0")
class StockAnalysis():
    """ stock analysis class """
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Analysis")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.filename = ""
        self.filenamesave = ""
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv",
                                   accelerator='Ctrl + O', command=self.insert_csv)
        self.file_menu.add_command(label="Close csv", accelerator='Ctrl+F4',
                                   command=self.closef)
        self.file_menu.add_command(label="Save Range Data", accelerator='Ctrl+T', command=self.save_range_data)
        self.file_menu.add_command(label="Exit",
                                   accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show Graph Summary", accelerator='Ctrl+S',
                                   command=self.showgraphsummary)
        self.show_menu.add_command(label="Show csv",
                                   accelerator='Alt+S', command=self.showcsv)
        self.show_menu.add_command(label="Show Open Graph",
                                   accelerator='Alt + T', command=lambda: self.graph('Open'))
        self.show_menu.add_command(label="Show High Graph",
                                   accelerator='Alt + U', command=lambda: self.graph('High'))
        self.show_menu.add_command(label="Show Low Graph",
                                   accelerator='Alt + Q', command=lambda: self.graph('Low'))
        self.show_menu.add_command(label="Show Close Graph",
                                   accelerator='Alt + C', command=lambda: self.graph('Close'))
        self.show_menu.add_command(label="Show Adj Close Graph", 
                                   accelerator='Alt + D', command=lambda: self.graph('Adj Close'))
        self.show_menu.add_command(label="Show Volume Graph",
                                   accelerator='Alt + B', command=lambda: self.graph('Volume'))
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.range_menu = Menu(self.menu, tearoff=0)
        self.range_menu.add_command(label="Date Range",
                                    accelerator='Ctrl + D', command=self.daterange)
        self.range_menu.add_command(label="Open Range", 
                                    accelerator='Alt + O', command=lambda: self.range('Open'))
        self.range_menu.add_command(label="High Range",
                                    accelerator='Alt + H', command=lambda: self.range('High'))
        self.range_menu.add_command(label="Low Range",
                                    accelerator='Alt + L', command=lambda: self.range('Low'))
        self.range_menu.add_command(label="Close Range", 
                                    accelerator='Alt + C', command=lambda: self.range('Close'))
        self.range_menu.add_command(label="Adj Close Range", 
                                    accelerator='Alt + A', 
                                    command=lambda: self.range('Adj Close'))
        self.range_menu.add_command(label="Volume Range",
                                    accelerator='Alt + V', command=lambda: self.range('Volume'))
        self.menu.add_cascade(label="Range", menu=self.range_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-t>', lambda event: self.save_range_data())
        self.master.bind('<Control-o>', lambda event: self.insert_csv())
        self.master.bind('<Alt-s>', lambda event: self.showcsv())
        self.master.bind('<Control-d>', lambda event: self.daterange())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Alt-o>', lambda event: self.range('Open'))
        self.master.bind('<Alt-h>', lambda event: self.range('High'))
        self.master.bind('<Alt-l>', lambda event: self.range('Low'))
        self.master.bind('<Alt-c>', lambda event: self.range('Close'))
        self.master.bind('<Alt-a>', lambda event: self.range('Adj Close'))
        self.master.bind('<Alt-v>', lambda event: self.range('Volume'))
        self.master.bind('<Alt-t>', lambda event: self.graph('Open'))
        self.master.bind('<Alt-u>', lambda event: self.graph('High'))
        self.master.bind('<Alt-q>', lambda event: self.graph('Low'))
        self.master.bind('<Alt-c>', lambda event: self.graph('Close'))
        self.master.bind('<Alt-d>', lambda event: self.graph('Adj Close'))
        self.master.bind('<Alt-b>', lambda event: self.graph('Volume'))
        self.master.bind('<Control-s>', lambda event: self.showgraphsummary())
        self.master.bind('<Control-F4>', lambda event: self.closef())
    def save_range_data(self):
        """ saves a csv data with the max min values"""
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            if self.filenamesave is None or self.filenamesave == "":
                msg.showerror("ERROR", "NO FILE SAVED")
            else:
                with open(str(self.filenamesave)+'.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
                    thewriter.writerow([str(self.df.iloc[0]['Date']), str(max(self.df['Open'])), str(max(self.df['High'])), str(max(self.df['Low'])), str(max(self.df['Close'])), str(max(self.df['Adj Close'])), str(max(self.df['Volume']))])
                    thewriter.writerow([str(self.df.iloc[-1]['Date']), str(min(self.df['Open'])), str(min(self.df['High'])), str(min(self.df['Low'])), str(min(self.df['Close'])), str(min(self.df['Adj Close'])), str(min(self.df['Volume']))])
                msg.showinfo("SUCCESS", "CSV FILE SAVED SUCCESSFULLY")

    def showgraphsummary(self):
        """ shows summary graph """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df.plot(title="Summary Graph")
            plt.show()
    def graph(self,graphname):
        """ shows volume graph """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df[graphname].plot(title=graphname+" Graph")
            plt.show()
    def showcsv(self):
        """ shows the whole dataset """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("DATA FRAME", str(self.df))
    def daterange(self):
        """ shows the range of Date """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            from1 = self.df.iloc[0]['Date']
            to1 = self.df.iloc[-1]['Date']
            msg.showinfo("Date Range", "From: "+str(from1) +"\nTo: " +str(to1))

    def range(self,rangename):
        """ shows the range of Open """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("Open Range", "Max: " +str(max(self.df[rangename])) +"\nMin: " +str(min(self.df[rangename])))
    def closef(self):
        """ closes file """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.filename = ""
            msg.showinfo("SUCCESS", "CSV FILE SUCCESSFULLY CLOSED")
    def insert_csv(self):
        """ insert csv function """
        # csv file stracture : Date,Open,High,Low,
        # Close,Adj Close,Volume
        if self.filename == "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            if ".csv" in self.filename:
                self.df = pd.read_csv(self.filename)
                if all([item in self.df.columns for item in ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]):
                    msg.showinfo("SUCCESS", "CSV FILE ADDED SUCCESSFULLY")
                else:
                    self.filename = ""
                    msg.showerror("ERROR", "NO PROPER CSV ")
            else:
                self.filename = ""
                msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            msg.showerror("ERROR", " A CSV FILE IS ALREADY OPEN")
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function"""
    root = Tk()
    StockAnalysis(root)
    root.mainloop()
if __name__ == '__main__':
    main()