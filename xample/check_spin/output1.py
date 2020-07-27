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
        self.rowconfigure(4, weight=3, pad=20)
        self.rowconfigure(5, weight=3, pad=20)
        self.rowconfigure(6, weight=3, pad=20)

        root.geometry("230x200")

        self.cv1 = IntVar()
        ck1 = Checkbutton(self, relief=RAISED, variable=self.cv1, text=' ketchup ')
        ck1.grid(row=1, column=1 )

        self.cv2 = IntVar()
        ck2 = Checkbutton(self, relief=RAISED, variable=self.cv2, text=' mustard ')
        ck2.grid(row=2, column=1 )

        self.cv3 = IntVar()
        ck2 = Checkbutton(self, relief=RAISED, variable=self.cv3, text=' pickles ')
        ck2.grid(row=3, column=1 )

        lbl = Label(self, text='QUANTITY')
        lbl.grid(row=4, column=1 )

        self.svar = StringVar()
        spn = Spinbox(self, from_=1, to=9, relief=FLAT, width=2,
                      textvariable=self.svar)
        spn.grid(row=5, column=1 )

        btn = Button(self, text='Order', command=self.on_btn_clicked)
        btn.grid(row=6, column=1 )


# from tkinter import messagebox
# messagebox.showerror("Error", "Error message")
# messagebox.showwarning("Warning","Warning message")
# messagebox.showinfo("Information","Informative message")
# messagebox.askokcancel('Message title', 'Message content')
# messagebox.askretrycancel('Message title', 'Message content')
#     ok, yes, retry returns TRUE
#     no, cancel returns FALSE


    def on_btn_clicked(self):
        msg = ""
        ketchup = self.cv1.get()  # checkbox var is 1 (checked)
        mustard = self.cv2.get()  #     or 0 (not checked)
        pickles = self.cv3.get()
        quan = self.svar.get()
        print(ketchup)
        print(mustard)
        print(pickles)
        print(quan)
        if ketchup:  # in Python 1 is true, 0 is false
            msg += "ketchup\n"
        if mustard:
            msg += "mustard\n"
        if pickles:
            msg += "pickles\n"
        msg += "quantity: " + str(quan)
        messagebox.showinfo("Order",msg)


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

root.title("Order")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
