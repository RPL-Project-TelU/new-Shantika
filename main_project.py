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