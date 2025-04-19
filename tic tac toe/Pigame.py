import pygame
import random
import Menu

VIDTH = 900
HEIGHT = 600
FPS = 60
CELL = 180
SPACEX = (VIDTH - CELL * 3)//2
SPACEY = (HEIGHT - CELL * 3)//2
CO = 10

pygame.init()

window = pygame.display.set_mode((VIDTH,HEIGHT))
pygame.display.set_caption('Крестики-нолики')
clock = pygame.time.Clock()

def change(t,znak):
    ex.krest = znak
    if znak == "x":
        bot.circle = 'o'
    else:
        bot.circle = 'x'

def restart():
    global pole, win, tick
    win = None
    pole = [
        ["", "", "", ],
        ["", "", "", ],
        ["", "", "", ]]
    menu.disable()
    tick = 0

def select(_,diff):
    bot.diff = diff

menu = Menu.Meny(window)
menu.add.button("ИГРАТЬ",restart)
menu.add.selector("ИГРАТЬ ЗА:",[('КРЕСТИК','x'),("НОЛИК",'o')],onchange=change)
menu.add.selector("СЛОЖНОСТЬ",[("ЛЕГКО",'easy'),("СРЕДНЯЯ",'medium'),("СЛОЖНАЯ",'hard')],onchange=select)
menu.add.button("ВЫХОД",quit)

pole = [
    ["","","",],
    ["","","",],
    ["","","",]]
def grid():
    for i in range(1,3):
        pygame.draw.line(window,"black",start_pos=(SPACEX + i * CELL,
                                                   SPACEY),end_pos=(SPACEX + i * CELL,
                                                                    HEIGHT - SPACEY))
        pygame.draw.line(window,"black",start_pos=(SPACEX,
                                                   SPACEY + i * CELL),end_pos=(VIDTH - SPACEX
                                                                            ,SPACEY + i * CELL))

def draw():
    for i in range(3):
        for a in range(3):
            if pole[i][a] == "x":
                pygame.draw.line(window, "red",width=3, start_pos=(SPACEX + a * CELL + CO, SPACEY + i * CELL + CO),
                                 end_pos=(SPACEX + a * CELL + CELL - CO , SPACEY + i * CELL + CELL - CO))
                pygame.draw.line(window, "red", width=3, start_pos=(SPACEX + a * CELL + CELL - CO, SPACEY + i * CELL + CO),
                                 end_pos=(SPACEX + a * CELL + CO, SPACEY + i * CELL + CELL - CO))
            elif pole[i][a] == "o":
                pygame.draw.circle(window,"blue",width=3,center=(SPACEX + a * CELL + CELL//2, SPACEY + i * CELL + CELL//2),
                                   radius=CELL//2*0.95)

def check():
    for i in range(3):
        for a in range(3):
            if pole[i][a] == "":
                return True

def check_win(znak):
    for i in range(3):
        kol = [k[i] for k in pole]
        if kol.count(znak) == 3:
            return (i,0),(i,1),(i,2)
    for i in range(3):
        if pole[i].count(znak) == 3:
            return (0,i),(1,i),(2,i)
    if pole[0][0] == pole[1][1] == pole[2][2] == znak:
        return (0,0),(1,1),(2,2)
    if pole[0][2] == pole[1][1] == pole[2][0] == znak:
        return (0,2),(1,1),(2,0)

def bot_win(znak):
    for i in range(3):
        if pole[i].count(znak) == 2 and ""in pole[i]:
            return (i,pole[i].index(""))
    for i in range(3):
        kol = [k[i]for k in pole]
        if kol.count(znak) == 2 and "" in kol:
            return (kol.index(""),i)
    diag1 = pole[0][0], pole[1][1], pole[2][2]
    diag2 = pole[0][2], pole[1][1], pole[2][0]
    if diag1.count(znak) == 2 and "" in diag1:
        return (diag1.index(""),diag1.index(""))
    if diag2.count(znak) == 2 and "" in diag2:
        return (diag2.index(""),2 - diag2.index(""))

def draw_win():
    a,i = win[0]
    b,c = win[2]
    pygame.draw.line(window,'black',width=6,start_pos=(SPACEX + a * CELL + CELL//2, SPACEY + i * CELL + CELL//2),
                     end_pos=((SPACEX + b * CELL + CELL//2, SPACEY + c * CELL + CELL//2)))


win = None
class Human:
    def __init__(self):
        self.krest = "x"
    def hod(self):
        x,y = pygame.mouse.get_pos()
        row = (y-SPACEY)/CELL
        col = (x-SPACEX)/CELL
        if row>=0 and row<3 and col>=0 and col<3 and pole[int(row)][int(col)] == "":
            pole[int(row)][int(col)] = self.krest
            return True

class Bot:
    def __init__(self):
        self.circle = "o"
        self.diff = "hard"
    def bot_hod(self):
        hod = bot_win(znak=self.circle)
        hod2 = bot_win(znak=ex.krest)
        print(hod,hod2)
        if self.diff in ("medium","hard") and hod:
            pole[hod[0]][hod[1]] = self.circle
        elif self.diff == "hard" and hod2:
            pole[hod2[0]][hod2[1]] = self.circle
        else:
            while check():
                row = random.randint(0,2)
                col = random.randint(0,2)
                if pole[row][col] == "":
                    pole[row][col] = self.circle
                    break

ex = Human()
bot = Bot()
tick = 0
run = True
while run:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not menu.is_enabled() and not win:
            hod_res = ex.hod()
            if hod_res:
                win = check_win(znak=ex.krest)
                if not win:
                    bot.bot_hod()
                    win = check_win(znak=bot.circle)
        if event.type == pygame.KEYDOWN and not menu.is_enabled():
            #print(event)
            if event.key == pygame.K_ESCAPE:
                menu.enable()
    window.fill("grey")
    draw()
    grid()
    if win:
        draw_win()
        tick += 1
        if tick == 5 * FPS:
            menu.enable()
    elif not check():
        tick += 1
        if tick == 5 * FPS:
            menu.enable()
    menu.flip(events)
    pygame.display.flip()
pygame.quit()