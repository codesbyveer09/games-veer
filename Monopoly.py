import pygame, sys, random, csv
from pprint import pprint
LEFT = 0
RIGHT = 1
CENTER = 2
pygame.init()
tl_plrs=4
l_bght=[]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
a=60
dict={}
l_keys=[]
l_stn=["Chennai Rail", "Howrah Railway", "Delhi Railway", "Chatrapati Shivaji"]
out=[]


l_clr={"blue" : (25,25,112), "red" : (250,0,0), "green" : (0,250,0), "yellow" : (250,250,0), "pink" : (255,20,147),
       "orange" : (255,140,0), "brown" : (139,69,19), "light blue" : (135,206,250), "light green" :
       (144,238,144), "white" : (255,255,255), "black" : (0,0,0), "grey" : (192,192,192)}

d_plrs={"Pos" : [], "Money" : [], "Cards" : [], "Clr" : []}
clrs = list(l_clr.keys())

for i in range(tl_plrs):
    d_plrs["Pos"].append(0)
    d_plrs["Money"].append(1500)
    d_plrs["Cards"].append([])
    d_plrs["Clr"].append(l_clr[clrs[i]])


def owner(crd, coord):
    for i in range(tl_plrs):
        if crd in d_plrs["Cards"][i]:
            pygame.draw.polygon(screen, d_plrs["Clr"][i], coord)

def cokri_pos(plr, b):
    clr=d_plrs["Clr"][plr]
    pos=d_plrs["Pos"][plr]


    if 0 <= pos < 10:                 #Down
        pygame.draw.circle(screen, clr, [int((11-pos+1/2) * a), (12*a)+b], int(a / 6))

    elif 10 <= pos < 20:                #Left
        pygame.draw.circle(screen, clr, [a-b, int((21-pos+1/2) * a)], int(a / 6))

    elif 20 <= pos < 30:                #Up
        pygame.draw.circle(screen, clr, [int((pos%10+3/2) * a), a-b], int(a / 6))

    elif 30 <= pos < 40:                #Right
        pygame.draw.circle(screen, clr, [(12*a)+b, int((pos%10+3/2) * a)], int(a / 6))


def buy(card_nm, i_prc, plr):
    d_plrs["Money"][plr]=d_plrs["Money"][plr]-int(i_prc)
    prt("     Player " + str(plr+1) + " bought " + card_nm + " by investing " + i_prc + "Cr     ", 1025, 750, f_clr=l_clr["white"], bg_clr=l_clr["black"], f_sz=20, alignment=CENTER)
    d_plrs["Cards"][plr].append(card_nm)
    l_bght.append(card_nm)


def UI(plr_num):
    x_origin = (13*a)
    y_origin = 0
    x_sz = int((1366 - x_origin) / 2)
    y_sz=int(768/(tl_plrs/2))
    for i in range(2):
        plr=i*2+1
        for j in range(int(tl_plrs/2)):
            plr=2*(j+1)-(i+1)%2
            pygame.draw.rect(screen, l_clr["white"], pygame.Rect(x_origin+x_sz*i, y_origin+y_sz*j, x_sz, y_sz))
            pygame.draw.rect(screen, l_clr["black"], pygame.Rect(x_origin+x_sz*i, y_origin+y_sz*j, x_sz, y_sz), 1)
            if plr - 1 == plr_num:
                pygame.draw.rect(screen, d_plrs["Clr"][plr-1], pygame.Rect(x_origin + x_sz * i+int(tl_plrs), y_origin + y_sz * j+int(tl_plrs), x_sz-tl_plrs*2, y_sz-tl_plrs*2), 7)

            prt("  Player " + str(plr) + "  ", x_origin + (x_sz / 2) + (i * x_sz), (j * y_sz) + 30, f_sz=30, f_clr=d_plrs["Clr"][plr-1], alignment=CENTER)
            prt("  Money: $" + str(d_plrs["Money"][plr-1]) + "  ", x_origin+(x_sz/2)+(i*x_sz), (j*y_sz) + 60, f_sz=20)
            prt("Properties Owned: ", x_origin+(x_sz/2)+(i*x_sz), (j*y_sz) + 90, f_sz=20)

            for k in range(len(d_plrs["Cards"][plr-1])):
                prt(str(d_plrs["Cards"][plr-1][k]), x_origin+(x_sz/2)+(i*x_sz), (j*y_sz) + 120+(k*20), f_sz=15)


def prt(v_nm, x_var, y_var, tilt=0, f_clr = l_clr["black"], bg_clr = l_clr["white"], f_sz = 10, alignment=CENTER):
    font = pygame.font.Font('freesansbold.ttf', f_sz)
    text = font.render(v_nm, True, f_clr, bg_clr)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    if tilt!=0:
        text = pygame.transform.rotate(text, tilt)
    if alignment==CENTER:
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    screen.blit(text, textRect)


