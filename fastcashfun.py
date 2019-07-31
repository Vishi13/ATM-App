from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox

def fastcash():
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

    l2=Label(d,text='PIN')
    l2.grid(row=2,column=0,pady=10)
    global t2
    num2=StringVar()
    t2=Entry(d,width=25,textvariable=num2)
    t2.grid(row=2,column=1,padx=10,pady=10)
   
    b1=Button(d,text='200',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=two)
    b1.grid(row=3,padx=50,pady=10)

    b2=Button(d,text='500',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=five)
    b2.grid(row=3,column=2,pady=10)

    b3=Button(d,text='1000',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=oneth)
    b3.grid(row=4,padx=50,pady=10)

    b4=Button(d,text='5000',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=fiveth)
    b4.grid(row=4,column=2,pady=10)

def two():
    acc=t1.get()
    p=t2.get()
    amt=200
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
        results=a.fetchone()
        if(int(results[0])>=amt):
            fbal=int(results[0])-int(amt)
            a.execute("update atmdetails set balance='"+str(fbal)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time,balance)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"','"+str(fbal)+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT WITHDRAWN')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()


def five():
    acc=t1.get()
    p=t2.get()
    amt=500
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
        results=a.fetchone()
        print(int(results[0]))
        if(int(results[0])>=int(amt)):
            fbal=int(results[0])-int(amt)
            a.execute("update atmdetails set balance='"+str(fbal)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time,balance)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"','"+str(fbal)+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT WITHDRAWN')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()


def oneth():
    acc=t1.get()
    p=t2.get()
    amt=1000
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
        results=a.fetchone()
        print(int(results[0]))
        if(int(results[0])>=int(amt)):
            fbal=int(results[0])-int(amt)
            a.execute("update atmdetails set balance='"+str(fbal)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time,balance)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"','"+str(fbal)+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT WITHDRAWN')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()


def fiveth():
    acc=t1.get()
    p=t2.get()
    amt=5000
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
        results=a.fetchone()
        print(int(results[0]))
        if(int(results[0])>=int(amt)):
            fbal=int(results[0])-int(amt)
            a.execute("update atmdetails set balance='"+str(fbal)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time,balance)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"','"+str(fbal)+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT WITHDRAWN')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()
