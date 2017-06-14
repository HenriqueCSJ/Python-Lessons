# import time

# print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))

# print("The current timezone is {0} with an offset of {1}.".format(time.tzname[0], time.timezone))

# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])

# print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print("The UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
# -----------------

# import datetime

# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('starttime', 'endtime', 'status')
        tv.heading("#0", text='Sources', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='Start Time')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='End Time')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='Status')
        tv.column('status', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()