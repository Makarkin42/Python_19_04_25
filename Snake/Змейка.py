import pygame
import random
import os
import Menu
#//30*30

VIDTH = 900
HEIGHT = 600
FPS = 5

pygame.init()

window = pygame.display.set_mode((VIDTH,HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()


class Snake:
    size = 49
    def __init__(self):
        self.x = 450
        self.y = 300
        self.step = 50
        self.xspeed = 0
        self.yspeed = 0
        self.long = 3
        self.coords = []
        self.headnap = 0
        self.tailnap = []
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.coords.append((self.x, self.y))
        self.tailnap.append(self.headnap)
        if self.long < len(self.coords):
            del self.coords[0]
            del self.tailnap[0]

        img = pics_snake ["head"][self.headnap]
        rect = img.get_rect(x=self.x,y=self.y)
        window.blit(img,rect)

        if self.xspeed or self.yspeed:
            img = pics_snake["tail"][self.tailnap[1]]
            x,y = self.coords[0]
            rect = img.get_rect(x=x, y=y)
            window.blit(img, rect)

            for x,y in self.coords[1:-1]:
                img = pics_snake["body"][0]
                rect = img.get_rect(x=x,y=y)
                window.blit(img,rect)

    def control(self,event):
        if event.key == pygame.K_w and not self.yspeed:
            self.xspeed = 0
            self.yspeed = -self.step
            self.headnap = 3
        if event.key == pygame.K_a and not self.xspeed:
            self.yspeed = 0
            self.xspeed = -self.step
            self.headnap = 1
        if event.key == pygame.K_s and not self.yspeed:
            self.xspeed = 0
            self.yspeed = self.step
            self.headnap = 0
        if event.key == pygame.K_d and not self.xspeed:
            self.yspeed = 0
            self.xspeed = self.step
            self.headnap = 2
    def defeat(self):
        if self.x >= VIDTH or self.x < 0 or self.y >= HEIGHT or self.y < 0:
            go_m.play()
            self.__init__()
            menu.enable()
        for x,y in self.coords[0:-1]:
            if self.x == x and self.y == y and self.xspeed != self.yspeed:
                go_m.play()
                self.__init__()
                menu.enable()

class Food:
    size = 50
    def __init__(self):
        self.x = random.randint(0,900)//50*50
        self.y = random.randint(0,600)//50*50
        if (self.x, self.y) in snake.coords:
            self.__init__()
        self.pic = random.choice(pics_food)
        self.rect = self.pic.get_rect(x = self.x,y = self.y)
    def rendering(self):
        window.blit(self.pic, self.rect)
    def check(self):
        if snake.x == self.x and snake.y == self.y:
            snake.long += 1
            eat_m.play()
            self.__init__()

put = "./img/snake/"
pics_snake = {
    "head":[pygame.image.load(put+"HeadB.png"),
            pygame.image.load(put+"HeadL.png"),
            pygame.image.load(put+"HeadR.png"),
            pygame.image.load(put+"HeadT.png")],
    "body":[pygame.image.load(put+"body.png")],
    "tail":[pygame.image.load(put+"TailB.png"),
            pygame.image.load(put+"TailL.png"),
            pygame.image.load(put+"TailR.png"),
            pygame.image.load(put+"TailT.png")]}
for key in pics_snake:
    pics_snake [key] = [pygame.transform.scale(img,(Snake.size,Snake.size))
                      for img in pics_snake [key]]
pics_food = [pygame.image.load(f"./img/food/{name}")
             for name in os.listdir("./img/food")]
pics_food = [pygame.transform.scale(img,(Food.size,Food.size))
                       for img in pics_food]
bg = {"bkg":[pygame.image.load("./img/grass_01.png"),
      pygame.image.load("./img/plodovye-derevia-2.jpg")]}
for key in bg:
    bg [key] = [pygame.transform.scale(img,(VIDTH,HEIGHT))
                for img in bg [key]]

snake = Snake()
apple = Food()
rect = bg["bkg"][0].get_rect(x=0,y=0)
hard_bg = 0

def diff(_,fps):
    global FPS, hard_bg
    FPS = fps
    if fps == 6:
        hard_bg = 1
    else:
        hard_bg = 0

def volume(ans):
    bg_m.set_volume(ans/10)
    print(ans)


menu = Menu.Meny(window)
menu.add.button("ИГРАТЬ",menu.disable)
menu.add.selector("СЛОЖНОСТЬ",[("ЛЁГКАЯ",5),("СРЕДНЯЯ",6.1),("СЛОЖНАЯ",6)],onchange=diff)
menu.add.range_slider("ГРОМКОСТЬ МУЗЫКИ",3,list(range(8)),onchange=volume)
menu.add.button("ВЫХОД",quit)

bg_m = pygame.mixer.Sound("./music/background.mp3")
bg_m.set_volume(0.3)
bg_m.play(loops=-1)

eat_m = pygame.mixer.Sound("./music/eat.mp3")
eat_m.set_volume(0.8)

go_m = pygame.mixer.Sound("./music/gameover.mp3")
go_m.set_volume(0.8)

run = True
while run:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and not menu.is_enabled():
            snake.control(event)
    window.fill("grey")
    window.blit(bg["bkg"][hard_bg], rect)
    apple.rendering()
    snake.move()
    snake.defeat()
    apple.check()
    menu.flip(events)
    pygame.display.flip()
pygame.quit()