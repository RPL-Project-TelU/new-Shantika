from tkinter import * 
from tkcalendar import * 
import sqlite3
btn = Button(root, cursor="hand2", text="ADD BUS",fg="brown",font=("bold", 15), height=1, width=10, command=clibtn)

btn.place(relx=0.1,rely=0.6,anchor=W)

def btn1():
        
    m = Tk()
    Label(m, text="SEARCH BUS", font=("arial bold red", 20),fg="Black").grid(column=1, row=0)
    m.geometry('600x500')

    lb1 = Label(m, text="BUS TYPE").grid(column=0, row=4)
    V = StringVar(m)

    clicked = StringVar()
    clicked.set("AC")
    bustype = OptionMenu(m,clicked,'AC', 'NON-AC', 'AC-SLEEPER', 'DOUBLE-DECKER', 'NON-AC SLEEPER', 'ALL TYPE').grid(column=4, row=4,pady=10)
    lb2 = Label(m, text="FROM").grid(column=0,row=5,pady=10)
    p = Entry(m)
    p.grid(column=4, row=5,pady=10)
    lb3 = Label(m, text="TO").grid(column=0, row=6,pady=10)
    q = Entry(m)
    q.grid(column=4, row=6,pady=10)
    lb4 = Label(m, text="DATE").grid(column=0, row=7,pady=10)
    r = Entry(m)
    r.grid(column=4, row=7,pady=10)