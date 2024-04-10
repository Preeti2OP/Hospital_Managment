from tkinter import*
import tkinter as tk
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

root=tk.Tk()
root.geometry("800x500")
root.config(bg="black")
root.title("HOSPITAL MANAGMENT")
im=PhotoImage(file='doctor.png')
l=Label(root,image=im)
l.place(x=0,y=0) 
l=tk.Label(root,text="WELCOME TO MARIAM HOSPITAL",font=("Times",30)).place(x=48,y=5)

def Drlogin():
    top=Toplevel(root)
    top.geometry('800x500')
    Label(top, text='Doctor_Id',font="Times,120").place(x=30,y=30)
    Doctor_Id=IntVar()
    e1 = Entry(top,textvariable="Doctor_ID   ",font="Times,120").place(x=100,y=30)
    def get():
        e1 = Entry(top,textvariable="Doctor_ID")
        e1.place(x=100,y=30)
        connection=mysql.connector.connect(host='127.0.0.1',user="root",password="root",database="hospital")
        engine=create_engine("mysql://root:root@127.0.0.1:3306/hospital")
        df=pd.read_sql_table("doctor",engine)
        cursor = connection.cursor()
        cursor.execute("""select * from doctor where Doctor_FirstName=%s""",((Doctor_Id.get(),)))
        records = cursor.fetchone()
        Label(top,text=records,font="Times,150").place(x=100,y=140)
        #print( records)
    button=Button(top,text='LOGIN',command=get,font="Times,100")
    button.place(x=150,y=80)
    button1=Button(top,text='Cancel',command=quit,font="Times,100")
    button1.place(x=250,y=80)


def Ptlogin():
    top=Toplevel(root)
    top.geometry('800x500')
    Label(top, text='PATIENT_Id',font="Times,120").place(x=30,y=30)
    patient_Id=IntVar()
    e1 = Entry(top,textvariable="PATIENT_ID   ",font="Times,120").place(x=100,y=30)
    def get1():
        e1 = Entry(top,textvariable="PATIENT_ID")
        e1.place(x=100,y=30)
        connection=mysql.connector.connect(host='127.0.0.1',user="root",password="root",database="hospital")
        engine=create_engine("mysql://root:root@127.0.0.1:3306/hospital")
        df=pd.read_sql_table("doctor",engine)
        cursor = connection.cursor()
        cursor.execute("""select * from patient where Patient_FirstName=%s""",((patient_Id.get(),)))
        records = cursor.fetchone()
        Label(top,text=records,font="Times,150").place(x=100,y=140)
    button=Button(top,text='LOGIN',command=get1,font="Times,100")
    button.place(x=150,y=80)
    button1=Button(top,text='Cancel',command=quit,font="Times,100")
    button1.place(x=250,y=80)





button2=Button(root,text='DOCTOR_LOGIN',command=Drlogin,font="Times,100",bg="light blue").place(x=120,y=130)
button2=Button(root,text='PATIENT_LOGIN',command=Ptlogin,font="Times,100",bg="light blue").place(x=120,y=200)



root.mainloop()
