"""
This is Still UNDER DEVELOPMENT
"""

import pygame, sys, time, random

#To Solve
"""

"""

#Functions

#Colours
def blue(): return 25, 25, 112
def red(): return 250, 0, 0
def green(): return 148, 216, 17
def yellow(): return 250, 250, 0
def white(): return 255, 255, 255
def black(): return 0, 0, 0

pygame.init()

def restart():

        #CONSTANTS
    global X, a, screen, font, st_pos

    X = 600
    a = int(X / 15)
    st_pos = 2, 15, 39, 26
    font = pygame.font.Font('freesansbold.ttf', 32)
    screen = pygame.display.set_mode((a*25, a*15))

        #variables
    global d_plr, turn

    turn=0
    d_plr = {"clr": [green(), yellow(), blue(), red()], "n_pos": []}
    for i in range(4):
        lst=[]
        for j in range(4):
            lst.append(-st_pos[i])
        d_plr["n_pos"].append(lst)

    refresh()


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


def n_to_g():

    refresh()
    for plr in range(len(d_plr["n_pos"])):
        for piece in range(len(d_plr["n_pos"][plr])):

            clr = d_plr["clr"][plr]
            n_pos = d_plr["n_pos"][plr][piece] # Numerical Position

            if clr==green() and n_pos==58:
                print(n_pos)
                g_pos = [6, 7]
            elif clr==yellow() and n_pos==69:
                print(n_pos)
                g_pos = [7, 6]
            elif clr==red() and n_pos==84:
                print(n_pos)
                g_pos = [8, 7]
            elif clr==blue() and n_pos==97:
                print(n_pos)
                g_pos = [7, 8]


            if clr==green() and n_pos>=52:
                if n_pos>58:
                    n_pos-=dice
                g_pos = [(n_pos+2)%6, 7]
            elif clr==yellow() and n_pos>=64:
                if n_pos>69:
                    n_pos-=dice
                g_pos = [7, (n_pos+3)%6]
            elif clr==red() and n_pos>=79:
                if n_pos>84:
                    n_pos-=dice
                g_pos = [14-(n_pos%6), 7]
            elif clr==blue() and n_pos>=92:
                if n_pos>97:
                    n_pos-=dice
                g_pos = [7, 14-(n_pos-1)%6]

            elif n_pos >= 53:
                n_pos -= 52

            if 1<=n_pos<=6:
                g_pos = [(n_pos-1)%6, 6]
            elif 7<=n_pos<12:
                g_pos = [6, 6-n_pos%6]
            elif n_pos==12:
                g_pos = [6, 0]
            elif n_pos==13:
                g_pos = [7, 0]
            elif 14<=n_pos<=19:
                g_pos = [8, (n_pos-2)%6]
            elif 20<=n_pos<=25:
                g_pos = [9+(n_pos-2)%6, 6]
            elif n_pos==26:
                g_pos = [14, 7]
            elif 27<=n_pos<=32:
                g_pos = [14-(n_pos-3)%6, 8]
            elif 33<=n_pos<=38:
                g_pos = [8, 9+(n_pos-3)%6]
            elif n_pos==39:
                g_pos = [7, 14]
            elif 40<=n_pos<=45:
                g_pos = [6, 14-(n_pos-4)%6]
            elif 46<=n_pos<=51:
                g_pos = [5-(n_pos-4)%6, 8]
            elif n_pos==52:
                g_pos = [0, 7]

            if n_pos>0:
                pygame.draw.circle(screen, d_plr["clr"][plr], [a*g_pos[0]+int(a/2), a*g_pos[1] + int(a/2)], int((3.5*a)/9))
                pygame.draw.circle(screen, white(), [a*g_pos[0]+int(a/2), a*g_pos[1] + int(a/2)], int((3.5*a)/9), 1)

    pygame.display.flip()


def f_dice():
    global turn
    plr=turn
    brk=False


    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    n_to_g()
                    dice=random.randrange(1, 7)
                    pygame.draw.rect(screen, black(), pygame.Rect(a*15, 0, a*25, a*25))
                    g_print("Dice: " + str(dice), a*20, int((a*15)/5))
                    pygame.display.flip()
                    brk=False
                    piece=-1

                    if dice==6:                                               # Dice rolls 6
                        if d_plr["n_pos"][plr][0]<0:                          # No pieces in board
                            d_plr["n_pos"][plr][0]*=-1
                            piece=0

                        elif d_plr["n_pos"][plr][0]>0:                        # 1 or more pieces in board

                            while True:
                                for event1 in pygame.event.get():
                                    if event1.type == pygame.KEYDOWN:
                                        g_print("Enter Piece: ", a*20, a*6)
                                        pygame.display.flip()
                                        if 48 < event1.key < 58:
                                            if d_plr["n_pos"][plr][int(chr(event1.key-1))]<0:
                                                d_plr["n_pos"][plr][int(chr(event1.key-1))]*=-1
                                            else:
                                                d_plr["n_pos"][plr][int(chr(event1.key-1))]+=dice
                                            piece=int(chr(event1.key-1))
                                            brk=True
                                if brk==True:
                                    brk=False
                                    break

                    else:                                                     # Dice doesn't roll 6
                        if d_plr["n_pos"][plr][0]>0:
                            num=0
                            for i in range(4):
                                if d_plr["n_pos"][plr][i]>0:
                                    num+=1
                            if 4>num>1:                                       # Multiple pieces in board
                                g_print("Enter Piece: ", a*20, a*6)
                                pygame.display.flip()
                                while True:
                                    for event1 in pygame.event.get():
                                        if event1.type == pygame.KEYDOWN:
                                            if 48 < event1.key < 58 and d_plr["n_pos"][plr][int(chr(event1.key-1))] > 0:
                                                d_plr["n_pos"][plr][int(chr(event1.key-1))]+=dice
                                                piece=int(chr(event1.key-1))
                                                brk=True
                                    if brk==True:
                                        brk=False
                                        break

                            else:                                             # 1 piece in board
                                d_plr["n_pos"][plr][0]+=dice

                    if d_plr["n_pos"][plr][piece] > 50+st_pos[plr] and piece!=-1:
                        d_plr["n_pos"][plr][piece]-=dice

                    if dice==6:
                        f_dice()

                    turn=(turn+1)%4


