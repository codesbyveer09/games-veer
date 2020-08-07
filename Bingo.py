import pygame, sys

pygame.init()
white = (255,255,255)
black = (0,0,0)
blue = (0,0,250)
red = (250,0,0)
green = (0,250,0)
yellow = (250,250,0)
a = 80
z=0
plr=1
my_lst=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

#POSITION INPUT
def pos(inp, plr):
    j=0
    for i in my_lst[inp]:
        if i == 0:
            my_lst[inp][j]=plr
            break
        j=j+1


def end():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Plr " + str(plr) + " WINS", True, yellow, black)
    textRect = text.get_rect()
    textRect.center = (1000, 200)
    screen.blit(text, textRect)
    pygame.display.flip()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
for y in range(6):
    for x in range(7):
        pygame.draw.rect(screen, white, pygame.Rect(x * a + a, y * a + a, a, a))
        pygame.draw.rect(screen, black, pygame.Rect(x * a + a, y * a + a, a, a), 1)

pygame.display.flip()

#PLAYER TURN
while True:
    for event in pygame.event.get():
        inp = 0

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Plr " + str(plr) + "'s Turn", True, yellow, black)
        textRect = text.get_rect()
        textRect.center = (1000, 100)
        screen.blit(text, textRect)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                inp=1
            elif event.key == pygame.K_2:
                inp=2
            elif event.key == pygame.K_3:
                inp=3
            elif event.key == pygame.K_4:
                inp=4
            elif event.key == pygame.K_5:
                inp=5
            elif event.key == pygame.K_6:
                inp=6
            elif event.key == pygame.K_7:
                inp=7
            elif event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                sys.exit()

            if inp > 0 and inp < 8:
                pos(inp-1, plr)

                # GUI GRID
                for y in range(7):
                    for x in range(6):
                        if my_lst[y][x]!=0:
                            if my_lst[y][x]==1:
                                iclr=blue
                            elif my_lst[y][x]==2:
                                iclr=red
                            pygame.draw.circle(screen, iclr, [int(a*y-a/2+2*a), int((a*7)-((a*x)+a/2))], int(a/2-2))

                pygame.display.flip()

                # Check
                for j in range(7):                      # |
                    num = 0
                    for k in range(6):
                        if my_lst[j][k] == plr:
                            num = num + 1
                        else:
                            num=0
                        if num>=4:
                            end()


                for j in range(6):                      # --
                    num = 0
                    for k in range(7):
                        if my_lst[k][j] == plr:
                            num = num + 1
                        else:
                            num=0
                        if num>=4:
                            end()

                num = 0

                #for j in range()
                for k in range(0,4):
                    if my_lst[k][3-k]==plr:
                        num = num + 1
                    else:
                        num = 0
                    if num>=4:
                        end()

                """                for m in range(3):
                        for j in range(7):              # \
                            if my_lst[j][-j+m] == plr:
                                num = num + 1
                            else:
                                num = 0
                            if num >= 4:
                                end()

                num = 0                                 # /
                for m in range(4):
                    for j in range(6):
                        if my_lst[j][j-m] == plr:
                            num = num + 1
                        else:
                            num = 0
                        if num >= 4:
                            end()"""

                t=0
                for j in range(7):                      # Tie
                    for k in range(6):
                        if my_lst[j][k] == 0:
                            t=t+1
                if t == 0:
                    sys.exit(5)

                z=z+1
                plr=(z%2)+1

if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
    sys.exit()