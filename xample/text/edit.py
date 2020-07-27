# edit.py
# This was created by tkautox.py, layout.xlsx and tkauto_tpl.py

from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

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

        efont = Font(family="Monospace", size=14)
        self.textv.configure(font=efont)
        self.textv.config(wrap = NONE, # wrap = "word"
               undo = True, # Tk 8.4
               width = 60,
               tabs = (efont.measure(' ' * 4),))
        self.textv.focus()

        self.scry = Scrollbar(self, orient=VERTICAL, command=self.textv.yview)
        self.scry.grid(row=1, column=3 , sticky=E+N+S)  # use N+S+E
        self.textv['yscrollcommand'] = self.scry.set

        self.scrx = Scrollbar(self, orient=HORIZONTAL, command=self.textv.xview)
        self.scrx.grid(row=2, column=1 , columnspan=2, sticky=E+W+N)
        self.textv['xscrollcommand'] = self.scrx.set

        btnSave = Button(self, text='Open', command=self.on_btn_open_clicked)
        btnSave.grid(row=3, column=1 )

        btnClose = Button(self, text='Save', command=self.on_btn_save_clicked)
        btnClose.grid(row=3, column=2 )


    def on_btn_open_clicked(self):
        fname = filedialog.askopenfilename(initialdir = "./",
                    title = "Open Text File",
                    filetypes = (("text files","*.txt"),("all files","*.*")))
        text = ""
        with open(fname, 'r') as f:
            text = f.read()
        print(text)
        self.textv.delete("1.0", END)
        self.textv.insert("1.0", text)

    def on_btn_save_clicked(self):
        fname = filedialog.asksaveasfilename(initialdir = "./",
                    title = "Save file",
                    filetypes = (("text files","*.txt"),("all files","*.*")))
        # file Save follows
        text = self.textv.get(1.0, END)
        with open(fname, "w") as f:
            f.write(text)

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

root.title("Text Editor")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
