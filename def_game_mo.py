import random
from practicum import find_mcu_boards, McuBoard
from time import sleep
import lcddriver

lcd = lcddriver.lcd()
devices = find_mcu_boards()
mcu = McuBoard(devices[0])

bot = 0

def light_life(life):
    if(life == 3):
        mcu.usb_write(10,index=2,value=0)
    elif(life == 2):
        mcu.usb_write(10,index=1,value=0)
    else:
        mcu.usb_write(10,index=0,value=0)
    life -= 1
    return life

def ABC_game(fail,life):
    F = fail
    simon = False
    over = False
    a_sort = []
    c = []
    d = []
    a = list(random.sample(range(174,214),4))
    for i in range(0,4):
        a_sort.append(a[i])
    a_sort.sort()
    lcd.lcd_display_string("    "+chr(35)*11+"    ",1)
    lcd.lcd_display_string("    "+chr(35)+" "+chr(a[0])+" "+chr(a[1])+" "+chr(a[2])+" "+chr(a[3])+" "+chr(35)+"     ",2)
    lcd.lcd_display_string("    "+chr(35)*11+"    ",3)
    
    while(simon == False):
        if(F >= 3):
            over = True
            break
        for i in range(0,4):
            sleep(0.35)
            lcd.lcd_clearline(4)
            while(1):
                state = mcu.usb_read(0, length=1)
                sleep(0.15)
                x = state[0]
                if(x != 0):
                    break
            if(x == 1):
                bot = 1
            elif(x == 2):
                bot = 2
            elif(x == 4):
                bot = 3
            elif(x == 8):
                bot = 4
            lcd.lcd_clearline(4)
            lcd.lcd_display_string("  "+str(bot),4)
            sleep(0.3)
            p = a[bot-1]

            if(p != a_sort[i]):
                F += 1
                life = light_life(life)    
                lcd.lcd_display_string(" Try again",4)
                break
            elif(i==3 and p == a_sort[i]):
                simon = True
                break
    if(not over):
        lcd.lcd_display_string(" Pass",4)
    sleep(1)
    lcd.lcd_clearlineOut(1)
    return F, life

def AmongUs_game(fail,life):
    F = fail
    b = []
    sequence = False
    over = False

    a = list(random.sample(range(4),4))
    bot = 0
    k = 0
    while(not sequence):
        if(F >= 3):
            over = True
            break
        b.append(a[k]+1)
        lcd.lcd_display_string("     "+chr(35)+"  "+chr(35)+"  "+chr(35)+"  "+chr(35)+"     ",2)
        lcd.lcd_display_string(" "*2+"Any Key To Play",4)
        while(1):
            state = mcu.usb_read(0, length=1)
            sleep(0.15)
            x = state[0]
            if(x != 0):
                break
        lcd.lcd_clear()
        for i in range(0,len(b)):
            A = 3*(b[i]-1)
            B = 9 - A
            lcd.lcd_display_string("     "+chr(35)+"  "+chr(35)+"  "+chr(35)+"  "+chr(35)+"     ",2)
            lcd.lcd_display_string("     "+" "*A+chr(3)+" "*B+" "+"     ",3)
            sleep(0.3)
            lcd.lcd_clearline(3)
        for j in range(0,k+1):
            sleep(0.35)
            lcd.lcd_clearline(4)
            while(1):
                state = mcu.usb_read(0, length=1)
                sleep(0.2)
                x = state[0]
                if(x != 0):
                    break
            if(x == 1):
                bot = 1
            elif(x == 2):
                bot = 2
            elif(x == 4):
                bot = 3
            elif(x == 8):
                bot = 4
            lcd.lcd_clearline(4)
            lcd.lcd_display_string("  "+str(bot),4)
            sleep(0.2)

            if(bot != b[j]):
                lcd.lcd_display_string(" Try again",4)
                life = light_life(life)    
                F += 1
                k = -1
                b.clear()
                break
            elif(j == 3 and bot == b[j]):
                sequence = True
                break
        k += 1
    if(not over):
        lcd.lcd_display_string(" Pass",4)
    sleep(1)
    lcd.lcd_clearlineOut(1)
    return F, life


