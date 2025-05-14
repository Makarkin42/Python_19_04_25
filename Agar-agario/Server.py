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
class Gamer():
    def __init__(self, name, sk, adress, id):
        self.id = id
        self.name = "wizarD"
        self.sk = sk
        self.adress = adress
        self.x = 250
        self.y = 250
        self.xspeed = 2
        self.yspeed = 2
        self.abspeed = 3
        self.color = "black"
        self.size = 100
        self.db = session.get(Stats, self.id)
        self.xvid = 500
        self.yvid = 500
    def move(self):
        self.x += self.xspeed * self.abspeed
        self.y += self.yspeed * self.abspeed
    def changesp(self, vx, vy):
        self.xspeed = float(vx)
        self.yspeed = float(vy)


WIDTH = 500
HEIGHT = 500
FPS = 20
WWIDTH = 5000
WHEIGHT = 5000

pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Server')
clock = pygame.time.Clock()

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

for i in range(50):
    bot = Gamer(name="boba", adress=None, sk=None, id=i)
    bot.x = random.randint(0, WHEIGHT)
    bot.y = random.randint(0, WWIDTH)
    bot.size = random.randint(20, 150)
    bot.color = random.choice(["white", "green", "yellow", "blue", "red", "purple", "orange"])
    bot.xspeed = random.random() * 2 - 1
    bot.yspeed = random.random() * 2 - 1
    users[i] = bot

run = True
while run:
    clock.tick(FPS)
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
        users[user.id] = user
    except BlockingIOError:
        pass


    for i in users:
        try:
            if users[i].sk is not None:
                users[i].sk.send("Я тут".encode())
        except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
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
            p2 = prs[a]

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