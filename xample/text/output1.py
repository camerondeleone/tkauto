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

        self.textv = Text(self, relief=SUNKEN)
        self.textv.grid(row=1, column=1 , columnspan=2, sticky=E+W)

        # efont = Font(family="Monospace", size=14)
        # self.editor.configure(font=efont)
        # self.editor.config(wrap = "word", # wrap = NONE
        #        undo = True, # Tk 8.4
        #        width = 80,
        #        tabs = (efont.measure(' ' * 4),))
        # self.editor.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")


        btnSave = Button(self, text='Save', command=self.on_btnSave_clicked)
        btnSave.grid(row=2, column=1 )

        btnClose = Button(self, text='Close', command=self.on_btnClose_clicked)
        btnClose.grid(row=2, column=2 )

    def on_btnSave_clicked(self):
        text = self.textv.get(1.0, END)
        print(text)

    def on_btnClose_clicked(self):
        root.destroy()



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

root.title("output")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
