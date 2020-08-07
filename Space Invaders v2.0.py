import pygame, random, time, clr

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#CONSTANTS
X=1360
Y=768
plr_Y=int((6*Y)/7)
add=int(X/341.5)

#Colours
def blue(): return 25, 25, 112
def red(): return 250, 0, 0
def green(): return 148, 216, 17
def yellow(): return 250, 250, 0
def pink(): return 255, 20, 147
def orange(): return 255, 173, 17
def brown(): return 139, 69, 19
def light_blue(): return 135, 206, 250
def light_green(): return 60, 236, 151
def dark_green(): return 8, 154, 139
def white(): return 255, 255, 255
def black(): return 0, 0, 0
def grey(): return 192, 192, 192
def dark_blue(): return 0, 0, 30

#variables
blt=0
wst=0
scr=0
count=0
a=1

x=int((30*X-2*X)/60)
blt_x=int(X/150)
blt_y=int(Y/20)
var_x=X/5464                # 0.25
var_y=1366/(683*(10**2))    # 0.02

dead=[]
l_blt=[]
l_bots=[]
rx=[]
ry=[]
bot_blt=[]

bool1=False
b=False

for i in range(30):
    rx.append(random.randrange(1, X))
    ry.append(random.randrange(1, Y))

for i in range(-3, 0, 1):
    for j in range(-6, 0, 1):
        l_bots.append([[(int(X/7) * -(j+0.5) + int(X/14-X/20)), int(Y / 15) * (-i), int(X/10), int(Y/20)], 3])


#Functions


def prt(v_nm, x_var, y_var, tilt=0, f_clr=white(), bg_clr=None, f_sz=10, b_center=True):
    font = pygame.font.SysFont("comicsansms", f_sz)
    if bg_clr==None:
        text = font.render(v_nm, True, f_clr)
    else:
        text = font.render(v_nm, True, f_clr, bg_clr)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    if tilt != 0:
        text = pygame.transform.rotate(text, tilt)
    if b_center == True:
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    screen.blit(text, textRect)

