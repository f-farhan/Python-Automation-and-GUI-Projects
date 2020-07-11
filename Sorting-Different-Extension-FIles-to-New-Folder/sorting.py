import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("File Sorting")
Tops = Frame(root, width=1600, relief=SUNKEN)



def callback1():
    path = filedialog.askdirectory()
    list_ = os.listdir(path)
    
    for file_ in list_:
        name, extnsn = os.path.splitext(file_)


        extnsn = extnsn[1:]

        # This forces the next iteration,
        # if it is the directory
        if extnsn == '':
            continue

        # This will move the file to the directory
        # where the name 'ext' already exists
        if os.path.exists(path + '/' + extnsn):
            shutil.move(path + '/' + file_, path + '/' + extnsn + '/' + file_)

            # This will create a new directory,
        # if the directory does not already exist
        else:
            os.makedirs(path + '/' + extnsn)
            shutil.move(path + '/' + file_, path + '/' + extnsn + '/' + file_)






button = ttk.Button(root, text='Sort')
labltitle = ttk.Label(text='Automatic File Sorting', font=(('Times'), 22))
lablname = ttk.Label(text='Select directory', font=(('Arial'), 15))
labltitle.grid(row=0, column=1, columnspan=2)
lablname.grid(row=1, column=0, sticky=W)
button.grid(row=1, column=1)
chvar = IntVar()
chvar.set(0)
button.config(command=callback1)

root.geometry('500x450')
root.mainloop()
