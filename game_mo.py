import random
from def_game_mo import ABC_game, AmongUs_game, Mos, LDR
from practicum import find_mcu_boards, McuBoard
from time import sleep ,time
import lcddriver
import os
from test_time import timer
import threading


def game(fail,life):
    over = False
    for i in range(0,len(a)):
        lcd.lcd_clear()
        if(a[i] == 0):
            lcd.lcd_display_string(" "*7+"Ready?",2)
            sleep(0.8)
            lcd.lcd_clearlineOut(1)
            fail,life = ABC_game(fail,life)
        elif(a[i] == 1):
            lcd.lcd_display_string(" "*7+"Ready?",2)
            sleep(0.8)
            lcd.lcd_clearlineOut(1)
            fail,life = AmongUs_game(fail,life)
        elif(a[i] == 2):
            lcd.lcd_display_string(" "*7+"Ready?",2)
            sleep(0.8)
            lcd.lcd_clearlineOut(1)
            fail,life = LDR(fail,life)
        elif(a[i] == 3):        
            lcd.lcd_display_string(" "*7+"Ready?",2)
            sleep(1)
            lcd.lcd_clearlineOut(1)
            fail,life = Mos(fail,life)
        if(fail >= 3):
            over = True
            break
    lcd.lcd_clear()
    if(not over):
        lcd.lcd_display_string(" "*6+"You Win",2)
        sleep(3)
        lcd.lcd_clear()
    else:
        mcu.usb_write(11,value=1)
        lcd.lcd_display_string(" "*5+"Game Over",2)
        sleep(3)
        mcu.usb_write(11,value=0)
        lcd.lcd_clear()
    os._exit(0)

lcd = lcddriver.lcd()
devices = find_mcu_boards()
mcu = McuBoard(devices[0])

life = 3
fail = 0
countdown = threading.Thread(target=timer)
playgame = threading.Thread(target=game, args=[fail, life])


lcd.lcd_display_string(" "*5+"Boombitxx",2)
lcd.lcd_display_string(" "*2+"Any Key To Start",4)

mcu.usb_write(10,index=0,value=1)
mcu.usb_write(10,index=1,value=1)
mcu.usb_write(10,index=2,value=1)

a = list(random.sample(range(3),3))
a.append(3)

while(1):
    state = mcu.usb_read(0, length=1)
    sleep(0.15)
    x = state[0]
    if(x != 0):
        break
lcd.lcd_clear()

countdown.start()
playgame.start()

countdown.join()

lcd.lcd_clear()
mcu.usb_write(11,value=1)
lcd.lcd_display_string(" "*5+"Game Over",2)
time.sleep(3)
mcu.usb_write(11,value=0)
lcd.lcd_clear()
os._exit(0)

