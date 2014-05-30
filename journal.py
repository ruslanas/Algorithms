# -*- coding: utf-8 -*-
__author__ = 'Ruslanas Balčiūnas'

from tkinter import *
from time import strftime
import os.path

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        frame = Frame(self)
        frame.pack()
        self.listbox = Listbox(frame)
        self.scrollbar = Scrollbar(frame)

        self.text = Entry(self)
        self.add = Button(self)
        self.delete = Button(self)

        self.prepareWidgets()

    def prepareWidgets(self):
        """
        create GUI widgets
        """
        self.listbox.config(width=100)
        self.listbox.pack(side=LEFT, fill='y')

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.text.bind('<Return>', lambda x: self.save())
        self.text.pack(fill=X)

        self.add['text'] = 'Add note'
        self.add['command'] = self.save
        self.add.pack(side='left')

        self.delete['text'] = 'Delete selected'
        self.delete['command'] = self.deleteMessage
        self.delete.pack(side='left')

        self.loadMessages()

    def deleteMessage(self):
        for i in self.listbox.curselection():
            print(i)
            self.listbox.delete(i)

    def clearMessages(self):
        self.listbox.delete(0, END)

    def loadMessages(self):
        self.clearMessages()
        if os.path.isfile('applications.dat'):
            f = open('applications.dat', 'r')
            lines = f.readlines()
            for line in lines:
                self.listbox.insert(END, line)
            f.close()

    def save(self):
        f = open('applications.dat', 'a')
        t = strftime('%Y-%m-%d %H:%M:%S')
        msg = '%s %s' % (t, self.text.get())
        f.write(msg + '\n')
        f.close()
        self.text.delete(0, END)
        self.loadMessages()

root = Tk()
root.title('Journal')
root.wm_attributes('-topmost', 1)
app = Application(master=root)
app.mainloop()