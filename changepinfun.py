from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox

def changepin():
    d=Tk()
    d.title("Fast Cash")
    d.resizable(False,False)
    d.geometry("500x200")
    l1=Label(d,text='Account No.')
    l1.grid(row=1,column=0,pady=10)
    global t1
    num1=StringVar()
    t1=Entry(d,width=25,textvariable=num1)
    t1.grid(row=1,column=1,padx=10,pady=10)

    l2=Label(d,text='Old PIN')
    l2.grid(row=2,column=0,pady=10)
    global t2
    num2=StringVar()
    t2=Entry(d,width=25,textvariable=num2)
    t2.grid(row=2,column=1,padx=10,pady=10)

    l3=Label(d,text='New PIN')
    l3.grid(row=3,column=0,pady=10)
    global t3
    num=StringVar()
    t3=Entry(d,width=25,textvariable=num)
    t3.grid(row=3,column=1,padx=10,pady=10)
   
    b1=Button(d,text='Change',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=change)
    b1.grid(row=4,padx=60,pady=10)
    


def change():
    acc1=t1.get()
    p=t2.get()
    q=t3.get()
    
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from atmdetails where accno='"+acc1+"'and pin='"+p+"'")
    if(a.rowcount>0):
        a.execute("update atmdetails set pin='"+q+"'where accno='"+acc1+"'and pin='"+p+"'")
        a.execute("update ministmt set pin='"+q+"'where acc='"+acc1+"'and pin='"+p+"'")  
        conn.commit()
        messagebox.showinfo('INFO','PIN Updated')
    else:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()
