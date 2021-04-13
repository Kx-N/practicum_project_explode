import random
from practicum import find_mcu_boards, McuBoard
from time import sleep
import lcddriver

lcd = lcddriver.lcd()
devices = find_mcu_boards()
mcu = McuBoard(devices[0])

bot = 0

def ABC_game(fail):
    F = fail
    simon = False
    over = False
    a_sort = []
    c = []
    d = []
    a = list(random.sample(range(174,196),4))
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
            sleep(0.3)
            lcd.lcd_display_string("          ",4)
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
            lcd.lcd_display_string("  "+str(bot)+"      ",4)
            sleep(0.3)
            p = a[bot-1]

            if(p != a_sort[i]):
                F += 1
                lcd.lcd_display_string("Try again",4)
                break
            elif(i==3 and p == a_sort[i]):
                simon = True
                break
    if(not over):
        lcd.lcd_display_string("Pass",4)
        sleep(1)
        lcd.lcd_clear()
    return F

def AmongUs_game(fail):
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
        for i in range(0,len(b)):
            A = 3*(b[i]-1)
            B = 9 - A
            lcd.lcd_display_string("     "+chr(35)+"  "+chr(35)+"  "+chr(35)+"  "+chr(35)+"     ",1)
            lcd.lcd_display_string("     "+" "*A+chr(b[i])+" "*B+" "+"     ",2)
            sleep(0.3)
            lcd.lcd_display_string(" "*20,2)
        #print(b)
        for j in range(0,k+1):
            sleep(0.2)
            lcd.lcd_display_string(" "*10,4)
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
            lcd.lcd_display_string("  "+str(bot)+" "*10,4)
            sleep(0.2)

            if(bot != b[j]):
                lcd.lcd_display_string(" Try again",4)
                #print("fail")
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
        lcd.lcd_clear()
        #print("pass")
    return F


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
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 1):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M1[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 2):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M2[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 3):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M3[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 4):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M4[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 5):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M5[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 6):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M6[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 7):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M7[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 8):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M8[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        elif(a[i] == 9):
            for j in range(0, 5):
                lcd.lcd_display_string("#"*20,2)
                if(M9[j]==1):
                    sleep(1)
                else:
                    sleep(0.25)
                lcd.lcd_clearline(2)
                sleep(0.3)
        P = P + a[i]*(i+1)
        sleep(1)
    P = P%10
    return P

def Mos(fail):
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
    while(1):
        sleep(0.3)
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
            sleep(0.3)
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
        lcd.clear()
    return F

def is_push(x):
    if(x==1):
        return True
    else:
        return False

def LDR(fail):
    F = fail
    led = False
    over = False
    count = 1
    bot = 0

    while(count<=3 or (led==True and count==3)):
        if(F >= 3):
            over = True
            break
        rand_set = random.randrange(1005)
        sleep(0.2)
        lcd.lcd_display_string("  light value = "+str(rand_set),3)
        while(1):
            sleep(0.15)
            lcd.lcd_clearline(1)
            lcd.lcd_clearline(2)
            stateL = mcu.usb_read(1, length=2)
            sleep(0.1)
            stateB = mcu.usb_read(0, length=1)
            sleep(0.15)
            x = stateB[0]
            y = stateL[0]
            z = stateL[1]
            if(y == 0):
                bot = 0
            elif(y == 1):
                bot = 256
            elif(y == 2):
                bot == 512
            elif(y == 3):
                bot = 768
            get_light = bot + z
            
            if(get_light <= 170):
                lcd.lcd_display_string("  "+"="*3,1)
                lcd.lcd_display_string("  "+"="*3,2)
            elif(170 < get_light <= 340):
                lcd.lcd_display_string("  "+"="*6,1)
                lcd.lcd_display_string("  "+"="*6,2)
            elif(340 < get_light <= 510):
                lcd.lcd_display_string("  "+"="*9,1)
                lcd.lcd_display_string("  "+"="*9,2)
            elif(510 < get_light <= 680):
                lcd.lcd_display_string("  "+"="*12,1)
                lcd.lcd_display_string("  "+"="*12,2)
            elif(680 < get_light <= 850):
                lcd.lcd_display_string("  "+"="*15,1)
                lcd.lcd_display_string("  "+"="*15,2)
            elif(850 < get_light):
                lcd.lcd_display_string("  "+"="*18,1)
                lcd.lcd_display_string("  "+"="*18,2)
            
            if(x != 0):
                break
        #print(get_light)
        if(rand_set <= 170):
            if(get_light <= 170):
                led=True
                count+=1
                lcd.lcd_display_string("  correct"+" "*5,3)
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(127 <= rand_set < 255):
            if(127 <= get_light < 255):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(255 <= rand_set < 383):
            if(255 <= get_light < 383):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(383 <= rand_set < 511):
            if(383 <= get_light < 511):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(511 <= rand_set < 639):
            if(511 <= get_light < 639):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(639 <= rand_set < 767):
            if(639 <= get_light < 767):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(767 <= rand_set < 895):
            if(767 <= get_light < 895):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
        elif(895 <= rand_set):
            if(895 <= get_light):
                led=True
                count+=1
                print("correct")
                continue
            else:
                print("fail")
                F += 1
                continue
    if(not over):
        print("pass")
    return F
