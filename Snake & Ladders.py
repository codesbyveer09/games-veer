import pygame, sys, random


"""
RULES
Snake_and_ladders v1.0
Download Pygame module if not present
reach 100 to win
Game under development
"""
lst=[]
lst.append("Esc for exit")
lst.append("Spacebar for rolling dice")
lst.append("Red lines indicates snakes")
lst.append("Green lines indicates ladder")

#Variables
pygame.init()
white = (255,255,255)
black = (0,0,0)
blue = (65,184,131)
red = (250,0,0)
green = (0,250,0)
yellow = (250,250,0)
a=65
l_pos=[]
l_x=[]
l_y=[]
l_clr=[blue, red, green, yellow]
l_done=[]
l_sklr=[]

for i in range(4):
    l_sklr.append([0, 0, 0, 0, 0, 0, 0])

#Player Listing
while True:
    tl_plr=int(input("Total number of players: "))
    if tl_plr >= 2 and tl_plr <= 6:
        break

for i in range(tl_plr):
    l_pos.append(1)
    l_x.append(0)
    l_y.append(0)
print(l_pos)

font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Defining Functions

def pos(i_pos):
    t_pos = i_pos-1
    d1=int(t_pos/10)
    d2=t_pos%10
    if d1%2 == 1:
        plc_y = int((10.5- d2) * (a))-10
    else:
        plc_y = int((d2 + 1.5) * (a))-10
    plc_x = int((10.5-d1)*(a))
    return [plc_y, plc_x]


def prt(str, plc_x, plc_y, clr):
    text = font.render(str, True, clr, black)
    textRect = text.get_rect()
    textRect = (plc_x, plc_y)
    screen.blit(text, textRect)


def end(wnr):
    pygame.draw.rect(screen, black, pygame.Rect(0, 0, 10000, 10000))
    for i in range(tl_plr):
        prt("PLR " + str(i + 1) + ": " + str(l_pos[i]), 1000, 100 + (i * 50), l_clr[i])

        prt("PLAYER: " + str(wnr+1) + " WINS !!!   : ) : )", 100, 100, l_clr[wnr])
    pygame.display.flip()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()


def board(num_plr):
    n = 10
    m = -1
    for y in range(10):

        if n == 10:
            m = -1
            l = 1
        else:
            m = 1
            l = 0
        for x in range(10):
            x_ = x * a + a
            y_ = y * a + a
            n = n + m

            pygame.draw.rect(screen, white, pygame.Rect(x_, y_, a, a))
            pygame.draw.rect(screen, black, pygame.Rect(x_, y_, a, a), 1)

            text = font.render(str(100 - ((y + 1) * 10) + n + l), True, black, white)
            textRect = text.get_rect()
            textRect.center = (int(x_+a/2), int(y_ + a/2))
            screen.blit(text, textRect)

    for j in range(7):
        r = pos(l_sklr[0][j])
        s = pos(l_sklr[1][j])
        pygame.draw.line(screen, green, r, s, 10)

        r = pos(l_sklr[2][j])
        s = pos(l_sklr[3][j])
        pygame.draw.line(screen, red, r, s, 5)

    j=num_plr-1
    for k in range(7):
        if l_pos[j] == l_sklr[1][k]:
            l_pos[j] = l_sklr[0][k]
            break

        elif l_pos[j] == l_sklr[2][k]:
            l_pos[j] = l_sklr[3][k]
            break

    b=int(-20/tl_plr)
    for j in range(tl_plr):
        t_pos = l_pos[j]-1
        d1=int(t_pos/10)
        d2=t_pos%10
        if d1%2 == 1:
            plc_y = int((10.5- d2) * (a))
        else:
            plc_y = int((d2 + 1.5) * (a))
        plc_x = int((10.5-d1)*(a))
        pygame.draw.circle(screen, l_clr[j], [plc_y+b, plc_x], int(a/4))

        b=b+int(20/tl_plr)

    pygame.display.flip()

for i in range(4):
    prt(lst[i], 800, 500 + (i * 50), white)

#Snakes and ladders
while True:
    for i in range(2):
        for i in range(7):
            while True:
                grlmt = random.randrange(5, 101)
                if grlmt > 27 and grlmt not in l_done:
                    break
            l_done.append(grlmt)

            while True:
                lrlmt = random.randrange(5, 101)
                if lrlmt < grlmt - 20 and lrlmt not in l_done:
                    break
            l_done.append(lrlmt)

    print(l_done)

    k = 0
    for i in range(7):
        for j in range(4):
            l_sklr[j][i] = l_done[k]
            k = k + 1

    print(l_sklr)

    # MAIN PROGRAM

    num_plr = 1
    board(num_plr)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    rdm = random.choice([1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 6])

                    prt("DICE: " + str(rdm), 950, 100, yellow)
                    prt("LAST TURN: " + str(num_plr), 900, 200, white)
                    l_pos[num_plr - 1] = l_pos[num_plr - 1] + rdm
                    for i in range(4):
                        prt(lst[i], 800, 500+(i*50), white)

                    for i in range(tl_plr):
                        text = font.render("PLR " + str(i + 1) + ": " + str(l_pos[i]), False, l_clr[i], black)
                        textRect = text.get_rect()
                        textRect.center = (1000, 300 + (i * 50))
                        screen.blit(text, textRect)
                        if l_pos[i] >= 100:
                            end(i)

                    pygame.display.flip()

                    board(num_plr)
                    num_plr = num_plr % tl_plr
                    num_plr = num_plr + 1

                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    sys.exit("EXIT")