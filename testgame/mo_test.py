import lcddriver
from practicum import find_mcu_boards, McuBoard
from time import *
lcd = lcddriver.lcd()

devices = find_mcu_boards()
mcu = McuBoard(devices[0])
x = 0
y = 0
for i in range(10000):
    state = mcu.usb_read(0, length=1)
    mcu.usb_write(10, index=x, value=y)
    sleep(0.5)
    if(x<3):
        x += 1
    else:
        x = 0
        if(y == 0):
            y = 1
        else:
            y = 0
    lcd.lcd_display_string(chr(35),2)
    lcd.lcd_display_string("Mo is very cool",1)
    sleep(1)
    lcd.lcd_clear()
    sleep(2)
    lcd.lcd_display_string("Mo is very cool",3)
    sleep(0.5)
    lcd.lcd_clearline(3)
    #lcd.lcd_write("0x80")
    #x = state[0]
    #print(x)

#state = mcu.usb_read(0, length=1)
#print(state)
#mcu.usb_write(10, index=1, value=1)