def mos_loop(a):
    M0 = [1,0,0,1,1]
    M1 = [0,1,1,1,1]
    M2 = [0,0,1,1,1]
    M3 = [0,0,0,1,1]
    M4 = [0,0,0,0,1]
    M5 = [0,0,0,0,0]
    M6 = [1,0,0,0,0]
    M7 = [1,1,0,0,0]
    M8 = [1,1,1,0,0]
    M9 = [1,1,1,1,0]
    P = 0
    for i in range(0,len(a)):
        lcd.lcd_display_string(" "*10+str(i+1),2)
        sleep(0.6)
        if(a[i] == 0):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M0[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 1):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M1[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 2):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M2[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 3):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M3[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 4):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M4[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 5):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M5[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 6):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M6[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 7):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M7[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 8):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M8[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 9):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M9[j]==1):
                    sleep(1)
                else:
                    sleep(0.2)
                lcd.lcd_clearline(2)
                sleep(0.3)
        P = P + a[i]*(i+1)
        sleep(1)
    P = P%10
    return P

def Mos(fail,life):
    b = []
    over = False
    F = fail

    M0 = [1,0,0,1,1]
    M1 = [0,1,1,1,1]
    M2 = [0,0,1,1,1]
    M3 = [0,0,0,1,1]
    M4 = [0,0,0,0,1]
    M5 = [0,0,0,0,0]
    M6 = [1,0,0,0,0]
    M7 = [1,1,0,0,0]
    M8 = [1,1,1,0,0]
    M9 = [1,1,1,1,0]
    a =[]
    a  = list(random.sample(range(10),2))
    
    PA = False
    lcd.lcd_display_string("Press button To Play",2)
    while(1):
        state = mcu.usb_read(0, length=1)
        sleep(0.15)
        x = state[0]
        if(x != 0):
            break
    lcd.lcd_clear()
    while(1):
        sleep(0.3)
        lcd.lcd_clearline(2)
        lcd.lcd_clearline(4)
        sleep(0.2)
        if(F >= 3):
            over = True
            break
        P = 0
        P = mos_loop(a)
        lcd.lcd_display_string("    your answer?",2)
        sleep(0.3)
        for i in range(0,5):
            sleep(0.35)
            lcd.lcd_clearline(4)

            while(1):
                state = mcu.usb_read(0, length=1)
                sleep(0.2)
                x = state[0]
                if(x == 1 or x == 2 ):
                    break
            if(x == 1):
                bot = 0
                lcd.lcd_display_string("  .",4)
            elif(x == 2):
                bot = 1
                lcd.lcd_display_string("  _",4)
            sleep(0.2)
            b.append(bot)

        if(P == 0):
            for j in range(0, len(M0)):
                lcd.lcd_clearline(4)
                if(M0[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M0)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 1):
            for j in range(0, len(M1)):
                if(M1[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M1)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 2):
            for j in range(0, len(M2)):
                if(M2[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M2)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 3):
            for j in range(0, len(M3)):
                if(M3[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M3)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 4):
            for j in range(0, len(M4)):
                if(M4[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M4)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 5):
            for j in range(0, len(M5)):
                if(M5[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M5)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 6):
            for j in range(0, len(M6)):
                if(M6[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M6)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 7):
            for j in range(0, len(M7)):
                if(M7[j] != b[j]):
                    b.clear()
                    life = light_life(life)    
                    lcd.lcd_display_string(" Try again",4)
                    F += 1
                    break
                if(j==len(M7)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 8):
            for j in range(0, len(M8)):
                if(M8[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M8)-1):
                    PA = True
                    break
            if(PA):
                break
        elif(P == 9):
            for j in range(0, len(M9)):
                if(M9[j] != b[j]):
                    b.clear()
                    lcd.lcd_display_string(" Try again",4)
                    life = light_life(life)    
                    F += 1
                    break
                if(j==len(M9)-1):
                    PA = True
                    break
            if(PA):
                break
    if(not over):
        lcd.lcd_display_string(" Pass",4)
    sleep(1)
    lcd.lcd_clearlineOut(1)
    return F, life

