# -*- coding: utf-8 -*-

__author__ = 'Ruslanas Balčiūnas'

from tkinter import *
from widgets import statusbar
import tkinter.messagebox
import sqlite3 as lite
import threading


class Application(Frame):
    def __init__(self, master=None):
        """
        initialize
        """
        self.lock = threading.Lock()

        Frame.__init__(self, master)
        self.pack()

        self.order = StringVar()
        self.order.set("DESC")

        self.toolbar = Frame(self)
        self.search = Entry(self.toolbar)
        self.search_btn = Button(self.toolbar)
        self.radio1 = Radiobutton(self.toolbar, text="Newest top",
                                  variable=self.order, value="DESC",
                                  command=self.loadMessages)
        self.radio2 = Radiobutton(self.toolbar, text="Oldest top",
                                  variable=self.order, value="ASC",
                                  command=self.loadMessages)

        self.frame = Frame(self)
        self.data = []
        self.listbox = Listbox(self.frame, activestyle=NONE)
        self.scrollbar = Scrollbar(self.frame)

        self.text = Entry(self)
        self.add = Button(self)
        self.complete_btn = Button(self)
        self.delete = Button(self)

        self.status_bar = statusbar.StatusBar(self)
        self.status = IntVar()
        self.checkbox = Checkbutton(self, text='Show all',
                                    command=self.loadAsync,
                                    variable=self.status)
        self.important = Button(self,
                                command = lambda : self.set_important('FF0000'),
                                bg="#FF0000",
                                activebackground="#FF0000",
                                padx="5",
                                fg="#FFFFFF")
        self.unimportant = Button(self,
                                command = lambda : self.set_important('000000'),
                                bg="#000000",
                                activebackground="#000000",
                                padx="5",
                                fg="#FFFFFF")

        self.prepareWidgets()

        self.con = lite.connect('mess.db')

    def set_important(self, code):
        with self.con:
            cur = self.con.cursor()
            for i in self.listbox.curselection():
                self.listbox.itemconfig(i, fg='#' + code)
                query = "UPDATE messages SET color = '%s'" \
                        " WHERE id = %d" % (code, self.data[int(i)][0])
                cur.execute(query)

    def taskCompleted(self):
        with self.con:
            cur = self.con.cursor()
            for i in self.listbox.curselection():
                query = 'UPDATE messages SET status = 1' \
                        ' WHERE id = %d' % (self.data[int(i)][0])
                cur.execute(query)

        self.loadAsync()

    def prepareWidgets(self):
        """
        prepare GUI
        :type self: object
        """

        self.toolbar.pack(side=TOP)
        self.toolbar.pack(fill=X)
        self.search.pack(side=LEFT)
        self.search_btn['text'] = 'Filter'
        self.search.bind('<KeyRelease>', lambda x: self.loadMessages())
        self.search_btn['command'] = self.loadMessages
        self.search_btn.pack(side=LEFT)

        self.radio1.pack(side=LEFT)
        self.radio2.pack(side=LEFT)

        self.frame.pack()
        self.listbox.config(width=100)
        self.listbox.pack(side=LEFT, fill='y')

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind('<Delete>', lambda x: self.delete_task())

        self.text.bind('<Return>', lambda x: self.save())
        self.text.pack(fill=X)
        self.text.focus_set()

        self.add['text'] = 'Add task'
        self.add['command'] = self.save
        self.add.config(takefocus=FALSE)
        self.add.pack(side=LEFT)

        self.checkbox.pack(side=LEFT)

        self.important['text'] = ' '
        self.important.pack(side=RIGHT)

        self.unimportant['text'] = ' '
        self.unimportant.pack(side=RIGHT)

        self.complete_btn['text'] = 'Completed'
        self.complete_btn['command'] = self.taskCompleted
        self.complete_btn.pack(side=RIGHT)

        self.delete['text'] = 'Delete selected'
        self.delete['command'] = self.delete_task
        self.delete.config(takefocus=FALSE)
        self.delete.pack(side=RIGHT)

        self.status_bar.pack(fill=X, side=RIGHT)

        self.loadAsync()

    def delete_task(self):

        if not tkinter.messagebox.askyesno('Delete task',
                                           'Do you want to delete task?'):
            return

        with self.con:
            cur = self.con.cursor()
            for i in self.listbox.curselection():
                query = 'DELETE FROM messages' \
                        ' WHERE id = %d' % (self.data[int(i)][0])
                cur.execute(query)

        self.text.focus_set()

        self.loadAsync()

    def clearMessages(self):
        self.listbox.delete(0, END)

    def loadAsync(self):
        self.status_bar.set('Loading...')
        thread = BackgroundThread(self.loadMessages, self.lock)
        thread.start()

    def loadMessages(self):

        self.clearMessages()

        con = lite.connect('mess.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM sqlite_master"
                        " WHERE type='table' AND name='messages'")

            data = cur.fetchone()

            if data[0]:
                # default get not done
                query = "SELECT id, created, message, status, color" \
                        " FROM messages" \
                        " WHERE NOT status AND message LIKE '%' || ? || '%'" \
                        " ORDER BY created " + self.order.get()

                if self.status.get():
                    query = "SELECT id, created, message, status, color" \
                            " FROM messages" \
                            " WHERE message LIKE '%' || ? || '%'" \
                            " ORDER BY created " + self.order.get()

                cur.execute(query, (self.search.get(),))
                self.data = cur.fetchall()

        con.close()

        # add timestamp
        for (i, line) in enumerate(self.data):
            self.listbox.insert(END, '%s %s' % (line[1][0:-3], line[2]))
            if line[3]:
                self.listbox.itemconfig(i, fg='#CCCCCC')
            else:
                self.listbox.itemconfig(i, fg="#" + line[4])

        self.status_bar.set(str(len(self.data)) + ' tasks.')

    def save(self):

        query = "INSERT INTO messages (message) VALUES (?)"

        with self.con:
            prefix = ''
            # add current tag
            if len(self.search.get()) and self.search.get()[0] == '#':
                prefix = self.search.get()

            msg = prefix + ' ' + self.text.get()
            cur = self.con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS"
                        " messages (id INTEGER PRIMARY KEY,"
                        " completed BOOL DEFAULT 0,"
                        " color VARCHAR(6) DEFAULT '000000',"
                        " status bool DEFAULT 0,"
                        " priority INT DEFAULT 0,"
                        " deadline DATETIME,"
                        " message VARCHAR(128),"
                        " created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

            cur.execute(query, (msg,))

        self.text.delete(0, END)
        self.loadAsync()


class BackgroundThread(threading.Thread):
    def __init__(self, func, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        self.func = func

    def run(self):
        if self.lock.acquire(False):
            try:
                self.func()
            finally:
                self.lock.release()


if __name__ == '__main__':
    root = Tk()
    root.title('Mess')
    root.iconbitmap(default='mess.ico')
    root.resizable(width=FALSE, height=FALSE)
    root.wm_attributes('-topmost', 1)
    app = Application(master=root)
    app.mainloop()