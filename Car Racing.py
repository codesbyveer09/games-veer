import sys, random, pygame, clr, time

# CONSTANTS
X = 1366
Y = 768
d_OBJ = {"car": [0.75, 1, True], "bike": [0.5, 1.5, True], "truck": [1.2, 0.75, True]}
crclr = clr.red()

# variables
x = int(X/2-int((X / 9) * d_OBJ["car"][0])/2)
y = Y-int((Y / 4.5) * d_OBJ["car"][0])
l=3
add = 4
spd = 2
num=0
j=0
lst=[]
rlst=[random.randrange(1, 3), random.randrange(3, 6)]

for i in range(2):
    r=random.choice(["car", "bike", "truck"])
    r1=rlst[i]
    lst.append([r, r1, -int((X / 4.5) * d_OBJ[r][0]), clr.rdm()])
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# Functions


def crash():
    global l, x, y, lst
    for i in range(len(lst)):
        if     (x >= int(lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2) \
            and x <= (int(lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2)) + int((X / 9) * d_OBJ[lst[i][0]][0])) \
            or (x + int((X / 9) * d_OBJ["car"][0]) >= int(lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2) \
            and x + int((X / 9) * d_OBJ["car"][0]) <= (int(lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2)) + int((X / 9) * d_OBJ[lst[i][0]][0]))\
            or (x <= int(lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2)
            and x + int((X / 9) * d_OBJ["car"][0]) >= (int(lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2)) + int((X / 9) * d_OBJ[lst[i][0]][0])):
            if     (y >= int(lst[i][2]) and y <= int(lst[i][2]) + int((Y / 4) * d_OBJ[lst[i][0]][0]))\
                or (y <= int(lst[i][2]) and y >= int(lst[i][2]) + int((Y / 4) * d_OBJ[lst[i][0]][0]))\
                or (y + int((X / 9) * d_OBJ["car"][0]) >= int(lst[i][2]) and y + int((X / 9) * d_OBJ["car"][0]) <= int(lst[i][2]) + int((Y / 4) * d_OBJ[lst[i][0]][0]))\
                or (y + int((X / 9) * d_OBJ["car"][0]) <= int(lst[i][2]) and y + int((X / 9) * d_OBJ["car"][0]) >= int(lst[i][2]) + int((Y / 4) * d_OBJ[lst[i][0]][0])):
                if l == 0:
                    prt("You Crashed, press ESC to exit", X/2, Y/2, f_clr=clr.blue(), f_sz=50)
                else:
                    prt("You Crashed, press ENTER to continue", X/2, Y/2, f_clr=clr.blue(), f_sz=50)
                while True:
                    for event3 in pygame.event.get():
                        if event3.type == pygame.KEYDOWN:
                            if event3.key == pygame.K_ESCAPE:
                                exit()
                            if event3.key == pygame.K_RETURN:
                                if l==0:
                                    l=3
                                    num=0
                                    spd=2
                                    return
                                l-=1
                                x = int(X / 2 - int((X / 9) * d_OBJ["car"][0]) / 2)
                                y = Y - int((Y / 4.5) * d_OBJ["car"][0])
                                r = random.randrange(1, 3)
                                r1 = r + random.randrange(1, 3)
                                lst = [["truck", r, 0, clr.rdm()], ["bike", r1, 0, clr.rdm()]]
                                spd = 2
                                return


def prt(v_nm, x_var, y_var, tilt=0, f_clr=clr.white(), bg_clr=None, f_sz=10, b_center=True):
    font = pygame.font.Font('freesansbold.ttf', f_sz)
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