def LDR(fail,life):
    F = fail
    over = False
    count = 1
    bot = 0

    while(count <= 3):
        if(F >= 3):
            over = True
            break
        rand_set = random.randrange(1000)
        sleep(0.35)
        lcd.lcd_clearline(4)
        lcd.lcd_display_string("  "+str(rand_set),3)
        while(1):
            sleep(0.3)
            lcd.lcd_clearline(4)
            stateL = mcu.usb_read(1, length=2)
            sleep(0.1)
            stateB = mcu.usb_read(0, length=1)
            sleep(0.15)
            x = stateB[0]
            y = stateL[0]
            z = stateL[1]
            bot = (y<<8)
            #if(y == 0):
             #   bot = 0
            #elif(y == 1):
             #   bot = 256
            #elif(y == 2):
             #   bot = 512
            #elif(y == 3):
             #   bot = 768
            get_light = (bot | z)
            
            if(get_light <= 170):
                lcd.lcd_display_string(" "+"="*3+" "*16,1)
                lcd.lcd_display_string(" "+"="*3+" "*16,2)
            elif(170 < get_light <= 340):
                lcd.lcd_display_string(" "+"="*6+" "*13,1)
                lcd.lcd_display_string(" "+"="*6+" "*13,2)
            elif(340 < get_light <= 510):
                lcd.lcd_display_string(" "+"="*9+" "*10,1)
                lcd.lcd_display_string(" "+"="*9+" "*10,2)
            elif(510 < get_light <= 680):
                lcd.lcd_display_string(" "+"="*12+" "*7,1)
                lcd.lcd_display_string(" "+"="*12+" "*7,2)
            elif(680 < get_light <= 850):
                lcd.lcd_display_string(" "+"="*15+" "*4,1)
                lcd.lcd_display_string(" "+"="*15+" "*4,2)
            elif(850 < get_light):
                lcd.lcd_display_string(" "+"="*18,1)
                lcd.lcd_display_string(" "+"="*18,2)
            
            if(x != 0):
                break
        if(rand_set <= 170):
            if(get_light <= 170):
                count+=1
                lcd.lcd_display_string("  Correct"+" "*5,4)
                continue
            else:
                lcd.lcd_display_string("  Try again"+" "*5,4)
                life = light_life(life)    
                F += 1
                continue
        elif(170 < rand_set <= 340):
            if(170 < get_light <= 340):
                count+=1
                lcd.lcd_display_string("  Correct"+" "*5,4)
                continue
            else:
                lcd.lcd_display_string("  Try again"+" "*5,4)
                life = light_life(life)    
                F += 1
                continue
        elif(340 < rand_set <= 510):
            if(340 < get_light <= 510):
                count+=1
                lcd.lcd_display_string("  Correct"+" "*5,4)
                continue
            else:
                life = light_life(life)    
                lcd.lcd_display_string("  Try again"+" "*5,4)
                F += 1
                continue
        elif(510 < rand_set <= 680):
            if(510 < get_light <= 680):
                count+=1
                lcd.lcd_display_string("  Correct"+" "*5,4)
                continue
            else:
                lcd.lcd_display_string("  Try again"+" "*5,4)
                life = light_life(life)    
                F += 1
                continue
        elif(680 < rand_set <= 850):
            if(680 < get_light <= 850):
                count+=1
                lcd.lcd_display_string("  Correct"+" "*5,4)
                continue
            else:
                lcd.lcd_display_string("  Try again"+" "*5,4)
                life = light_life(life)    
                F += 1
                continue
        elif(850 < rand_set):
            if(850 < get_light):
                count+=1
                lcd.lcd_display_string("  Correct"+" "*5,4)
                continue
            else:
                lcd.lcd_display_string("  Try again"+" "*5,4)
                life = light_life(life)    
                F += 1
                continue
        
    if(not over):
        lcd.lcd_display_string("  Pass"+" "*5,4)
    sleep(1)
    lcd.lcd_clearlineOut(1)
    return F, life
