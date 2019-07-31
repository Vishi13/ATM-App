from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox

def createacc():
    d=Tk()
    d.title("Create Account")
    d.resizable(False,False)
    d.geometry("500x250")
    l1=Label(d,text='Name')
    l1.grid(row=1,column=0,pady=10)
    global t1
    name=StringVar()
    t1=Entry(d,width=25,textvariable=name)
    t1.grid(row=1,column=1,padx=10,pady=10)
    
    l2=Label(d,text='Account No.')
    l2.grid(row=2,column=0,pady=10)
    global t2
    num1=StringVar()
    t2=Entry(d,width=25,textvariable=num1)
    t2.grid(row=2,column=1,padx=10,pady=10)

    l3=Label(d,text='PIN')
    l3.grid(row=3,column=0,pady=10)
    global t3
    num=StringVar()
    t3=Entry(d,width=25,textvariable=num)
    t3.grid(row=3,column=1,padx=10,pady=10)

    l4=Label(d,text='Initial Amount')
    l4.grid(row=4,column=0,pady=10)
    global t4
    num4=StringVar()
    t4=Entry(d,width=25,textvariable=num4)
    t4.grid(row=4,column=1,padx=10,pady=10)
   
    b1=Button(d,text='Create',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=create)
    b1.grid(row=5,padx=60,pady=10)


def create():
    nam=t1.get()
    acc=t2.get()
    p=t3.get()
    amt=t4.get()
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("insert into atmdetails(accno,name,pin,balance) values('"+acc+"','"+nam+"','"+p+"','"+amt+"')")  
        conn.commit()
        messagebox.showinfo('INFO','Account Created')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','Account Not Created')
    conn.close()
