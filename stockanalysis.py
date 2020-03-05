"""Analysis of stocks"""
from tkinter import Menu, messagebox as msg, filedialog, Tk
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
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv",
                                   accelerator='Ctrl + O', command=self.insert_csv)
        self.file_menu.add_command(label="Close csv", accelerator='Ctrl+F4',
                                   command=self.closef)
        self.file_menu.add_command(label="Save Range Data", command=self.save_range_data)
        self.file_menu.add_command(label="Exit",
                                   accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show Graph Summary", accelerator='Ctrl+S',
                                   command=self.showgraphsummary)
        self.show_menu.add_command(label="Show csv",
                                   accelerator='Alt+S', command=self.showcsv)
        self.show_menu.add_command(label="Show Open Graph",
                                   accelerator='Alt + T', command=self.opengraph)
        self.show_menu.add_command(label="Show High Graph",
                                   accelerator='Alt + U', command=self.highgraph)
        self.show_menu.add_command(label="Show Low Graph",
                                   accelerator='Alt + Q', command=self.lowgraph)
        self.show_menu.add_command(label="Show Close Graph",
                                   accelerator='Alt + C', command=self.closegraph)
        self.show_menu.add_command(label="Show Adj Close Graph", 
                                   accelerator='Alt + D', command=self.adjclosegraph)
        self.show_menu.add_command(label="Show Volume Graph",
                                   accelerator='Alt + B', command=self.volumegraph)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.range_menu = Menu(self.menu, tearoff=0)
        self.range_menu.add_command(label="Show Date Range",
                                    accelerator='Ctrl + D', command=self.daterange)
        self.range_menu.add_command(label="Show Open Range", 
                                    accelerator='Alt + O', command=self.openrange)
        self.range_menu.add_command(label="Show High Range",
                                    accelerator='Alt + H', command=self.highrange)
        self.range_menu.add_command(label="Show Low Range",
                                    accelerator='Alt + L', command=self.lowrange)
        self.range_menu.add_command(label="Show Close Range", 
                                    accelerator='Alt + C', command=self.closerange)
        self.range_menu.add_command(label="Show Adj Close Range", 
                                    accelerator='Alt + A', 
                                    command=self.adjcloserange)
        self.range_menu.add_command(label="Show Volume Range",
                                    accelerator='Alt + V', command=self.volumerange)
        self.menu.add_cascade(label="Range", menu=self.range_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insert_csv())
        self.master.bind('<Alt-s>', lambda event: self.showcsv())
        self.master.bind('<Control-d>', lambda event: self.daterange())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Alt-o>', lambda event: self.openrange())
        self.master.bind('<Alt-h>', lambda event: self.highrange())
        self.master.bind('<Alt-l>', lambda event: self.lowrange())
        self.master.bind('<Alt-c>', lambda event: self.closerange())
        self.master.bind('<Alt-a>', lambda event: self.adjcloserange())
        self.master.bind('<Alt-v>', lambda event: self.volumerange())
        self.master.bind('<Alt-t>', lambda event: self.opengraph())
        self.master.bind('<Alt-u>', lambda event: self.highgraph())
        self.master.bind('<Alt-q>', lambda event: self.lowgraph())
        self.master.bind('<Alt-c>', lambda event: self.closegraph())
        self.master.bind('<Alt-d>', lambda event: self.adjclosegraph())
        self.master.bind('<Alt-b>', lambda event: self.volumegraph())
        self.master.bind('<Control-s>', lambda event: self.showgraphsummary())
        self.master.bind('<Control-F4>', lambda event: self.closef())
    def save_range_data(self):
        """ test
        print(str(self.df.iloc[0]['Date']))
        print(str(self.df.iloc[-1]['Date']))
        print("Open Range", "Max: " +str(max(self.df['Open'])) +"\nMin: " +str(min(self.df['Open'])))
        print("High Range", "Max: "+str(max(self.df['High'])) + "\nMin: " +str(min(self.df['High'])))
        print("Low Range", "Max: "+str(max(self.df['Low'])) + "\nMin: " +str(min(self.df['Low'])))
        print("Close Range", "Max: "+str(max(self.df['Close'])) + "\nMin: " +str(min(self.df['Close'])))
        print("Adj Close Range", "Max: "+str(max(self.df['Adj Close'])) + "\nMin: " +str(min(self.df['Adj Close'])))
        print("Volume Range", "Max: "+str(max(self.df['Volume'])) + "\nMin: " +str(min(self.df['Volume'])))
        """

    def showgraphsummary(self):
        """ shows summary graph """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df.plot(title="Summary Graph")
            plt.show()
    def volumegraph(self):
        """ shows volume graph """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df['Volume'].plot(title="Volume Graph")
            plt.show()
    def highgraph(self):
        """ shows high graph """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df['High'].plot(title="High Graph")
            plt.show()
    def lowgraph(self):
        """ shows low graph"""
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df['Low'].plot(title="Low Graph")
            plt.show()
    def closegraph(self):
        """ shows close graph"""
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df['Close'].plot(title="Close Graph")
            plt.show()
    def adjclosegraph(self):
        """ shows adj close graph"""
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df['Adj Close'].plot(title="Adj Close Graph")
            plt.show()
    def opengraph(self):
        """ shows open graph"""
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            self.df['Open'].plot(title="Open Graph")
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
    def openrange(self):
        """ shows the range of Open """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("Open Range", "Max: " +str(max(self.df['Open'])) +"\nMin: " +str(min(self.df['Open'])))
    def highrange(self):
        """ shows the range of High """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("High Range", "Max: "+str(max(self.df['High'])) + "\nMin: " +str(min(self.df['High'])))
    def lowrange(self):
        """ shows the range of Low """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("Low Range", "Max: "+str(max(self.df['Low'])) + "\nMin: " +str(min(self.df['Low'])))
    def closerange(self):
        """ shows the range of Close """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("Close Range", "Max: "+str(max(self.df['Close'])) + "\nMin: " +str(min(self.df['Close'])))
    def adjcloserange(self):
        """ shows the range of Adj Close """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("Adj Close Range", "Max: "+str(max(self.df['Adj Close'])) + "\nMin: " +str(min(self.df['Adj Close'])))
    def volumerange(self):
        """ shows the range of Volume """
        if self.filename == "":
            msg.showerror("ERROR", "NO CSV FILE")
        else:
            msg.showinfo("Volume Range", "Max: "+str(max(self.df['Volume'])) + "\nMin: " +str(min(self.df['Volume'])))
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
            msg.showerror("Error", " A CSV FILE IS ALREADY OPEN")
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