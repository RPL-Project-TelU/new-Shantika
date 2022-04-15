from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import * 
import sqlite3

def mainprogram():
    #splash_screen

    root1=Tk()
    root1.iconbitmap('pp.ico')
    root1.geometry('2000x900')
    root1.configure(background='#454445')
    root1.title('Project Developer Details')
    Label(root1,text='Project Title: Bus Booking System',fg='#FFC300',font=('Arial 20 bold',50),background='#454445').grid(row=0,column=0)
    Label(root1,text=' Advanced Programming ',fg='#15DAC1',font='Arial 20 bold',background='#454445').grid(row=1,column=0)
    Label(root1,text='',fg='red',font='Arial 20 bold',background='#454445').grid(row=2,column=0)
    Label(root1,text='-------------------------------------------------',fg='yellow',font='Arial 20 bold',background='#454445').grid(row=3,column=0)
    Label(root1,text='',fg='#15DAC1',font='Arial 20 bold',background='#454445').grid(row=4,column=0)
    Label(root1,text='Double Click on the screen to enter the Project',fg='Green',font='Arial 20 bold',background='#454445').grid(row=5,column=0,pady=150)

    #bind function for splash screen
    def close(e):
        root1.destroy()
    root1.bind('<Double 1>', close)
    root1.mainloop()


    #main screen of program
    root=Tk()
    root.configure(background='black')
    root.geometry('2000x900')
    root.title('Aplikasi Pemesanan Bus New Shantika')
    root.iconbitmap('bus.ico')

    my_img=Image.open("banner.png")
    image=my_img.resize((700,250),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(image)
    
    my_label=Label(image=img).place(relx=0.5,rely=0.1,anchor=CENTER)
    lb1=Label(root,text='NEW SHANTIKA BUS BOOKING SERVICE',fg='red',relief=SUNKEN,font=('Times',30),background="#2E2E03")
    lb1.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    conn = sqlite3.connect('busdatabase.db')
    c = conn.cursor()
    c.execute(
    "CREATE Table IF NOT EXISTS buses1(OPERATOR text,BUS_TYPE text,D_FROM text,A_TO text,DATE text,DEP_TIME text,ARR_TIME text,FARE integer,SEATS integer)")
    conn.commit()

    def cbtn1():
        
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
        def cb2():
            op=Tk()
            def update():
                conn = sqlite3.connect('busdatabase.db')
                c = conn.cursor()
                c.execute('UPDATE buses1 SET SEATS = SEATS - 1 WHERE OPERATOR = ?',(ID,))
                conn.commit()
                messagebox.showinfo("BUS", "SEAT BOOKED") 
                
            an=p.get()
            bn=q.get()
            cn=r.get()
            if an==' ' or bn==' ' or cn==' ':
                Tk.MessageBox.showerror("OOPS","Some Details are Missing")
            else:
                conn = sqlite3.connect('busdatabase.db')
                c = conn.cursor()
                c.execute("SELECT * FROM buses1 WHERE D_FROM= ? AND A_TO = ?  ",(an,bn))
                conn.commit()
                ro=c.fetchall()
                radio = IntVar()
                #sea = IntVar()
                row=6
                column=2
                for i in ro:
                    rad = Radiobutton(op,value = i, variable = radio)
                    rad.pack(side=LEFT)
                    for j in i:
                        qwerty=Label(op,text=j ,fg="black")
                        qwerty.pack(padx=5,pady=20,side=LEFT)
                    column=column+3
                    row=row+1
                ID = ro[radio.get()][0]
                b1 = Button(op,text = 'BOOK NOW',command = update)
                b1.pack(side = BOTTOM)
                
                print(ro)
                conn.close()
            op.mainloop()
        b1 = Button(m,cursor="hand2", text="EXIT", fg="Blue", font=("bold", 15), height=1, width=10, command=m.destroy).grid(column=0, row=20,padx=10)
        b2 = Button(m,cursor="hand2", text="SEARCH", fg="Blue", font=("bold", 15), height=1, width=10,command=cb2).grid(column=4, row=20)
        m.resizable(False,False)
        m.mainloop()

    btn1 = Button(root,cursor="hand2", text="SEARCH BUS", fg="Brown", font=("bold", 15), height=1, width=10, command=cbtn1)
    btn1.place(relx=0.92,rely=0.6,width=150,anchor=E)
    root.tk_setPalette('#E6DB74')
    conn.commit()
    conn.close()