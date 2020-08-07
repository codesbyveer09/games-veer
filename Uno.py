import pygame, random, sys, string, time

tl_plrs=4
LEFT = 0
RIGHT = 1
CENTER = 2
INL_CRDS = 7
usd_crd=[]
cards=[] # owned by a player
PLS2="+2"
REV="Rev"
SKP="Skip"
WLD="Wild"
PLS4="+4"


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
white = (255,255,255)
black = (0,0,0)
blue = (0,139,139)
red = (250,0,0)
green = (0,250,0)
yellow = (250,250,0)
gold = (255,215,0)
bg_clr = (146,197,200)

l_clr=[blue, red, green, yellow]

pygame.draw.rect(screen, bg_clr, pygame.Rect(0, 0, 2366, 768))

def UI(plr=100):
    #Three CPUs
    j=1

    for i in range(0, tl_plrs+1, 2):
        x=int((i+1)*(1366/(tl_plrs-1))/2)-80
        pygame.draw.rect(screen, white, pygame.Rect(x, 30, 150, 180))
        if plr == j:
            clr=gold
        else:
            clr=black
        pygame.draw.rect(screen, clr, pygame.Rect(x, 30, 150, 180), 2)
        pygame.draw.rect(screen, blue, pygame.Rect(x+130, 185, 20, 25), 3)
        prt("CPU " + str(j), x+75, 30+90, f_sz=30, f_clr=l_clr[j])
        prt(str(len(cards[j])), x+140, 200, f_sz=15, f_clr=blue)
        j+=1

    # Player Cards
    var=-(len(cards[0])/2)*70-(230/5)
    pygame.draw.rect(screen, bg_clr, pygame.Rect(0, 570, 1366, 240))
    for i in range(len(cards[0])):
        pygame.draw.rect(screen, cards[0][i][1], pygame.Rect(int(1366/2+var), 570, 163, 240))
                                        # cards[0][i][1] is the colour of the card
        pygame.draw.rect(screen, white, pygame.Rect(int(1366/2+var), 570, 163, 240), 2)
        prt(cards[0][i][0], 1366/2+var+2, 570+2, alignment=LEFT, f_clr=white, f_sz=16, bg_clr=cards[0][i][1], tilt=25)
        prt(cards[0][i][0], 1366/2+var+2+int(163/2), 570+2+int(240/2), alignment=CENTER, f_clr=white, bg_clr=cards[0][i][1], f_sz=50)
                                        # cards[0][i][0] is the name of the card
        var+=70

    # Deck
    pygame.draw.rect(screen, black, pygame.Rect(0, int(768/2), 225, 163))
    pygame.draw.ellipse(screen, red, (0, int(768/2), 225,163))
    prt("UNO", 225/2, 768/2+163/2, alignment=CENTER, f_clr=gold, bg_clr=red, f_sz=60, tilt=25)
    pygame.draw.rect(screen, white, pygame.Rect(0, int(768/2), 225, 163), 3)

    # Played Cards in center
    prt("     ", 1355/2, 768/2, alignment=CENTER, bg_clr=pl_crd[1], tilt=90, f_sz=160)
    prt(pl_crd[0], int(1366/2)-(161/2)+15, 768/2-(240/2)+2+(3*16)/2, alignment=CENTER, f_clr=white, bg_clr=pl_crd[1], tilt=25, f_sz=16)
    prt(pl_crd[0], int(1366/2), 768/2, alignment=CENTER, f_clr=white, bg_clr=pl_crd[1], f_sz=50)
    prt(pl_crd[0], 1366/2+int(223/2)-60, (768/2)+(240/2)-25, alignment=CENTER, f_clr=white, bg_clr=pl_crd[1], tilt=205, f_sz=16)
    pygame.draw.rect(screen, white, pygame.Rect(int(1366/2)-int(170/2)-2, int(768/2)-int(225/2), 163, 223), 2)

    pygame.display.flip()

