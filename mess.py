# -*- coding: utf-8 -*-
__author__ = 'Ruslanas Balčiūnas'

from tkinter import *
import sqlite3 as lite

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        frame = Frame(self)
        frame.pack()
        self.data = []
        self.listbox = Listbox(frame)
        self.scrollbar = Scrollbar(frame)

        self.menubar = Menu(self)

        self.text = Entry(self)
        self.add = Button(self)
        self.complete_btn = Button(self)
        self.delete = Button(self)

        self.prepareWidgets()

    def taskCompleted(self):
        con = lite.connect('mess.db')
        with con:
            cur = con.cursor()
            for i in self.listbox.curselection():
                query = 'UPDATE messages SET status = 1 WHERE id = %d' % (self.data[int(i)][0])
                cur.execute(query)

        con.close()
        self.loadMessages()

    def prepareWidgets(self):
        """
        create GUI widgets
        """

        self.menubar.add_command(label='Database')
        self.menubar.add_command(label='About')

        self.listbox.config(width=60)
        self.listbox.pack(side=LEFT, fill='y')

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind('<Delete>', lambda x: self.deleteMessage())

        self.text.bind('<Return>', lambda x: self.save())
        self.text.pack(fill=X)
        self.text.focus_set()

        self.add['text'] = 'Add task'
        self.add['command'] = self.save
        self.add.config(takefocus=FALSE)
        self.add.pack(side=LEFT)

        self.status = IntVar()
        self.checkbox = Checkbutton(self, text='Show all',
                                    command=self.loadMessages,
                                    variable=self.status)
        self.checkbox.pack(side=LEFT)

        self.complete_btn['text'] = 'Done'
        self.complete_btn['command'] = self.taskCompleted
        self.complete_btn.pack(side=RIGHT)

        self.delete['text'] = 'Delete selected'
        self.delete['command'] = self.deleteMessage
        self.delete.config(takefocus=FALSE)
        self.delete.pack(side=RIGHT)

        self.loadMessages()

    def deleteMessage(self):
        con = lite.connect('mess.db')
        with con:
            cur = con.cursor()
            for i in self.listbox.curselection():
                query = 'DELETE FROM messages WHERE id = %d' % (self.data[int(i)][0])
                cur.execute(query)
        con.close()
        self.text.focus_set()
        self.loadMessages()

    def clearMessages(self):
        self.listbox.delete(0, END)

    def loadMessages(self):
        self.clearMessages()

        con = lite.connect('mess.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM sqlite_master"
                        " WHERE type='table' AND name='messages'")

            data = cur.fetchone()

            if data[0]:
                query = 'SELECT id, created, message FROM messages WHERE NOT status'
                if self.status.get():
                    query = 'SELECT id, created, message FROM messages'

                cur.execute(query)
                self.data = cur.fetchall()

        con.close()

        for line in self.data:
            self.listbox.insert(END, '%s - %s' % (line[1], line[2]))

    def save(self):

        query = "INSERT INTO messages (message) VALUES ('" + self.text.get() + "')"
        con = lite.connect('mess.db')

        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS"
                        " messages (id INTEGER PRIMARY KEY, completed BOOL DEFAULT 0,"
                        " status bool DEFAULT 0, priority INT DEFAULT 0,"
                        " message VARCHAR(128), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            cur.execute(query)

        con.close()
        self.text.delete(0, END)
        self.loadMessages()

root = Tk()
root.title('Mess')
root.iconbitmap(default='mess.ico')
root.resizable(width=FALSE, height=FALSE)
root.wm_attributes('-topmost', 1)
#root.wm_overrideredirect(TRUE)
app = Application(master=root)
root.config(menu=app.menubar)
app.mainloop()