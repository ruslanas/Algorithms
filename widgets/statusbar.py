__author__ = 'Ruslanas'

from tkinter import *

class StatusBar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.status = Entry(self)
        self.status.pack(fill='x')
        self.status.insert(0, '')

    def set(self, msg):
        self.status.config(state=NORMAL)
        self.status.delete(0, END)
        self.status.insert(END, msg)
        self.status.config(state=DISABLED)
