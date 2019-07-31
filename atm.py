from tkinter import *
import pymysql
import pymysql.cursors
from datetime import datetime
from tkinter import messagebox
import depositfun as df
import withdrawfun as wf
import ministmtfun as mf
import transferfundfun as tf
import checkbalfun as cf
import fastcashfun as ff
import changepinfun as cpf
import createaccfun as caf


win=Tk()
win.title("ATM Application")
win.config(bg="Cyan")
win.geometry("600x600")
win.resizable(False,False)

f=Frame(win,width=500,height=150,bd=8,relief='sunken',bg='pink',cursor='dot',highlightcolor='blue').grid(padx=50,pady=10)

l=Label(f,text='ATM App',font=('ariel',30)).grid(row=0)

btn1=Button(win,text='Create Account',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=caf.createacc).place(x=80,y=180)

btn2=Button(win,text='Balance Enquiry',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=cf.checkbalance).place(x=320,y=180)

btn3=Button(win,text='Deposit',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=df.deposit).place(x=80,y=280)

btn4=Button(win,text='Withdraw',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=wf.withdraw).place(x=320,y=280)

btn5=Button(win,text='Mini Statement',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=mf.ministmt).place(x=80,y=380)

btn6=Button(win,text='Fast Cash',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=ff.fastcash).place(x=320,y=380)

btn7=Button(win,text='Change Pin',bd=4,font=('ariel',15),relief='sunken',width=13,activebackground='pink',command=cpf.changepin).place(x=80,y=480)

btn8=Button(win,text='Transfer Fund',bd=4,font=('ariel',15),relief='ridge',width=13,activebackground='pink',command=tf.transferfund).place(x=320,y=480)


