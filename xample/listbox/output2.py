# output.py
# This was created by tkautox.py, layout.xlsx and tkauto_tpl.py

from tkinter import *
from tkinter import font
# import requests, sys, os, csv, webbrowser
# from tkinter.filedialog import askopenfilename
# from tkinter import messagebox

class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        self.listv = Listbox(self, height=5)
        self.listv.grid(row=1, column=1 , rowspan=2, sticky=E+W+N+S)

        self.listv.bind("<Double-Button-1>", self.open_path)
        for i in range(100):
            self.listv.insert(i, str(i) + "Item")

        self.scroll = Scrollbar(self, orient=VERTICAL, command=self.listv.yview)
        self.scroll.grid(row=1, column=2 , rowspan=2, sticky=W+N+S)  # use N+S+E
        self.listv['yscrollcommand'] = self.scroll.set

        self.vlbltext = StringVar()
        labelv = Label(self, text='…', textvariable=self.vlbltext)
        labelv.grid(row=3, column=1 , sticky=E+W)

        buttonv = Button(self, text='Select', command=self.on_buttonv_clicked)
        buttonv.grid(row=4, column=1 , sticky=E)

    def on_buttonv_clicked(self):
        self.open_path(None)


    # Handler for List selection
    # Make this a class method
    def open_path(self, event):
        list_item = self.listv.curselection()
        fp = self.listv.get(list_item[0])
        print(str(fp) + " --> " + str(list_item[0]) +
            " of " + str(self.listv.size()))
        self.vlbltext.set(str(fp))  # or self.labelv['text'] = str(fp)


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

root.title("List")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
