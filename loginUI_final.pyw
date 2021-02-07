import sqlite3
import os
con=sqlite3.Connection('keylogger')
cur=con.cursor()
cur.execute('create table if not exists info(username varchar(20),password varchar(20))')
con1=sqlite3.Connection('Settings')
cur1=con1.cursor()
cur1.execute('create table if not exists settings(frequency varchar(20))')
con2=sqlite3.Connection('Email')
cur2=con2.cursor()
cur2.execute('create table if not exists email(address varchar(100))')
from tkinter import *
from tkinter.messagebox import *
import webbrowser
root0=Tk()
root0.geometry('1000x1000')

#settings_panel
def create_setting_panel():
    setting_panel_heading=Frame(root0,height=50,width=400,highlightbackground='red',highlightthicknes=3)
    setting_panel_heading.place(x=300,y=30)
    setting_panel_frame=Frame(root0,height=300,width=400,highlightbackground='red',highlightthicknes=3)
    setting_panel_frame.place(x=300,y=70)
    Label(setting_panel_heading,text='SETTINGS',font=('Arial',25)).place(x=110,y=0)
    Label(setting_panel_frame,text='Screenshot frequency',font=('Arial',17)).place(x=20,y=30)
    freq=Scale(setting_panel_frame,from_=1,to=60,orient=HORIZONTAL)
    freq.place(x=280,y=20)
    def get_freq():
        cur1.execute('update settings set frequency=(?)',(freq.get(),))
        con1.commit()
        cur1.execute('select * from settings')
        frequency=cur1.fetchall()
    Button(setting_panel_frame,text='Done',command=get_freq).place(x=280,y=60)
    Label(setting_panel_frame,text='Recipient email address',font=('Arial',16)).place(x=20,y=110)
    email=Entry(setting_panel_frame)
    email.place(x=265,y=115)
    def get_email():
        cur2.execute('update email set address=(?)',(email.get(),))
        con2.commit()
        cur2.execute('select * from email')
        email_add=cur2.fetchall()
    Button(setting_panel_frame,text='Done',command=get_email).place(x=280,y=140)
    Label(setting_panel_frame,text='Open Log File',font=('Arial',17)).place(x=20,y=200)
    Label(setting_panel_frame,text='Day-Month-Year').place(x=265,y=185)
    spin_day=Spinbox(setting_panel_frame,from_=1,to=31,width=3)
    spin_day.place(x=255,y=205)
    spin_month=Spinbox(setting_panel_frame,from_=1,to=12,width=3)
    spin_month.place(x=295,y=205)
    spin_year=Spinbox(setting_panel_frame,from_=2020,to=2030,width=5)
    spin_year.place(x=335,y=205)
    def get_date():
        file=spin_day.get()+'-'+spin_month.get()+'-'+spin_year.get()
        try:
            os.startfile('C:/Users/divyansh/Desktop/Keylogger/LOG FILES/'+file+'.txt')
        except FileNotFoundError:
            showerror('error','File not Found')
    def get_date1():
        clip_file=spin_day.get()+'-'+spin_month.get()+'-'+spin_year.get()
        try:
            os.startfile('C:/Users/divyansh/Desktop/Keylogger/LOG FILES/'+'clipLog '+clip_file+'.txt')
        except FileNotFoundError:
            showerror('error','File not Found')
    Button(setting_panel_frame,text='Open Keylog',command=get_date).place(x=280,y=230)
    Button(setting_panel_frame,text='Open Cliplog',command=get_date1).place(x=280,y=260)

#new user frame

#done button code

def create_new_user_frame():
    heading_frame2=Frame(root0,height=50,width=400,highlightbackground='red',highlightthicknes=3)
    heading_frame2.place(x=300,y=30)
    Label(heading_frame2,text='SIGNUP',font=('Arial',25)).place(x=140,y=0)
    new_user_frame=Frame(root0,height=300,width=400,highlightbackground='red',highlightthicknes=3)
    new_user_frame.place(x=300,y=70)
    Label(new_user_frame,text='Username ',font=('Arial',20)).place(x=70,y=60)
    un=Entry(new_user_frame)
    un.place(x=220,y=70)
    Label(new_user_frame,text='Password ',font=('Arial',20)).place(x=70,y=100)
    pwd=Entry(new_user_frame,show="*")
    pwd.place(x=220,y=110)
    Label(new_user_frame,text='Confirm Password ',font=('Arial',12)).place(x=70,y=150)
    confirm_pwd=Entry(new_user_frame,show="*")
    confirm_pwd.place(x=220,y=150)
    def done():
        if pwd.get()!=confirm_pwd.get():
            def fun():
                showerror('error','password not confirmed')
            fun()
            heading_frame2.place_forget()
            new_user_frame.place_forget()
            create_new_user_frame()
        else:
            cur.execute('insert into info (username,password) values(?,?)',(un.get(),pwd.get()))
            con.commit()
            #cur.execute('select * from info')
            #print(cur.fetchall())
            heading_frame2.place_forget()
            new_user_frame.place_forget()
            create_login_frame()
    dn=Button(new_user_frame,text='Done',command=done)
    dn.place(x=80,y=190)
    

#login_frame
def create_login_frame():
    login_frame=Frame(root0,height=300,width=400,highlightbackground='red',highlightthicknes=3)
    login_frame.place(x=300,y=50)
    #heading frame code
    heading_frame=Frame(root0,height=50,width=400,highlightbackground='red',highlightthicknes=3)
    heading_frame.place(x=300,y=30)
    #inside of login frame
    Label(heading_frame,text='LOGIN / SIGNUP',font=('Arial',25)).place(x=75,y=0)
    Label(login_frame,text='Username ',font=('Arial',20)).place(x=70,y=60)
    un_login=Entry(login_frame)
    un_login.place(x=220,y=70)
    Label(login_frame,text='Password ',font=('Arial',20)).place(x=70,y=100)
    pwd_login=Entry(login_frame,show="*")
    pwd_login.place(x=220,y=110)
    def new_user():
        login_frame.place_forget()
        heading_frame.place_forget()
        create_new_user_frame()
    def login():
        cur.execute('select * from info where username=(?) and password=(?)',(un_login.get(),pwd_login.get()))
        record=cur.fetchall()
        if len(record)==1:
            login_frame.place_forget()
            heading_frame.place_forget()
            login_frame.place_forget()
            heading_frame.place_forget()
            create_setting_panel()
        else:
            showerror('error','User not found')
            un_login.delete(0,END)
            pwd_login.delete(0,END)
        
    Button(login_frame,text='Login',width=20,command=login).place(x=70,y=170)
    Button(login_frame,text='new user?',bd=0,font=('Arial',12),command=new_user).place(x=100,y=200)
    root0.mainloop()
create_login_frame()

