import pygame
from pygame.locals import *
from math import floor
import time
import os
from practicum import find_mcu_boards, McuBoard
import lcddriver

lcd = lcddriver.lcd()
devices = find_mcu_boards()
mcu = McuBoard(devices[0])

def timer():
    clock = pygame.time.Clock()
    tim = 0  
    last = 0

    while True:
        mcu.usb_write(11,value=0)
        milli = clock.tick()  #clock.tick() returns how many milliseconds passed since the last time it was called
        time.sleep(1)            #So it tells you how long the while loop took
        seconds = milli/1000
        tim += seconds                     
        t = 300 
        s = t-(floor(tim))
        minute = floor(s/60)
        sec = s%60
        if(sec>=10):
            #lcd.lcd_display_string(" "*15+str(minute)+":"+str(sec),1)
            print('%d:%.0f'%(minute,sec)) #So you can see that this works
            if(s < 30):
                mcu.usb_write(11,value=1)
                time.sleep(0.2)
            elif(s%10 == 0):
                mcu.usb_write(11,value=1)
                time.sleep(0.2)
        else:
            if(s < 30):
                mcu.usb_write(11,value=1)
                time.sleep(0.2)
            elif(s%10 == 0):
                mcu.usb_write(11,value=1)
                time.sleep(0.2)
            print('%d:0%d'%(minute,sec))
            #lcd.lcd_display_string(" "*15+str(minute)+":0"+str(sec),1)
        
        if(t-tim <= 0):
            break
    time.sleep(0.6)
#timer()