def board():
    for y in range(12):
        for x in range(12):

            if x%11 == 0 and y%11 == 0:      #Corners
                pygame.draw.rect(screen, l_clr["white"], pygame.Rect((x * a), (y * a), 2*a, 2*a))
                pygame.draw.rect(screen, l_clr["black"], pygame.Rect((x * a), (y * a), 2*a, 2*a), 2)

            elif x%11 == 0:                  # |
                pygame.draw.rect(screen, l_clr["white"], pygame.Rect((x * a), (y * a)+a, 2*a, a))
                pygame.draw.rect(screen, l_clr["black"], pygame.Rect((x * a), (y * a)+a, 2*a, a), 2)
                if x==0:                            #Left
                    val=20-y
                    pygame.draw.rect(screen, l_clr[dict["Colour"][val]], pygame.Rect(int((x+3/2)*a), int((y+1) * a), int(a/2), a))
                    pygame.draw.rect(screen, l_clr["black"], pygame.Rect(int((x+3/2)*a), int((y+1) * a), int(a/2), a), 2)
                    prt(dict["Card Name"][val], int((x * a)+a*3/4), int((y * a) + a*5/4), alignment=CENTER)
                    prt(dict["Price"][val], int((x * a) + a*3/4), int((y * a) + a*7/4), alignment=CENTER)
                    if dict["Card Name"][val] in l_bght:
                        owner(dict["Card Name"][val], [((x*a)+22, (y+1)*a+2), ((x*a)+2, ((y+1)*a)+2), ((x*a)+2, ((y+1)*a)+22)])


                elif x==11 and y!=1:                #Right
                    val = 29+y
                    pygame.draw.rect(screen, l_clr[dict["Colour"][val]], pygame.Rect(int(x * a), int(y * a), int(a/2), a))
                    pygame.draw.rect(screen, l_clr["black"], pygame.Rect(int(x * a), int(y * a), int(a/2), a), 2)
                    prt(dict["Card Name"][val], int((x * a)+a*5/4), int((y * a)+a/4), alignment=CENTER)
                    prt(dict["Price"][val], int((x * a)+a*5/4), int((y * a)+(a*3/4)), alignment=CENTER)
                    owner(dict["Card Name"][val], [(((x)*a)+((2*a)-20), ((y)*a)+2), (((x+2)*a)-2, ((y)*a)+2), (((x+2)*a)-2, ((y)*a)+20)])


            elif y%11 == 0:                  # __
                pygame.draw.rect(screen, l_clr["white"], pygame.Rect((x * a)+a, (y * a), a, 2*a))
                pygame.draw.rect(screen, l_clr["black"], pygame.Rect((x * a)+a, (y * a), a, 2*a), 2)

                if y==0:                            #Up
                    val=20+x
                    pygame.draw.rect(screen, l_clr[dict["Colour"][val]], pygame.Rect(int((x+1)*a), int((y+3/2) * a), a, int(int(int(a/2)))))
                    pygame.draw.rect(screen, l_clr["black"], pygame.Rect(int((x+1)*a), int((y+3/2) * a), a, int(a/2)), 2)
                    prt(dict["Card Name"][val], int((x + 5 / 4) * a), int((y + 3 / 4) * a), tilt=90, alignment=CENTER)
                    prt(dict["Price"][val], int((x * a) + a * 5 / 4) +int(a/2), int((y * a) + (a * 3 / 4)), tilt=90, alignment=CENTER)
                    owner(dict["Card Name"][val], [(((x+1)*a)+20, (y*a)+2), (((x+1)*a)+2, (y*a)+2), (((x+1)*a)+2, (y*a)+20)])


                elif y==11 and x!=1:                #Down
                    val = 11-x
                    pygame.draw.rect(screen, l_clr[dict["Colour"][val]], pygame.Rect(int(x * a), int(y * a), a, int(a/2)))
                    pygame.draw.rect(screen, l_clr["black"], pygame.Rect(int(x * a), int(y * a), a, int(a/2)), 2)
                    prt(dict["Card Name"][val], int((x * a) + a * 3 / 4)-int(a/2), int((y * a) + (a * 8 / 7)), tilt=90, alignment=CENTER)
                    prt(dict["Price"][val], int((x * a) + a * 5 / 4)-int(a/2), int((y * a) + (a * 8 / 7)), tilt=90, alignment=CENTER)
                    owner(dict["Card Name"][val], [((x*a)+26, (y*a+2*a)-2), ((x*a)+a-2, (y*a+2*a)-2), ((x*a)+a-2, (y*a)+a+(a-34))])


    prt(dict["Card Name"][20], a, a, alignment=CENTER, f_sz=20)
    prt(dict["Card Name"][30], 12*a, a, alignment=CENTER, f_sz=20)
    prt(dict["Card Name"][10], a, 12*a, alignment=CENTER, f_sz=20)
    prt(dict["Card Name"][0], 12*a, 12*a, alignment=CENTER, f_sz=20)

    b=int(-(tl_plrs/2)/tl_plrs+10)
    for i in range(tl_plrs):
        cokri_pos(i, b)
        b = b + int(-30 / tl_plrs+1/2)

    pygame.draw.rect(screen, l_clr["light green"], pygame.Rect(int(2*a), int(2*a), 9*a, 9*a))
    pygame.draw.rect(screen, l_clr["black"], pygame.Rect(int(2*a), int(2*a), 9*a, 9*a), 2)
    pygame.display.flip()

