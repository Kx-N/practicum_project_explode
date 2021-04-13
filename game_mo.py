import random
from def_game_mo import ABC_game, AmongUs_game, Mos, LDR
from practicum import find_mcu_boards, McuBoard
from time import sleep

devices = find_mcu_boards()
mcu = McuBoard(devices[0])

fail = 0
over = False
a = list(random.sample(range(3),3))
a.append(3)

fail = Mos(fail)

while(1):
    state = mcu.usb_read(0, length=1)
    sleep(0.15)
    x = state[0]
    if(x == 2 or x == 4):
        break

for i in range(0,len(a)):
    if(a[i] == 0):
        print("ABC game")
        fail = ABC_game(fail)
    elif(a[i] == 1):
        print("Among-us game")
        fail = AmongUs_game(fail)
    elif(a[i] == 2):
        print("LDR game")
        fail = LDR(fail)
    elif(a[i] == 3):
        print("Mos-pass game")
        fail = Mos(fail)
    if(fail >= 3):
        over = True
        break

if(not over):
    print("You Win")
else:
    print("Game Over")