def refresh():
    global scr, bool1, wst, count, plr_lvs, b

    # Normal refreshing
    pygame.draw.rect(screen, dark_blue(), pygame.Rect(0, 0, X + blt_x, Y + blt_y))
    for i in range(30):
        pygame.draw.rect(screen, white(), pygame.Rect(rx[i], ry[i], int(X/300), int(X/300)))

    if plr_lvs>=3:
        pygame.draw.polygon(screen, dark_green(), [(int(x), plr_Y), (int(x + 2 * X / 30) - 2, plr_Y), (int(x + X / 30), int(plr_Y - Y / 75))])
        pygame.draw.rect(screen, dark_green(), pygame.Rect(int(x), plr_Y, int(X / 15), int(Y / 50)))
    elif plr_lvs==2:
        pygame.draw.polygon(screen, green(), [(int(x), plr_Y), (int(x + 2 * X / 30) - 2, plr_Y), (int(x + X / 30), int(plr_Y - Y / 75))])
        pygame.draw.rect(screen, green(), pygame.Rect(int(x), plr_Y, int(X / 15), int(Y / 50)))
    elif plr_lvs==1:
        pygame.draw.polygon(screen, light_green(), [(int(x), plr_Y), (int(x + 2 * X / 30) - 2, plr_Y), (int(x + X / 30), int(plr_Y - Y / 75))])
        pygame.draw.rect(screen, light_green(), pygame.Rect(int(x), plr_Y, int(X / 15), int(Y / 50)))


    # Bot Bullets
    for i in range(len(l_bots)):
        if l_bots[i][1] == 3:
            pygame.draw.rect(screen, white(), pygame.Rect(int(l_bots[i][0][0]), int(l_bots[i][0][1]), int(l_bots[i][0][2]), int(l_bots[i][0][3])))
        elif l_bots[i][1] == 2:
            pygame.draw.rect(screen, yellow(), pygame.Rect(int(l_bots[i][0][0]), int(l_bots[i][0][1]), int(l_bots[i][0][2]), int(l_bots[i][0][3])))
        elif l_bots[i][1] == 1:
            pygame.draw.rect(screen, red(), pygame.Rect(int(l_bots[i][0][0]), int(l_bots[i][0][1]), int(l_bots[i][0][2]), int(l_bots[i][0][3])))
        if b==True and l_bots[i][1] == 0:
                pygame.draw.rect(screen, white(), pygame.Rect(int(l_bots[i][0][0]), int(l_bots[i][0][1]), int(l_bots[i][0][2]), int(l_bots[i][0][3])), 1)
        # Bot Movement
        if bool1 == False:
            l_bots[i][0][0] += var_x
            if int(l_bots[i][0][0] + l_bots[i][0][2]) == X - int(X / 35):
                bool1 = True
        elif bool1 == True:
            l_bots[i][0][0] -= var_x
            if int(l_bots[i][0][0]) == int(X / 35):
                bool1 = False
        l_bots[i][0][1] += var_y

    # Very ahead
    for i in range(len(l_bots)):
        if l_bots[i][0][1] + l_bots[i][0][3]>=plr_Y - Y / 75 and l_bots[i][1] != 0:
            plr_lvs=0
            return

    if len(l_bots)==0:
        for i in range(3):
            for j in range(-6, 0, 1):
                l_bots.append([[(int(X / 7) * -(j + 0.5) + int(X / 14 - X / 20)), (int(Y / 15) * (-i)) - int(Y / 20), int(X / 10), int(Y / 20)], 3])

    if len(l_bots)>6 and int(l_bots[-1][0][1]) > int(Y / 15):
        for i in range(3):
            for j in range(-6, 0, 1):
                l_bots.append([[l_bots[-j][0][0], -int(Y / 15) * (i+1), int(X/10), int(Y/20)], 3])

    if count == int(sht_spd) and len(l_bots)!=0:
        brk=False
        while True:
            r = random.randrange(6)
            for i in range(int(len(l_bots)/6)):
                if l_bots[r + (i * 6)][1] != 0:
                    bot_blt.append([int(l_bots[r + (i * 6)][0][0] + int(X/20)), int(l_bots[r + (i * 6)][0][1] + int(Y/20))])
                    brk=True
                    break
            if brk==True:
                break
    count%=int(sht_spd)
    count+=1
    for i in range(len(bot_blt)):
        pygame.draw.rect(screen, orange(), pygame.Rect(bot_blt[i][0], bot_blt[i][1], blt_x, blt_y))
        bot_blt[i][1]+=blt_spd
    # Bullets
    for i in range(len(l_blt)):
        l_blt[i][1]-=blt_spd
        pygame.draw.rect(screen, blue(), pygame.Rect(int(l_blt[i][0]), int(l_blt[i][1]), blt_x, blt_y))

    # Check bullets
    if len(l_blt) > 0:
        i = 0
        while i < len(l_blt):
            if l_blt[i][1] <= -int(Y/10):
                l_blt.pop(i)
                wst+=1
            i = i + 1

    if len(bot_blt) > 0:
        i=0
        while i < len(bot_blt):
            if bot_blt[i][1] >= Y:
                bot_blt.pop(i)
                if len(bot_blt)==0:
                    break
            i+=1

    # Bullets Crash
    l_rmw = []
    for i in range(len(l_blt)):
        for j in range(len(bot_blt)):
            if (l_blt[i][0]   <= bot_blt[j][0] <= l_blt[i][0]+blt_x   or l_blt[i][0]   <= bot_blt[j][0]+blt_x <= l_blt[i][0]+blt_x or\
                bot_blt[j][0] >= l_blt[i][0]   >= bot_blt[j][0]+blt_x or bot_blt[j][0] >= l_blt[i][0]+blt_x   >= bot_blt[j][0]+blt_x) and\
               (l_blt[i][1]   <= bot_blt[j][1] <= l_blt[i][1]+blt_x   or l_blt[i][1]   <= bot_blt[j][1]+blt_x <= l_blt[i][1]+blt_x or\
                bot_blt[j][1] >= l_blt[i][1]   >= bot_blt[j][1]+blt_x or bot_blt[j][1] >= l_blt[i][1]+blt_x   >= bot_blt[j][1]+blt_x):
                l_rmw.append([i, j])
                break
    for i in range(len(l_rmw)):
        l_blt.pop(l_rmw[i][0]-i)
        bot_blt.pop(l_rmw[i][1]-i)

    # Bot Lives
    l_rmw = []
    for i in range(len(l_blt)):
        for j in range(len(l_bots)):
            if l_bots[j][1] != 0:
                if (l_bots[j][0][0] <= l_blt[i][0] <= l_bots[j][0][0]+l_bots[j][0][2] or l_bots[j][0][0] <= l_blt[i][0]+blt_x <= l_bots[j][0][0]+l_bots[j][0][2])\
                    and (((l_bots[j][0][1] <= l_blt[i][1] <= l_bots[j][0][1]+l_bots[j][0][3])) or (l_bots[j][0][1] <= l_blt[i][1]+blt_y <= l_bots[j][0][1]+l_bots[j][0][3])):
                    l_rmw.append(i)
                    l_bots[j][1]-=1
                    break
    for i in range(len(l_rmw)):
        l_blt.pop(l_rmw[i]-i)

    # Player Lives
    j=0
    for i in range(len(bot_blt)):
        if (bot_blt[i-j][0] <= x <= bot_blt[i-j][0]+blt_x or bot_blt[i-j][0] <= x+int(X / 15) <= bot_blt[i-j][0]+blt_x or x <= bot_blt[i-j][0] <= x+int(X / 15) or x <= bot_blt[i-j][0]+blt_x <= x+int(X / 15))\
            and (bot_blt[i-j][1] <= plr_Y <= bot_blt[i-j][1]+blt_y or bot_blt[i-j][1] <= plr_Y+int(Y / 50) <= bot_blt[i-j][1]+blt_y):
            bot_blt.pop(i-j)
            j+=1
            plr_lvs-=1

    scr += 0.01
    pygame.display.flip()