def clear():
    pygame.draw.rect(screen, clr.black(), pygame.Rect(0, 0, X, Y))
    pygame.draw.rect(screen, clr.grey(), pygame.Rect(int(X / 7), 0, int((5 * X) / 7), Y))
    for i in range(1, 7):
        pygame.draw.line(screen, clr.white(), (i * int(X / 7), 0), (int(i * int(X / 7)), int(Y)), 6)
    for i in range(len(lst)):
        pygame.draw.rect(screen, lst[i][3], pygame.Rect(
            int((lst[i][1] * int(X / 7)) + int(X / 14) - (int(X / 9) * d_OBJ[lst[i][0]][0]/2)), int(lst[i][2]),
            int((X / 9) * d_OBJ[lst[i][0]][0]), int((Y / 4) * d_OBJ[lst[i][0]][0])))
    pygame.draw.rect(screen, crclr, pygame.Rect(int(x), int(y), int((X / 9) * d_OBJ["car"][0]), int((Y / 4.5) * d_OBJ["car"][0])))
    prt("Score: " + str(int(num)), X / 14, Y / 12, f_sz=20)
    prt("Lives: " + str(l), X/14, Y/8, f_sz=20)
    prt("Speed: " + str(int(spd)), X/14, Y/6, f_sz=20)
    crash()
    pygame.display.flip()


def stop(axis):
    if axis == "x":
        if int(X / 7) + 1 > x:
            return int(X / 7) + 1
        elif x > int(6 * X / 7)-int((X / 9) * d_OBJ["car"][0]):
            return int(6 * X / 7)-int((X / 9) * d_OBJ["car"][0])
        return x
    elif axis == "y":
        if 0 > y:
            return 0
        elif y > Y-int((X / 9) * d_OBJ["car"][0]):
            return Y-int((X / 9) * d_OBJ["car"][0])
        return y


def arw_keys(add, axis, key):

        global brk, num, j, spd
        if key == "a":
            k_lst=[pygame.K_a, pygame.K_LEFT]
        if key == "d":
            k_lst = [pygame.K_d, pygame.K_RIGHT]
        if key == "w":
            k_lst = [pygame.K_w, pygame.K_UP]
        if key == "s":
            k_lst = [pygame.K_s, pygame.K_DOWN]

        while True:
            if axis == "x":
                global x
                axis1 = x
            else:
                global y
                axis1 = y
            for event2 in pygame.event.get():
                crash()
                if event2.type == pygame.KEYUP:
                    if event.key == k_lst[0] or event.key == k_lst[1]:
                        brk = True
            if brk == True:
                break
            axis1 += add
            num += 0.01
            if int(num) == j * 100:
                j += 1
                spd += 0.2
            for i in range(len(lst)):
                lst[i][2] += spd * d_OBJ[lst[i][0]][1]
            if axis == "x":
                x=axis1
                x=stop("x")
            else:
                y=axis1
                y=stop("y")
            clear()


pygame.init()
clear()
brk=False
prt("Press any key to start", X/2, Y/2, f_sz=50)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                brk=True
    if brk==True:
        break

for i in range(3, 0, -1):
    clear()
    prt(str(i), X/2, Y/2, f_sz=100)
    pygame.display.flip()
    time.sleep(0.5)
clear()
prt("GO!!", X/2, Y/2, f_sz=100)
pygame.display.flip()
time.sleep(0.5)
clear()

# MAIN

while True:
    brk = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_a or event.key == pygame.K_LEFT:     # LEFT
                arw_keys(-add, "x", "a")

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:   # RIGHT
                arw_keys(add, "x", "d")

            elif event.key == pygame.K_w or event.key == pygame.K_UP:     # UP
                arw_keys(-add, "y", "w")

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:     # UP
                arw_keys(add, "y", "s")

            elif event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                exit()
    for i in range(len(lst)):
        lst[i][2] += spd * d_OBJ[lst[i][0]][1]
    clear()

    rnum = random.randrange(3, 6)
    for i in range(len(lst)):
        if lst[i][2] >= rnum * Y / 7 and len(lst) == 2:
            while True:
                r1 = random.choice(["car", "car", "car", "car", "car", "car", "bike", "bike", "bike", "truck"])
                r2 = random.randrange(1, 6)
                if (d_OBJ[r1][1] <= d_OBJ[lst[0][0]][1] or r2 != lst[0][1]) and r2 not in lst[1]:
                    lst.append([r1, r2, -int((X / 4.5) * d_OBJ[r1][0]), clr.rdm()])
                    break
        elif lst[i][2] >= Y:
            lst.pop(i)
            break

        crash()

    num+=0.015

    if int(num)==j*100:
        j+=1
        spd+=0.2