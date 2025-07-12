import socket
import random
import pygame
from Schema import Stats, session

master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
master.bind(("localhost", 10524))
master.setblocking(False)
master.listen(5)
print("Сокет создан!")
users = {}
colors = ["white", "purple", "black", "green", "red", "blue", "yellow", "orange"]
class Gamer:
    def __init__(self, name, sk, adress, id, color):
        self.id = id
        self.name = name
        self.sk = sk
        self.adress = adress
        self.x = 2500
        self.y = 2500
        self.xspeed = 0
        self.yspeed = 0
        self.abspeed = 8
        self.color = color
        self.size = 30
        self.db = session.get(Stats, self.id)
        self.xvid = 500
        self.yvid = 500
        self.scale = 1
    def move(self):
        x = self.x + self.xspeed * self.abspeed
        y = self.y + self.yspeed * self.abspeed
        if x <= 0 or  x >= WWIDTH:
            self.xspeed = 0 if self.sk else -self.xspeed
        if y <= 0 or  y >= WHEIGHT:
            self.yspeed = 0 if self.sk else -self.yspeed
            #Тернарный оператор^^^
        #if self.adress:
            #print(self.x, self.y, self.xspeed, self.yspeed)
        self.x += self.xspeed * self.abspeed
        self.y += self.yspeed * self.abspeed

    def changesp(self, vx, vy):
        self.xspeed = float(vx)
        self.yspeed = float(vy)

    def scchange(self):
        if self.size >= self.xvid // 6:
            self.scale += 0.5
            self.xvid = 500 * self.scale
            self.yvid = 500 * self.scale


class Food:
    def __init__(self):
        self.x = random.randint(0, WWIDTH)
        self.y = random.randint(0, WHEIGHT)
        self.size = 18
        self.color = random.choice(colors)


WIDTH = 500
HEIGHT = 500
FPS = 30
WWIDTH = 8000
WHEIGHT = 8000

pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Server')
clock = pygame.time.Clock()
foods = []

def checkvect(mess):
    first = None
    for ind, lett in enumerate(mess):
        if lett == "<":
            first = ind
        if lett == ">" and first is not None:
            second = ind
            result = mess[first + 1: second].split(",")
            return result

def vision(p1: Gamer, p2: Gamer):
    #print(usvid)
    #print(users)
    distx = p2.x - p1.x
    disty = p2.y - p1.y
    #Проверка видимости противника
    if abs(distx) <= p1.xvid / 2 + p2.size and abs(disty) <= p1.yvid / 2 + p2.size:
        dist = (distx ** 2 + disty ** 2) ** 0.5
        #Проверка поедания противника
        if dist < p1.size:
           p1.size = (p1.size**2 + p2.size**1.5)**0.5
           p2.size = 0
           p1.scchange()
        else:
            x = int(distx)
            y = int(disty)
            size = int(p2.size)
            color = p2.color
            data = f"{x} {y} {size} {color}"
            usvid[p1.id].append(data)


tick = 0
run = True
while run:
    clock.tick(FPS)
    tick += 1
    if tick % (FPS * 5) == 0:
        try:
            clients, adres = master.accept()
            clients.setblocking(False)
            print(adres, "Подключился")
            login = clients.recv(1024).decode()
            nickname, col = checkvect(login)
            player = Stats(adress=adres)
            session.merge(player)
            session.commit()

            host = f"({adres[0]},{adres[1]})"
            data = session.query(Stats).filter(host==Stats.adress).all()[0]
            user = Gamer(name=nickname,sk=clients,adress=host,id=data.id, color=col)
            users[user.id] = user
        except BlockingIOError:
            pass

    if tick % (FPS * 5) == 0:
        us = 75 - len(users)
        for i in range(us):
            bot = Gamer(name="boba", adress=None, sk=None, id=tick + i, color="")
            bot.x = random.randint(0, WHEIGHT)
            bot.y = random.randint(0, WWIDTH)
            bot.size = random.randint(15, 40)
            bot.color = random.choice(["white", "green", "yellow", "blue", "red", "purple", "orange"])
            bot.xspeed = random.random() * 2 - 1
            bot.yspeed = random.random() * 2 - 1
            users[bot.id] = bot
        fus = 150 - len(foods)
        for i in range(fus):
            eda = Food()
            foods.append(eda)

    for i in users:
        try:
            if users[i].sk:
                mess = users[i].sk.recv(1024).decode()
                #print(mess)
                vector = checkvect(mess)
                users[i].changesp(vx = vector[0], vy = vector[1])
            elif tick % (FPS * 5) == 0:
                users[i].xspeed = random.random() * 2 - 1
                users[i].yspeed = random.random() * 2 - 1
        except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
            pass
    for i in users:
        users[i].move()

    usvid = {}
    for i in users:
        usvid[i] = []
    prs = tuple(users.items())
    for i in range(len(prs)):
        p1 = prs[i][1]
        for a in range(i+1, len(prs)):
            p2 = prs[a][1]
            vision(p1, p2)
            vision(p2, p1)
        for i in foods:
            vision(p1, i)

    for i in users:
        #Формируем сообщение КЛИЕНТА
        size = int(users[i].size)
        scale = users[i].scale
        xx = int(users[i].x)
        yy = int(users[i].y)
        usvid[i] = ",".join(usvid[i])
        usvid[i] = f"<{size},{scale},{xx},{yy},{usvid[i]}>"

    for id in users:
        try:
            if users[id].sk is not None:
                mss = usvid[id]
                users[id].sk.send(mss.encode())
        except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
            pass

    for i in tuple(users):
        if users[i].size == 0:
            del users[i]

    for i in foods:
        if i.size == 0:
            foods.remove(i)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    window.fill("grey")


    for i in users:
        user = users[i]
        x = user.x * WIDTH // WWIDTH
        y = user.y * HEIGHT // WHEIGHT
        s = user.size * HEIGHT // WHEIGHT
        pygame.draw.circle(surface=window, color=user.color, center=(x, y), radius=s)

    '''for user in foods:
        x = user.x * WIDTH // WWIDTH
        y = user.y * HEIGHT // WHEIGHT
        s = user.size * HEIGHT // WHEIGHT
        pygame.draw.circle(surface=window, color="black", center=(x, y), radius=s)'''

    pygame.display.flip()
pygame.quit()