# output.py
# This was created by tkautox.py, layout.xlsx and tkauto_tpl.py

from tkinter import *
# from tkinter.font import Font
# import requests, sys, os, csv, webbrowser
# from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        self.columnconfigure(1, weight=1, pad=10)
        self.rowconfigure(1, weight=1, pad=20)
        self.rowconfigure(2, weight=1, pad=20)
        self.rowconfigure(3, weight=1, pad=20)
        self.rowconfigure(4, weight=1, pad=20)
        self.rowconfigure(5, weight=1, pad=20)

        root.geometry("200x200")

        self.radvar = StringVar() # Use one Var per group of buttons
        r1 = Radiobutton(self, variable=self.radvar, value='Fish', text='Fish')
        r1.grid(row=1, column=1 , sticky=E+W)
        r2 = Radiobutton(self, variable=self.radvar, value='Ham', text='Ham')
        r2.grid(row=2, column=1 , sticky=E+W)
        r3 = Radiobutton(self, variable=self.radvar, value='Beef', text='Beef')
        r3.grid(row=3, column=1 , sticky=E+W)

        optionlist = ('1.0 lb', '1.5 lb', '2.0 lb', '0.5 lb')
        self.optv = StringVar()
        self.optv.set(optionlist[0])
        optionlist = OptionMenu(self, self.optv, *optionlist)
        optionlist.grid(row=4, column=1 )

        btn = Button(self, text='Order', command=self.on_btn_clicked, relief=FLAT)
        btn.grid(row=5, column=1 , sticky=E+W)


# from tkinter import messagebox
# messagebox.showerror("Error", "Error message")
# messagebox.showwarning("Warning","Warning message")
# messagebox.showinfo("Information","Informative message")
# messagebox.askokcancel('Message title', 'Message content')
# messagebox.askretrycancel('Message title', 'Message content')
#     ok, yes, retry returns TRUE
#     no, cancel returns FALSE


    def on_btn_clicked(self):
        meat = self.radvar.get()
        weight = self.optv.get()
        print(meat, weight)
        messagebox.showinfo("Meat Order",meat + "\n" + weight)



    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass

#

# def save_location():
#     ''' executes at WM_DELETE_WINDOW event '''
#     with open("winfoxy", "w") as fout:
#         fout.write(str(root.winfo_x()) + "\n" + str(root.winfo_y() - 24))
#     root.destroy()

root = Tk()

# root.geometry("200x120") # WxH+left+top
# or the following:
''' the following repositions the window from last time '''
# if os.path.isfile("winfoxy"):
#     lcoor = tuple(open("winfoxy", 'r'))  # no relative path for this
#     root.geometry('350x200+%d+%d'%(int(lcoor[0].strip()),int(lcoor[1].strip())))
# else:
#     root.geometry("350x200") # WxH+left+top

root.title("Meat")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