def stop():
    if X-int(X/35)-int(X/15) < x:
        return X-int(X/35)-X/15
    elif int(X/35) > x:
        return int(X/35)
    return x


def shoot(evnt):
    global blt
    if (evnt.key == pygame.K_SPACE or evnt.key == pygame.K_w) and (len(l_blt)==0 or l_blt[len(l_blt)-1][1]+blt_y<=plr_Y - int(X/35)):
        l_blt.append([x + int(X / 30 - X / 300), plr_Y-blt_y])
        blt+=1


def movement(evt, arw, k, add):
    global x, brk
    if evt.key == arw or evt.key == k:  # LEFT
        while True:
            for event2 in pygame.event.get():
                if event2.type == pygame.KEYUP:
                    shoot(event2)
                    if event2.key == arw or event2.key == k:
                        brk = True
            if brk == True:
                break
            refresh()
            x += add
            x = stop()


#MAIN

pygame.draw.rect(screen, dark_blue(), pygame.Rect(0, 0, X+blt_x, Y+blt_y))
for i in range(30):
    pygame.draw.rect(screen, white(), pygame.Rect(rx[i], ry[i], int(X/300), int(X/300)))
prt("Difficulty", int(X/2), int(Y/5), f_sz=int(X/35))
prt("1) Easy", int(X/2), int(2*Y/5), f_sz=int(X/35))
prt("2) Medium", int(X/2), int(3*Y/5), f_sz=int(X/35))
prt("3) Hard", int(X/2), int(4*Y/5), f_sz=int(X/35))
pygame.display.flip()
brk=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                blt_spd = X/910     # acc3l3ration (per 1 frame)
                sht_spd = 300       # 1 sh00t/___frames for b0ts
                plr_lvs = 4
                brk = True
            elif event.key == pygame.K_2:
                blt_spd = X/780     # acc3l3ration (per 1 frame)
                sht_spd = 250       # 1 sh00t/___frames for b0ts
                plr_lvs = 3
                brk = True
            elif event.key == pygame.K_3:
                blt_spd = X/643     # acc3l3ration (per 1 frame)
                sht_spd = 200       # 1 sh00t/___frames for b0ts
                plr_lvs = 2
                brk = True
            elif event.key == pygame.K_4:
                blt_spd = X / 643   # acc3l3ration (per 1 frame)
                sht_spd = 200       # 1 sh00t/___frames for b0ts
                plr_lvs = 1000
                b = True
                brk = True
            elif event.key == pygame.K_ESCAPE:
                exit()
    if brk == True:
        break

pygame.draw.rect(screen, dark_blue(), pygame.Rect(0, 0, X+blt_x, Y+blt_y))
for i in range(30):
    pygame.draw.rect(screen, white(), pygame.Rect(rx[i], ry[i], int(X/300), int(X/300)))
