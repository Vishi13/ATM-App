from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox

def checkbalance():
    d=Tk()
    d.title("Balance Enquiry")
    d.resizable(False,False)
    d.geometry("500x220")
    l1=Label(d,text='Account No.')
    l1.grid(row=1,column=0,pady=10)
    global t1
    num1=StringVar()
    t1=Entry(d,width=25,textvariable=num1)
    t1.grid(row=1,column=1,padx=10,pady=10)

    l2=Label(d,text='PIN')
    l2.grid(row=2,column=0,pady=10)
    global t2
    num2=StringVar()
    t2=Entry(d,width=25,textvariable=num2)
    t2.grid(row=2,column=1,padx=10,pady=10)    
   
    b1=Button(d,text='Check Balance',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=check)
    b1.grid(row=3,padx=60,pady=10)


def check():
    acc=t1.get()
    p=t2.get()
    
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
    results=a.fetchone()
    count=a.rowcount
    if(count>0):
        x="Your Balance is"
        y=str(results[0])
        z=x+" "+y
        messagebox.showinfo('INFO',z)
    else:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()    
