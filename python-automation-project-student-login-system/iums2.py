from tkinter import *
from tkinter import ttk
from selenium import webdriver
from bs4 import BeautifulSoup

root = Tk()
def callback():
    usr = entry.get()
    pwd = entry2.get()
    driver = webdriver.Chrome()
    driver.get('https://iums.aust.edu/ums-web/login/')
    username_box = driver.find_element_by_id('userName')
    username_box.send_keys(usr)
    password_box = driver.find_element_by_id('password')
    password_box.send_keys(pwd)
    login_box = driver.find_element_by_id('login_btn')
    login_box.click()

entry=ttk.Entry(root,width=30)
entry2=ttk.Entry(root,width=30)
entry.insert(0,'Please enter name')
entry2.insert(0,'')
button=ttk.Button(root,text='Enter')
labltitle=ttk.Label(text='AUST IUMS',font=(('Times'),22))
lablname=ttk.Label(text='Name',font=(('Arial'),15))
lablpass=ttk.Label(text='Password',font=(('Arial'),15))
labltitle.grid(row=0,column=1,columnspan=2)
lablname.grid(row=1,column=0,sticky=W)
lablpass.grid(row=2,column=0)
entry2.config(show='*')
entry.grid(row=1,column=1)
entry2.grid(row=2,column=1)
button.grid(row=3,column=1,sticky=E,pady=5)
chvar=IntVar()
chvar.set(0)
button.config(command=callback)


root.geometry('500x450')
root.mainloop()