prt("| SPACE INVADERS |", int(X/2), int(Y/3), f_sz=int(X/35))
prt("Press any key to start...", int(X/2), int(2*Y/3), f_sz=int(X/35))
pygame.display.flip()
while True:
    brk=False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            else:
                brk=True
    if brk==True:
        break

for i in range(3, 0, -1):
    refresh()
    prt(str(i), int(X/2), int(Y/2), f_sz=int(X/20))
    pygame.display.flip()
    time.sleep(0.5)
refresh()
prt("GO!!", int(X/2), int(Y/2), f_sz=int(X/20))
pygame.display.flip()
time.sleep(0.25)

while True:
    brk=False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            movement(event, pygame.K_a, pygame.K_LEFT, -add)

            movement(event, pygame.K_d, pygame.K_RIGHT, add)

            shoot(event)
            # Settings
            if event.key == pygame.K_s or event.key == pygame.K_RETURN:
                while True:
                    pygame.draw.rect(screen, dark_blue(), pygame.Rect(0, 0, X+blt_x, Y+blt_y))
                    prt("Settings",                             int(X/2), int(Y/9), f_sz=int(X/25))
                    prt("Controls",                             int(X/8), int(2*Y/9), f_sz=int(X/45))
                    prt("SPACEBAR or W to Shoot",               int(X/8), int(3*Y/9), f_sz=int(X/55))
                    prt("<-- or A          D or -->",           int(X/8), int(4*Y/9), f_sz=int(X/55))
                    prt("Esc to exit",                          int(X/8), int(5*Y/9), f_sz=int(X/55))
                    prt("Enter to continue",                    int(X/8), int(6*Y/9), f_sz=int(X/55))
                    prt("Stats",                                int(7*X/8), int(2 * Y / 9), f_sz=int(X / 45))
                    prt("Your Score: " + str(int(scr)),         int(7 * X / 8), int(3 * Y / 9), f_sz=int(X / 55))
                    prt("Ammo Used: " + str(blt),               int(7 * X / 8), int(4 * Y / 9), f_sz=int(X / 55))
                    prt("Ammo Wasted: " + str(wst),             int(7 * X / 8), int(5 * Y / 9), f_sz=int(X / 55))
                    prt("Lives: " + str(plr_lvs),               int(7 * X / 8), int(6 * Y / 9), f_sz=int(X / 55))
                    prt("Bots Destroyed: " + str(len(dead)),    int(7 * X / 8), int(7 * Y / 9), f_sz=int(X / 55))
                    prt("Space Invaders v2.0", int(X / 2), int(8 * Y / 9), f_sz=int(X / 45))
                    pygame.display.flip()
                    for event2 in pygame.event.get():
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_ESCAPE:
                                exit()
                            if event2.key == pygame.K_RETURN or event2.key == pygame.K_s:
                                brk=True
                                break
                    if brk==True:
                        break

    if 150*a<=int(scr)<1000:
        a+=1
        var_x+= int(X/1366*(10**-2)) # 0.01
        var_y+= int(X/2732*(10**-2)) # 0.005
    if int(sht_spd)>50:
        sht_spd-=2*(10**-4) # 0.0002

    if len(l_bots)!=0:
        j = 0
        for i in range(6):
            if l_bots[i][1] == 0:
                j += 1
        for i in range(6):
            if j == 6:
                l_bots.pop(0)

    for i in range(len(l_bots)):
        if l_bots[i][1]==0 and l_bots[i] not in dead:
            dead.append(l_bots[i])

    if plr_lvs==0:
        pygame.draw.rect(screen, dark_blue(), pygame.Rect(0, 0, X + blt_x, Y + blt_y))
        prt("Score: " + str(int(scr)),                              int(X / 2), int(Y / 5), f_sz=int(X / 30))
        prt("Bots Destroyed: " + str(len(dead)),                    int(X / 2), int(2 * Y / 5), f_sz=int(X / 30))
        prt("Bullets Used: " + str(blt) + ", Wasted: " + str(wst),  int(X / 2), int(3 * Y / 5), f_sz=int(X / 30))
        prt("Space Invaders v2.0",                                  int(X / 2), int(4 * Y / 5), f_sz=int(X / 30))
        pygame.display.flip()
        time.sleep(2)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    exit()
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_ESCAPE:
            exit()

    print(int(scr))

    refresh()
