from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button=Button(self,text='点击',command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup',message='button pressed')

if __name__=='__main__':
    window=MyGui()
    window.pack()
    window.mainloop()