board()
num=0
plr_num=0
while True:
    UI(plr_num)
    board()
    if d_plrs["Money"][plr_num] != 0:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i_dice = random.choice([2,2,2,2,3,3,4,5,6,6,6,6,7,7,8,8,9,9,9,10,10,10,11,11,12])
                    #pygame.display.flip()

                    d_plrs["Pos"][plr_num] = d_plrs["Pos"][plr_num] + i_dice
                    if d_plrs["Pos"][plr_num]>=40:
                        d_plrs["Pos"][plr_num] = d_plrs["Pos"][plr_num] % 40
                        d_plrs["Money"][plr_num] = d_plrs["Money"][plr_num] + 200


                    if (dict["Type"][d_plrs["Pos"][plr_num]] == "Property" or dict["Type"][d_plrs["Pos"][plr_num]] == "Station"
                        or dict["Type"][d_plrs["Pos"][plr_num]] == "Utilities")\
                        and dict["Card Name"][d_plrs["Pos"][plr_num]] not in l_bght:                #Buying
                        buy(dict["Card Name"][d_plrs["Pos"][plr_num]], dict["Price"][d_plrs["Pos"][plr_num]], plr_num)

                    elif dict["Type"][d_plrs["Pos"][plr_num]] == "Property" and dict["Card Name"][d_plrs["Pos"][plr_num]] in l_bght:
                                                                                                    #Property Rent -
                        d_plrs["Money"][plr_num]=int(d_plrs["Money"][plr_num])-int(dict["Rent"][d_plrs["Pos"][plr_num]])
                        for i in range(tl_plrs):                                                    #Property Rent +
                            if dict["Card Name"][d_plrs["Pos"][plr_num]] in d_plrs["Cards"][i]:
                                d_plrs["Money"][i] = int(d_plrs["Money"][i]) + int(dict["Rent"][d_plrs["Pos"][plr_num]])

                    elif dict["Type"][d_plrs["Pos"][plr_num]] == "Station" and dict["Card Name"][d_plrs["Pos"][plr_num]] in l_bght:
                        d_plrs["Money"][plr_num] = int(d_plrs["Money"][plr_num]) - int(dict["1 House"][d_plrs["Pos"][plr_num]])
                        for i in range(tl_plrs):                                                    #Station Rent +
                            if dict["Card Name"][d_plrs["Pos"][plr_num]] in d_plrs["Cards"][i]:
                                d_plrs["Money"][i] = int(d_plrs["Money"][i]) + int(dict["1 House"][d_plrs["Pos"][plr_num]])
                                break


                    elif dict["Card Name"][d_plrs["Pos"][plr_num]] == "Go to Jail":                 #Go to Jail
                        d_plrs["Pos"][plr_num] = 10
                        prt("     Player "+str(plr_num+1)+" went to Jail     ", 1025, 600, f_sz=20, f_clr=l_clr["white"], bg_clr=l_clr["black"])

                    elif dict["Card Name"][d_plrs["Pos"][plr_num]] == "Go" and num > 4:             #GO
                        d_plrs["Pos"][plr_num] = 0
                        prt(str(plr_num) + " Go", 1025, 700, f_sz=20, f_clr=l_clr["white"], bg_clr=l_clr["black"])

                    elif dict["Type"][d_plrs["Pos"][plr_num]] == "Tax":                             #Tax
                        d_plrs["Money"][plr_num]=d_plrs["Money"][plr_num]-int(dict["Price"][d_plrs["Pos"][plr_num]])


                    if d_plrs["Money"][plr_num]<=0:
                        d_plrs["Money"][plr_num] = 0
                        d_plrs["Pos"][plr_num] = 0
                        out.append(plr_num)
                        print(str(plr_num + 1) + " is BANKCURRUPT")

                    if len(out)==tl_plrs-1:
                        for i in range(tl_plrs):
                            if i not in out:
                                print("PLAYER " + str(i+1) + " WONNN!!! :) :)")
                                exit()

                    if plr_num == tl_plrs - 1:
                        plr_num = plr_num%(tl_plrs-1)
                    else:
                        plr_num=plr_num+1
                    num=num+1


                if event.key == pygame.K_ESCAPE:
                    exit()

    else:
        if plr_num == tl_plrs - 1:
            plr_num = 0

        else:
            plr_num = plr_num + 1
        num = num + 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if event.key == pygame.K_ESCAPE:
                    exit()
