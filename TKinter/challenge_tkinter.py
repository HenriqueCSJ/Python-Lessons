# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

# 6 linhas por 4 colunas

import tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Tkinter Calculator")
mainWindow.geometry("200x300")
mainWindow["padx"] = 8
mainWindow["pady"] = 8

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

# Display
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky="nwe")

# C and CE buttons

cButton = tkinter.Button(mainWindow, text="C")
cButton.grid(row=1, column=0, sticky="nesw")
ceButton = tkinter.Button(mainWindow, text="CE")
ceButton.grid(row=1, column=1, sticky="nswe")

# 7, 8, 9, + buttons
_7Button = tkinter.Button(mainWindow, text="7")
_8Button = tkinter.Button(mainWindow, text="8")
_9Button = tkinter.Button(mainWindow, text="9")
plusButton = tkinter.Button(mainWindow, text="+")
_7Button.grid(row=2, column=0, sticky="nswe")
_8Button.grid(row=2, column=1, sticky="nswe")
_9Button.grid(row=2, column=2, sticky="nswe")
plusButton.grid(row=2, column=3, sticky="nswe")

# 4, 5, 6, -
_4Button = tkinter.Button(mainWindow, text="4")
_5Button = tkinter.Button(mainWindow, text="5")
_6Button = tkinter.Button(mainWindow, text="6")
minusButton = tkinter.Button(mainWindow, text="-")
_4Button.grid(row=3, column=0, sticky="nswe")
_5Button.grid(row=3, column=1, sticky="nswe")
_6Button.grid(row=3, column=2, sticky="nswe")
minusButton.grid(row=3, column=3, sticky="nswe")

# 1, 2, 3, *
_1Button = tkinter.Button(mainWindow, text="1")
_2Button = tkinter.Button(mainWindow, text="2")
_3Button = tkinter.Button(mainWindow, text="3")
timesButton = tkinter.Button(mainWindow, text="*")
_1Button.grid(row=4, column=0, sticky="nswe")
_2Button.grid(row=4, column=1, sticky="nswe")
_3Button.grid(row=4, column=2, sticky="nswe")
timesButton.grid(row=4, column=3, sticky="nswe")

# 0, =, /
_0Button = tkinter.Button(mainWindow, text="0")
equalButton = tkinter.Button(mainWindow, text="=")
divisionButton = tkinter.Button(mainWindow, text="/")
_0Button.grid(row=5, column=0, sticky="nswe")
equalButton.grid(row=5, column=1, columnspan=2, sticky="nswe")
divisionButton.grid(row=5, column=3, sticky="nswe")


mainWindow.mainloop()

















