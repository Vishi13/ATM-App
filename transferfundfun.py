from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox

def transferfund():
    d=Tk()
    d.title("Transfer Fund")
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

    l3=Label(d,text='Amount')
    l3.grid(row=3,column=0,pady=10)
    global t3
    num=StringVar()
    t3=Entry(d,width=25,textvariable=num)
    t3.grid(row=3,column=1,padx=10,pady=10)
    
    l4=Label(d,text='Transfer into(acc no.)')
    l4.grid(row=4,column=0,pady=10)
    global t4
    num4=StringVar()
    t4=Entry(d,width=25,textvariable=num4)
    t4.grid(row=4,column=1,padx=10,pady=10)    
   
    b1=Button(d,text='Transfer',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=transfer)
    b1.grid(row=5,padx=60,pady=10)


def transfer():
    acc=t1.get()
    p=t2.get()
    amt=t3.get()
    acc2=t4.get()
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
        results=a.fetchone()
        if(int(results[0])>=int(amt)):
            fwith=int(results[0])-int(amt)
            fdepo=int(results[0])+int(amt)
            a.execute("update atmdetails set balance='"+str(fwith)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("update atmdetails set balance='"+str(fdepo)+"'where accno='"+acc2+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time,balance)values('"+acc+"','"+p+"','"+amt+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"','"+str(fwith)+"')")
            a.execute("insert into ministmt (acc,pin,deposit,time,balance)values('"+acc2+"','"+p+"','"+amt+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"','"+str(fdepo)+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT TRANSFERRED')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()
