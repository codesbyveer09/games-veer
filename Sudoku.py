import pygame, random, time


#Colours
def blue(): return 64, 224, 208
def red(): return 250, 0, 0
def green(): return 148, 216, 17
def yellow(): return 250, 250, 0
def white(): return 255, 255, 255
def black(): return 0, 0, 0

c1=white()
c2=black()
c3=50, 213, 219
c4=black()
c5=0, 41, 132

extreme = 24
hard = 26
medium = 35
easy = 44
diff = extreme

pygame.init()


def g_print(v_nm, x_var, y_var, f_clr = white(), bg_clr=None, f_sz=10, b_center=True):
    global font
    if bg_clr==None:
        text = font.render(v_nm, True, f_clr)
    else:
        text = font.render(v_nm, True, f_clr, bg_clr)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    if b_center == True:
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    screen.blit(text, textRect)


def restart():
    # CONSTANTS

    global X, a, screen, font

    X=600
    a=int(X/9)
    screen = pygame.display.set_mode((a*9, a*9))
    font = pygame.font.Font('freesansbold.ttf', int(a*2/3))

    # variables

    global l_pos

    l_pos=[]
    num=0

    for i in range(9):
        m=[]
        for j in range(9):
            m.append([0, False])
        l_pos.append(m)
    for i in range(diff):
        r1=8
        r2=5

        while l_pos[r2][r1][0] != 0:
            r1=random.randrange(0, 9)
            r2=random.randrange(0, 9)
        grid_maker(r1, r2, False)

def grid_maker(x, y, bool):
    while True:
        r_num=random.randrange(1, 10)
        brk=False
        bool_4_brk=0
        for i in range(3):
            for j in range(3):
                if r_num==l_pos[(y-y%3)+i][(x-x%3)+j][0]:
                    brk=True
                    bool_4_brk+=1
                    break
            if brk==True:
                break

        for i in range(9):
            for j in range(9):
                if r_num==l_pos[y][j][0]:
                    brk=True
                    bool_4_brk+=1
                    break

                if r_num==l_pos[i][x][0]:
                    brk=True
                    bool_4_brk+=1
                    break

            if brk==True:
                break

        if bool_4_brk==3:
            return 1
        elif bool == True:
            return
        if brk==False:
            l_pos[y][x][0]=r_num
            return


def refresh(cell=None):

    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, c1, pygame.Rect(j*a, i*a, a, a))
            pygame.draw.rect(screen, c2, pygame.Rect(j*a, i*a, a, a), 1)

            if l_pos[i][j][0]!=0:
                if l_pos[i][j][1] == True:
                    g_print(str(l_pos[i][j][0]), a*j+int(a/2), a*i+int(a/2), f_clr=c5)
                else:
                    g_print(str(l_pos[i][j][0]), a*j+int(a/2), a*i+int(a/2), f_clr=c4)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, c2, pygame.Rect(j*a*3, i*a*3, a*3, a*3), 3)

    for i in range(9):
        for j in range(9):
            if cell!=None:
                if cell==(i, j):
                    pygame.draw.rect(screen, c3, pygame.Rect(i*a, j*a, a, a), 5)


    pygame.display.flip()

# Main
restart()
refresh()

while True:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            click = int((click[0] - click[0]%a)/a), int((click[1] - click[1]%a)/a)

            for i in range(9):
                for j in range(9):
                    if j == click[0] and i == click[1]:
                        if event.button == 1 and l_pos[i][j][0] == 0:
                            refresh(cell=click)
                            brk=False
                            while True:
                                for event1 in pygame.event.get():
                                    if event1.type == pygame.KEYDOWN:
                                        if 49 <= event1.key <= 57:
                                            l_pos[i][j]=[chr(event1.key), True]
                                            refresh()
                                            brk=True
                                            break
                                    if event1.type==pygame.QUIT:
                                        pygame.quit()
                                        exit()
                                if brk==True:
                                    brk=False
                                    break

                        elif event.button == 3 and l_pos[i][j][0] != 0 and l_pos[i][j][1] == True:
                            l_pos[i][j]=[0, False]
                            refresh()


            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    for i in range(9):
        for j in range(9):
            grid_maker(i, j, True)
