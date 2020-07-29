'''
tkauto_tpl.py
Used with tkauto.py and tkmenu.py
'''

from tkinter import *
from tkinter.ttk import Combobox, LabelFrame
# from tkinter.font import Font
# import requests, sys, os, csv, webbrowser
# from tkinter.filedialog import askopenfilename
# from tkinter import messagebox

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        lframe = LabelFrame(self, text="Combobox",
                            width=100, height=100)
        lframe.grid(row=1, column=1, sticky=N+S+E+W)

        self.cbov = StringVar()
        cbox = Combobox(lframe, textvariable=self.cbov)
        cbox['values'] = ('value1', 'value2', 'value3')
        # COMBO.bind('<<ComboboxSelected>>', self.ONCOMBOSELECT)
        cbox.current(0)
        cbox.grid(row=1, column=1 , sticky=E+W, padx=10, pady=20)


        # lframe = LabelFrame(self, text="text",
        #                     width=100, height=100)
        # lframe.grid(row=1, column=1, sticky=N+S+E+W)
        #
        # fram = Frame(self, width=100, height=100)
        # fram.grid(row=1, column=1, sticky=N+S+E+W)




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
#   or the following:
#   the following repositions the window from last time '''
# if os.path.isfile("winfoxy"):
#     lcoor = tuple(open("winfoxy", 'r'))  # no relative path for this
#     root.geometry('350x200+%d+%d'%(int(lcoor[0].strip()),int(lcoor[1].strip())))
# else:
#     root.geometry("350x200") # WxH+left+top

root.title("ttk")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
