import random
from def_game_mo import ABC_game, AmongUs_game, Mos, LDR
from practicum import find_mcu_boards, McuBoard
from time import sleep
import lcddriver

lcd = lcddriver.lcd()
devices = find_mcu_boards()
mcu = McuBoard(devices[0])


lcd.lcd_display_string(" "*6+"Bomboom?",2)
life = 3
mcu.usb_write(10,index=0,value=1)
mcu.usb_write(10,index=1,value=1)
mcu.usb_write(10,index=2,value=1)
fail = 0
over = False
a = list(random.sample(range(3),3))
a.append(3)

#fail = LDR(fail,life)

while(1):
    state = mcu.usb_read(0, length=1)
    sleep(0.15)
    x = state[0]
    if(x != 0):
        break

for i in range(0,len(a)):
    if(a[i] == 0):
        #print("ABC game")
        lcd.lcd_display_string(" "*7+"Ready?",2)
        sleep(0.6)
        lcd.lcd_clear()
        fail,life = ABC_game(fail,life)
    elif(a[i] == 1):
        #print("Among-us game")
        lcd.lcd_display_string(" "*7+"Ready?",2)
        sleep(0.6)
        lcd.lcd_clear()
        fail,life = AmongUs_game(fail,life)
    elif(a[i] == 2):
        #print("LDR game")
        lcd.lcd_display_string(" "*7+"Ready?",2)
        sleep(0.6)
        lcd.lcd_clear()
        fail,life = LDR(fail,life)
    elif(a[i] == 3):        
        lcd.lcd_display_string(" "*7+"Ready?",2)
        sleep(0.6)
        lcd.lcd_clear()
        fail,life = Mos(fail,life)
    if(fail >= 3):
        over = True
        break
lcd.lcd_clear()
if(not over):
    lcd.lcd_display_string(" "*6+"You Win",2)
    sleep(1)
    lcd.lcd_clear()
    #print("You Win")
else:
    #print("Game Over")
    mcu.usb_write(11,value=1)
    lcd.lcd_display_string(" "*5+"Game Over",2)
    sleep(1)
    mcu.usb_write(11,value=0)
    lcd.lcd_clear()