def refresh():


    for i in range(15):
        for j in range(15):
            pygame.draw.rect(screen, white(), pygame.Rect(j*a, i*a, a, a))

    pygame.draw.rect(screen, d_plr["clr"][0], pygame.Rect(a,   7*a, 5*a, a))
    pygame.draw.rect(screen, d_plr["clr"][1], pygame.Rect(7*a, a,   a,   5*a))
    pygame.draw.rect(screen, d_plr["clr"][2], pygame.Rect(7*a, 9*a, a,   5*a))
    pygame.draw.rect(screen, d_plr["clr"][3], pygame.Rect(9*a, 7*a, 5*a, a))

    pygame.draw.rect(screen, d_plr["clr"][0], pygame.Rect(a, 6*a, a, a))
    pygame.draw.rect(screen, d_plr["clr"][1], pygame.Rect(8*a, a, a, a))
    pygame.draw.rect(screen, d_plr["clr"][2], pygame.Rect(6*a, 13*a, a, a))
    pygame.draw.rect(screen, d_plr["clr"][3], pygame.Rect(13*a, 8*a, a, a))

    for i in range(15):
        for j in range(15):
            pygame.draw.rect(screen, black(), pygame.Rect(j*a, i*a, a, a), 1)

    pygame.draw.rect(screen, d_plr["clr"][1], pygame.Rect(9*a, 0, 6*a, 6*a))
    pygame.draw.rect(screen, d_plr["clr"][2], pygame.Rect(9*a, 9*a, 6*a, 6*a))
    pygame.draw.rect(screen, d_plr["clr"][3], pygame.Rect(0, 9*a, 6*a, 6*a))

    k=0
    for i in range(2):
        for j in range(2):
            pygame.draw.rect(screen, d_plr["clr"][i+j+k], pygame.Rect(a*9*j, a*9*i, a*6, a*6))
            pygame.draw.rect(screen, white(), pygame.Rect((a*9*j) + a, (a*9*i) + a, a*4, a*4))
            pygame.draw.rect(screen, black(), pygame.Rect(a*9*j, a*9*i, a*6, a*6), 1)

            pygame.draw.polygon(screen, d_plr["clr"][0], [(6*a, 6*a), (int(7.5*a), int(7.5*a)), (6*a, 9*a)])
            pygame.draw.polygon(screen, d_plr["clr"][1], [(6*a, 6*a), (int(7.5*a), int(7.5*a)), (9*a, 6*a)])
            pygame.draw.polygon(screen, d_plr["clr"][2], [(6*a, 9*a), (int(7.5*a), int(7.5*a)), (9*a, 9*a)])
            pygame.draw.polygon(screen, d_plr["clr"][3], [(9*a, 6*a), (int(7.5*a), int(7.5*a)), (9*a, 9*a)])

            pygame.draw.polygon(screen, black(), [(6*a, 6*a), (int(7.5*a), int(7.5*a)), (6*a, 9*a)], 1)
            pygame.draw.polygon(screen, black(), [(6*a, 6*a), (int(7.5*a), int(7.5*a)), (9*a, 6*a)], 1)
            pygame.draw.polygon(screen, black(), [(6*a, 9*a), (int(7.5*a), int(7.5*a)), (9*a, 9*a)], 1)
            pygame.draw.polygon(screen, black(), [(9*a, 6*a), (int(7.5*a), int(7.5*a)), (9*a, 9*a)], 1)

            if i+j+k == turn:
                pygame.draw.rect(screen, d_plr["clr"][turn], pygame.Rect((a*9*j) + int(a*9/8), (a*9*i) + int(a*9/8), int(a*15/4), int(a*15/4)), 5)

            for l in range(2):
                for m in range(2):
                    pygame.draw.circle(screen, d_plr["clr"][i+j+k], [(a*9*j) + a*2 + (a*2*m), (a*9*i) + a*2 + (a*2*l)], int(a/2))
        k+=1

    pygame.draw.rect(screen, black(), pygame.Rect(0, 0, a*15, a*15), 3)

    pygame.display.flip()



def py_exit():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

#MAIN

restart()

while True:
    f_dice()
    py_exit()
