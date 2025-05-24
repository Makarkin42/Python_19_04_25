import socket
import time, random
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
    def __init__(self, name, sk, adress, id):
        self.id = id
        self.name = "wizarD"
        self.sk = sk
        self.adress = adress
        self.x = 2500
        self.y = 2500
        self.xspeed = 1
        self.yspeed = 1
        self.abspeed = 5
        self.color = "black"
        self.size = 100
        self.db = session.get(Stats, self.id)
        self.xvid = 500
        self.yvid = 500
    def move(self):
        x = self.x + self.xspeed * self.abspeed
        y = self.y + self.yspeed * self.abspeed
        if x <= 0 or x >= WWIDTH:
            self.xspeed = 0
        if y <= 0 or y >= WHEIGHT:
            self.yspeed = 0
        #if self.adress:
            #print(self.x, self.y, self.xspeed, self.yspeed)
        self.x += self.xspeed * self.abspeed
        self.y += self.yspeed * self.abspeed

    def changesp(self, vx, vy):
        self.xspeed = float(vx)
        self.yspeed = float(vy)


class Food:
    def __init__(self):
        self.x = random.randint(0, WWIDTH)
        self.y = random.randint(0, WHEIGHT)
        self.size = 18
        self.color = random.choice(colors)


WIDTH = 500
HEIGHT = 500
FPS = 30
WWIDTH = 5000
WHEIGHT = 5000

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
    distx = p2.x - p1.x
    disty = p2.y - p1.y
    if abs(distx) <= p1.xvid / 2 + p2.size and abs(disty) <= p1.yvid / 2 + p2.size:
        x = int(distx)
        y = int(disty)
        size = int(p2.size)
        color = p2.color
        data = f"{x} {y} {size} {color}"
        usvid[p1.id].append(data)


for i in range(50):
    bot = Gamer(name="boba", adress=None, sk=None, id=i)
    bot.x = random.randint(0, WHEIGHT)
    bot.y = random.randint(0, WWIDTH)
    bot.size = random.randint(20, 150)
    bot.color = random.choice(["white", "green", "yellow", "blue", "red", "purple", "orange"])
    bot.xspeed = random.random() * 2 - 1
    bot.yspeed = random.random() * 2 - 1
    users[i] = bot

for i in range(300):
    eda = Food()
    foods.append(eda)

tick = 0
run = True
while run:
    clock.tick(FPS)
    tick += 1
    if tick % FPS * 5 == 0:
        try:
            clients, adres = master.accept()
            clients.setblocking(False)
            print(adres, "Подключился")
            player = Stats(adress=adres)
            session.merge(player)
            session.commit()

            host = f"({adres[0]},{adres[1]})"
            data = session.query(Stats).filter(host==Stats.adress).all()[0]
            user = Gamer(name="John",sk=clients,adress=host,id=data.id)
            user.abspeed = 15
            users[user.id] = user
        except BlockingIOError:
            pass

    for i in users:
        try:
            if users[i].sk:
                mess = users[i].sk.recv(1024).decode()
                print(mess)
                vector = checkvect(mess)
                print(vector)
                users[i].changesp(vx = vector[0], vy = vector[1])
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
                vision(i, p1)

    for i in users:
        usvid[i] = ",".join(usvid[i])
        usvid[i] = f"<{usvid[i]}>"

    for id in users:
        try:
            if users[id].sk is not None:
                mss = usvid[id]
                users[id].sk.send(mss.encode())
        except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
            pass

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
        pygame.draw.circle(surface=window ,color=user.color, center=(x, y), radius=s)

    pygame.display.flip()
pygame.quit()