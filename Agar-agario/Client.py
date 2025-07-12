import socket, pygame
from Enter import Window

login = Window()
print(login.color, login.name)
master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
master.connect(("localhost", 10524))
master.send(f"<{login.name},{login.color}>".encode())


WIDTH = 500
HEIGHT = 500
WWIDTH = 8000
WHEIGHT = 8000

pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Agar-agario')
radplay = 30
oldvect = (0, 0)
scale = 1
bufer = 1024
xx = 0
yy = 0

class Grid:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cell = 100

    def celldraw(self, x, y, scale):
        lines = int(WIDTH // self.cell + 2)
        hlines = int(HEIGHT // self.cell + 2)

        left = int((0 + x) / scale)
        right = int((WWIDTH - x) / scale)
        up = int((0 + y) / scale)
        down = int((WHEIGHT - y) / scale)
        top = max(0, HEIGHT // 2 - up)
        bottom = min(HEIGHT, HEIGHT // 2 + down)
        left = max(0, WIDTH // 2 - left)
        right = min(WIDTH, WIDTH // 2 + right)
        for i in range(lines):
            if left < (self.cell * i + self.x) < right:
                pygame.draw.line(window, color="grey60", width=2, start_pos=(self.cell * i + self.x ,top), end_pos=(self.cell * i + self.x, bottom))
        for i in range(hlines):
            if top < (self.cell * i + self.y) < bottom:
                pygame.draw.line(window, color="grey60", width=2, start_pos=(left, self.cell * i + self.y),
                             end_pos=(right, self.cell * i + self.y))

    def gridmove(self, x, y, scale):
        self.x = -self.cell - x // scale % self.cell
        self.y = -self.cell - y // scale % self.cell
        #print(self.x, self.y)

    def gridscale(self, scale):
        self.cell = 100 // scale

def checkvect(mess):
    first = None
    for ind, lett in enumerate(mess):
        if lett == "<":
            first = ind
        if lett == ">" and first is not None:
            second = ind
            result = mess[first + 1: second].split(",")
            return result
    global bufer
    bufer = min(bufer*2, 70000)
    print(bufer)

def draw(data):
    x, y, size, color = data.split()
    x = WIDTH // 2 + int(x) // scale
    y = HEIGHT // 2 + int(y) // scale
    size = int(size) // scale
    pygame.draw.circle(surface=window, color=color, center=(x, y), radius=size)

grid = Grid()

run = True
while run:
    try:
        mess = master.recv(bufer).decode()
        #print(mess)
        victims = checkvect(mess)
        if victims:
            radplay = int(victims[0])
            if float(victims[1]) != scale:
                grid.gridscale(float(victims[1]))
            scale = float(victims[1])
            xx = int(victims[2])
            yy = int(victims[3])
            grid.gridmove(xx, yy, scale)
    except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
        #print("800fps")
        pass

    if pygame.mouse.get_focused():
        mx, my = pygame.mouse.get_pos()
        vx, vy = mx - WIDTH // 2, my - HEIGHT // 2
        vecd = (vx**2 + vy**2)**0.5
        #print(vx, vy)
        if vecd < radplay // scale:
            vx, vy = 0, 0
        else:
            vx /= vecd
            vy /= vecd
        if (vx, vy) != oldvect:
            oldvect = (vx, vy)
            try:
                master.send(f"<{vx},{vy}>".encode())
            except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
                pass

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    window.fill("grey")

    grid.celldraw(xx, yy, scale)

    if victims:
        #print(victims[:4])
        for i in victims[4:]:
            if i:
                draw(i)

    pygame.draw.circle(surface=window, color=login.color, center=(WIDTH // 2, HEIGHT // 2), radius=radplay // scale)
    pygame.display.flip()
pygame.quit()