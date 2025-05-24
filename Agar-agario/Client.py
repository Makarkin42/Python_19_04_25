import socket, pygame

master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
master.connect(("localhost", 10524))


WIDTH = 500
HEIGHT = 500
WWIDTH = 5000
WHEIGHT = 5000

pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Agar-agario')
radplay = 30
oldvect = (0, 0)

def checkvect(mess):
    first = None
    for ind, lett in enumerate(mess):
        if lett == "<":
            first = ind
        if lett == ">" and first is not None:
            second = ind
            result = mess[first + 1: second].split(",")
            return result

def draw(data):
    x, y, size, color = data.split()
    x = WIDTH // 2 + int(x)
    y = HEIGHT // 2 + int(y)
    size = int(size)
    pygame.draw.circle(surface=window, color=color, center=(x, y), radius=size)


run = True
while run:
    try:
        mess = master.recv(1024).decode()
        print(mess)
        victims = checkvect(mess)
    except(BlockingIOError, ConnectionResetError, ConnectionAbortedError):
        #print("800fps")
        pass

    if pygame.mouse.get_focused():
        mx, my = pygame.mouse.get_pos()
        vx, vy = mx - WIDTH // 2, my - HEIGHT // 2
        vecd = (vx**2 + vy**2)**0.5
        #print(vx, vy)
        if vecd < radplay:
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

    print(victims)
    for i in victims:
        if i:
            draw(i)

    pygame.draw.circle(surface=window, color="yellow", center=(WIDTH // 2, HEIGHT // 2), radius=radplay)
    pygame.display.flip()
pygame.quit()