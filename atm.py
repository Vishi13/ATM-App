from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox



def deposit():
    d=Tk()
    d.title("Deposit Cash")
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

    l3=Label(d,text='Amount')
    l3.grid(row=3,column=0,pady=10)
    global t3
    num=StringVar()
    t3=Entry(d,width=25,textvariable=num)
    t3.grid(row=3,column=1,padx=10,pady=10)
   
    b1=Button(d,text='DepositCash',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=depositcash)
    b1.grid(row=4,padx=60,pady=10)


def depositcash():
    acc=t1.get()
    p=t2.get()
    amt=t3.get()
    
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from atmdetails where accno='"+acc+"'and pin='"+p+"'")
    if(a.rowcount>0):
        a.execute("update atmdetails set balance=balance+'"+amt+"'where accno='"+acc+"'and pin='"+p+"'")
        a.execute("insert into ministmt (acc,pin,deposit,time)values('"+acc+"','"+p+"','"+amt+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
        conn.commit()
        messagebox.showinfo('INFO','Amount Deposited')
    else:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()
        



def withdraw():
    d=Tk()
    d.title("Withdraw Cash")
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

    l3=Label(d,text='Amount')
    l3.grid(row=3,column=0,pady=10)
    global t3
    num=StringVar()
    t3=Entry(d,width=25,textvariable=num)
    t3.grid(row=3,column=1,padx=10,pady=10)
   
    b1=Button(d,text='WithdrawCash',bd=4,font=('ariel',14,'bold'),relief='groove',activebackground='pink',command=withdrawcash)
    b1.grid(row=4,padx=60,pady=10)



def withdrawcash():
    acc=t1.get()
    p=t2.get()
    amt=t3.get()
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select balance from atmdetails where accno='"+acc+"'and pin='"+p+"'")
        results=a.fetchone()
        if(int(results[0])>=int(amt)):
            a.execute("update atmdetails set balance=balance-'"+amt+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time)values('"+acc+"','"+p+"','"+amt+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT WITHDRAWN')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()
    


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
        t.geometry("1400x600")
        f3=Frame(t,width=1400,height=600)
        f3.pack(side="top")
        lb1=Label(f3,text="Account Details",font=('Times 15',30,'bold')).grid(row=1,column=2)
        lb1=Label(f3,text="Acc",font=('ariel',15),width=20).grid(row=2,column=0)
        lb1=Label(f3,text="PIN",font=('ariel',15),width=20).grid(row=2,column=1)
        lb1=Label(f3,text="Deposit",font=('ariel',15),width=20).grid(row=2,column=2)
        lb1=Label(f3,text="Time",font=('ariel',15),width=20).grid(row=2,column=3)
        lb1=Label(f3,text="Withdraw",font=('ariel',15),width=20).grid(row=2,column=4)
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
            lb1=Label(f2,text=results[i][0],bg='white',width=32,bd=5).grid(row=j,column=0,pady=10,padx=10)
            lb1=Label(f2,text=results[i][1],bg='white',width=32,bd=5).grid(row=j,column=1,pady=10,padx=10)
            lb1=Label(f2,text=results[i][2],bg='white',width=32,bd=5).grid(row=j,column=2,pady=10,padx=10)
            lb1=Label(f2,text=results[i][3],bg='white',width=32,bd=5).grid(row=j,column=3,pady=10,padx=10)
            lb1=Label(f2,text=results[i][4],bg='white',width=32,bd=5).grid(row=j,column=4,pady=10,padx=10)
            
            j=j+1
         
    else:
        messagebox.showinfo('INFO',"Record Not Found")
              
    
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
            a.execute("update atmdetails set balance=balance-'"+amt+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("update atmdetails set balance=balance+'"+amt+"'where accno='"+acc2+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time)values('"+acc+"','"+p+"','"+amt+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
            a.execute("insert into ministmt (acc,pin,deposit,time)values('"+acc2+"','"+p+"','"+amt+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT TRANSFERRED')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()


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
        print(int(results[0]))
        if(int(results[0])>=amt):
            a.execute("update atmdetails set balance=balance-'"+str(amt)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
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
            a.execute("update atmdetails set balance=balance-'"+str(amt)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
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
            a.execute("update atmdetails set balance=balance-'"+str(amt)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
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
            a.execute("update atmdetails set balance=balance-'"+str(amt)+"'where accno='"+acc+"'and pin='"+p+"'")
            a.execute("insert into ministmt (acc,pin,withdraw,time)values('"+acc+"','"+p+"','"+str(amt)+"','"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"')")
            conn.commit()
            messagebox.showinfo('INFO','AMT WITHDRAWN')
        else:
            messagebox.showinfo('INFO','INSUFFICIENT BALANCE')
    except:
        conn.rollback()
        messagebox.showinfo('INFO','INVALID ACCCNO OR PIN')
    conn.close()



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





win=Tk()
win.title("ATM Application")
win.config(bg="Cyan")
win.geometry("600x600")
win.resizable(False,False)

f=Frame(win,width=500,height=150,bd=8,relief='sunken',bg='pink',cursor='dot',highlightcolor='blue').grid(padx=50,pady=10)

l=Label(f,text='ATM App',font=('ariel',30)).grid(row=0)

btn1=Button(win,text='Create Account',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=createacc).place(x=80,y=180)

btn2=Button(win,text='Balance Enquiry',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=checkbalance).place(x=320,y=180)

btn3=Button(win,text='Deposit',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=deposit).place(x=80,y=280)

btn4=Button(win,text='Withdraw',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=withdraw).place(x=320,y=280)

btn5=Button(win,text='Mini Statement',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=ministmt).place(x=80,y=380)

btn6=Button(win,text='Fast Cash',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=fastcash).place(x=320,y=380)

btn7=Button(win,text='Change Pin',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=changepin).place(x=80,y=480)

btn8=Button(win,text='Transfer Fund',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=transferfund).place(x=320,y=480)