def enter_card(p1cards):
    apnd=0
    num=""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit(1)
                if event.key == pygame.K_c:
                    if apnd==1:
                        return pl_crd, None
                    a=get_card()
                    cards[0].append(a)
                    UI()

                    apnd += 1
                if event.key == pygame.K_1:
                    num+="1"
                if event.key == pygame.K_2:
                    num+="2"
                if event.key == pygame.K_3:
                    num+="3"
                if event.key == pygame.K_4:
                    num+="4"
                if event.key == pygame.K_5:
                    num+="5"
                if event.key == pygame.K_6:
                    num+="6"
                if event.key == pygame.K_7:
                    num+="7"
                if event.key == pygame.K_8:
                    num+="8"
                if event.key == pygame.K_9:
                    num+="9"
                if event.key == pygame.K_0:
                    num+="0"
                prt(num, 0, 0, alignment=LEFT, f_sz=20)
                pygame.display.flip()

                if event.key == pygame.K_RETURN:
                    if num!="":
                        if int(num)!=0 and int(num)<=len(p1cards):
                            if pl_crd[0] == p1cards[int(num)-1][0] or pl_crd[1] == p1cards[int(num)-1][1] or p1cards[int(num)-1][1] == black:
                                return p1cards[int(num)-1], num
                            else:
                                prt("This card doesn't match the played card", 2, 750, f_clr=red, bg_clr=bg_clr, alignment=LEFT, f_sz=20)
                                num = ""
                                pygame.display.flip()
                        else:
                            prt("Input the number on which your card is", 2, 750, f_clr=red, bg_clr=bg_clr, alignment=LEFT, f_sz=20)
                            num=""
                            pygame.display.flip()
                    else:
                        prt("Input a number then press Enter key", 2, 750, f_clr=red, bg_clr=bg_clr, alignment=LEFT, f_sz=20)
                        num=""
                        pygame.display.flip()



def get_card():
    if len(usd_crd)==108:
        exit("0 CARDS LEFT ERROR")
    while True:
        num=random.randrange(0, 10)
        val=random.choice([str(num), str(num), str(num), str(num), str(num), str(num), str(num), str(num), PLS2, PLS2, REV, REV, SKP, SKP, WLD, PLS4])
        clr = random.choice([blue, green, red, yellow])
        if val == PLS4 or val == WLD:
            clr = black
        crd = (val, clr)

        if val == PLS4 or val == WLD:
            j = 0
            for i in usd_crd:
                if crd==i:
                    j+=1
            if j < 4:
                break

        elif val==PLS2 or val==REV or val==SKP or 0 < int(val) < 10:
            j=0
            for i in usd_crd:
                if crd==i:
                    j+=1
            if j < 2:
              break

        elif val == "0":
            if crd not in usd_crd:
                break

    usd_crd.append(crd)
    return crd


def prt(v_nm, x_var, y_var, tilt=0, f_clr = black, bg_clr = white, f_sz = 10, alignment=CENTER):
    font = pygame.font.Font('freesansbold.ttf', f_sz)
    text = font.render(v_nm, True, f_clr, bg_clr)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    if tilt!=0:
        text = pygame.transform.rotate(text, tilt)
    if alignment==CENTER:
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    elif alignment==RIGHT:
        text = font.render(v_nm, True, white)
        text_rect = text.get_rect()
        text_rect.right = 150  # align to right to 150px
    screen.blit(text, textRect)


for i in range(tl_plrs):
    lst=[]
    for i in range(INL_CRDS):
        lst.append(get_card())
    lst.append(("+4", black))
    cards.append(lst)

print(cards)


pl_crd=get_card()
UI()
plr_no=0
while True:
    UI()
    # PLAYER Turn
    lst=enter_card(cards[0])
    if len(cards[0])==1:
        prt("Type UNO else you will be given a penalty")
        if event.key == pygame.K_u:
            if event.key == pygame.K_n:
                if event.key == pygame.K_o:
                    prt("UNO", )

    pl_crd=lst[0]
    if lst[1] != None:
        cards[0].pop(int(lst[1])-1)
    print(len(cards[0]))
    if len(cards[0])==0:
        exit("Player 1 WOOONNN!!!")

    # Card Type
    if pl_crd[0]=="Skip":
        skpd=True
    else:
        skpd=False
    if pl_crd[0]=="+2":
        cards[1].append(get_card())
        cards[1].append(get_card())
    if pl_crd[0]=="+4":
        for i in range(4):
            cards[1].append(get_card())


    #CPU's Turn
    for i in range(1, tl_plrs):
        if skpd==False:
            UI(plr=i)
            time.sleep(2)
            bool1 = 0
            plr_crds=cards[i]
            while True:
                for card_no in range(len(plr_crds)):
                    if plr_crds[card_no][1]==pl_crd[1] or plr_crds[card_no][0]==pl_crd[0] or pl_crd[1]==black:
                        pl_crd=plr_crds[card_no]
                        cards[i].pop(card_no)
                        bool1+=1
                        break
                if bool1 == 0:
                    cards[i].append(get_card())
                else:
                    break
            if i-1==tl_plrs:
                num=i%3
            else:
                num=i
            if pl_crd[0] == "Skip":
                skpd = True
            else:
                skpd = False
            if pl_crd[0] == "+2":
                cards[i].append(get_card())
                cards[i].append(get_card())
            if pl_crd[0] == "+4":
                for j in range(4):
                    cards[i].append(get_card())
            print(cards)


    plr_no=plr_no%(tl_plrs-1)
    plr_no=plr_no+1