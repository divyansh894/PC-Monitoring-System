import pyautogui
import time
import sqlite3
import random
date=time.localtime().tm_mday,time.localtime().tm_mon,time.localtime().tm_year
today=str(date[0])+'-'+str(date[1])+'-'+str(date[2])

con1=sqlite3.Connection('Settings')
cur1=con1.cursor()
cur1.execute('select * from settings')
frequency=cur1.fetchall()
count=0
while(1):
    name=random.random()
    myScreenshot=pyautogui.screenshot()
    myScreenshot.save('C:/Users/divyansh/Desktop/Keylogger/screenshot/'+today+' ('+str(name)+')'+'.png')
    time.sleep(int(frequency[0][0])*60)
