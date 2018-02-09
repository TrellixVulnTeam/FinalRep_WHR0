# import Tkinter
import sys

print(sys.version)
print(sys.executable)
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import tkinter.filedialog

pad = tkinter.Tk()  # creates new GUI and all code between here and pad.mainloop() control that GUI
textPad = tkst.ScrolledText(pad, width=100, height=80)


# Menu functions

# Open function

def open_command():
    file = filedialog.askopenfile(parent=pad, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

    # Save file


def fuckPython():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()

    # create quiz


dicktickler = {}
"""side note about this function: it won't display the text in the editor when you open it but it does open it """

c = 0
def quiz():

    file = filedialog.askopenfile(parent=pad, mode='r', title='Select a file')
    if file != None:
        for i, line in enumerate(file):
            if '#' and ':' in line:
                dicktickler[str(line[line.index("#") + 1: line.index(':')])] = line[line.index(':') + 1:]
                print(i, line)
    print(dicktickler) # This is just for us to see if it is still working correctly


    flash = tkinter.Tk() # create new GUI for flash card interface
    Label(flash, text="Flash Cards").grid(column=1, row=0)
    Label(flash, text=list(dicktickler.keys())[c], padx=100, pady=100).grid(column=1, row=1)
    def back():
        global c
        c -= 1
        Label(flash, text=list(dicktickler.keys())[c], padx=100, pady=100).grid(column=1, row=1)
        return c

    def next():
        try:
            global c
            c += 1
            Label(flash, text=list(dicktickler.keys())[c], padx=100, pady=100).grid(column=1, row=1)
            return c
        except:
            c = 0
            Label(flash, text=list(dicktickler.keys())[c], padx=100, pady=100).grid(column=1, row=1)
            return c

    Button(flash, text="Next", command=next).grid(column=2, row=3)
    Button(flash, text="Back", command=back).grid(column=0, row=3)


    flash.mainloop()

def exit_command():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        pad.destroy()


def about_command():
    label = messagebox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")


def dummy():
    print("I am a Dummy Command, I will be removed in the next step")


menu = Menu(pad)
pad.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Create Quiz", command=quiz)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=fuckPython)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
textPad.pack()

pad.mainloop()