from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox

def ministmt():
    d=Tk()
    d.title("Ministatement")
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
   
    b1=Button(d,text='View Statement',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=view)
    b1.grid(row=4,padx=60,pady=10)



def view():
    acc=t1.get()
    p=t2.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from ministmt where acc='"+acc+"'and pin='"+p+"'")
    results=a.fetchall()
    count=a.rowcount
    if(count>0):
        def myfunction(event):
            c.configure(scrollregion=c.bbox("all"),width=1400,height=1000)
        t=Tk()
        t.title("Mini Statement")
        t.geometry("1500x600")
        f3=Frame(t,width=1400,height=600)
        f3.pack(side="top")
        lb1=Label(f3,text="Account Details",font=('Times 15',30,'bold')).grid(row=1,column=2)
        lb1=Label(f3,text="Acc",font=('ariel',15),width=18).grid(row=2,column=0)
        lb1=Label(f3,text="PIN",font=('ariel',15),width=18).grid(row=2,column=1)
        lb1=Label(f3,text="Withdraw",font=('ariel',15),width=18).grid(row=2,column=2)
        lb1=Label(f3,text="Time",font=('ariel',15),width=18).grid(row=2,column=3)
        lb1=Label(f3,text="Deposit",font=('ariel',15),width=20).grid(row=2,column=4)
        lb1=Label(f3,text="Balance",font=('ariel',15),width=18).grid(row=2,column=5) 
        f=Frame(t,width=1500,height=1000)
        f.pack(side="left")

        c=Canvas(f)
        f2=Frame(c)
        scrollbar=Scrollbar(f,orient="vertical",command=c.yview)
        c.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right",fill="y")
        c.pack(padx=90)
               
        c.create_window((0,0),window=f2,anchor='nw')
        f2.bind("<Configure>",myfunction)
    
        j=3
        for i in range(0,count):
            lb1=Label(f2,text=results[i][0],bg='white',width=20,bd=5,font=('times 15',12)).grid(row=j,column=0,pady=10,padx=10)
            lb1=Label(f2,text=results[i][1],bg='white',width=20,bd=5,font=('times 15',12)).grid(row=j,column=1,pady=10,padx=10)
            lb1=Label(f2,text=results[i][2],bg='white',width=20,bd=5,font=('times 15',12)).grid(row=j,column=2,pady=10,padx=10)
            lb1=Label(f2,text=results[i][3],bg='white',width=25,bd=5,font=('times 15',12)).grid(row=j,column=3,pady=10,padx=10)
            lb1=Label(f2,text=results[i][4],bg='white',width=20,bd=5,font=('times 15',12)).grid(row=j,column=4,pady=10,padx=10)
            lb1=Label(f2,text=results[i][5],bg='white',width=20,bd=5,font=('times 15',12)).grid(row=j,column=5,pady=10,padx=10)
            
            j=j+1
         
    else:
        messagebox.showinfo('INFO',"Record Not Found")
