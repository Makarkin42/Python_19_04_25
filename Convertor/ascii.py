import numpy as np
import cv2
import pygame

class Converter:
    def __init__(self, path, fsize = 32):
        self.fsize = fsize
        self.path = path
        self.blacknwhite = self.load()
        self.width, self.height = self.blacknwhite.shape[:2]
        self.SYMBOLS = ' .,":;!-~+xmo*#W&8@'
        self.KOFF = 255 // (len(self.SYMBOLS) - 1)
        self.STEP = int(self.fsize * 0.6)
        pygame.init()
        self.font = pygame.font.SysFont('consolas', self.fsize, bold=True)
        self.RENDERS = [self.font.render(sym, True, "white") for sym in self.SYMBOLS]

    def load(self):
        pic = cv2.imread(self.path)
        pic = cv2.transpose(pic)
        pic = cv2.resize(pic, dsize=(360, 384))
        blacknwhite = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)
        #cv2.imshow("pic", blacknwhite)
        #cv2.waitKey(0)
        return blacknwhite

    def convertation(self):
        surface = pygame.Surface((self.width, self.height))
        #print(self.blacknwhite)
        indexes = self.blacknwhite // self.KOFF
        print(indexes)
        for x in range(0, self.width, self.STEP):
            for y in range(0, self.height, self.STEP):
                index = indexes[x, y]
                if index:
                    surface.blit(self.RENDERS[index], (x, y))
        return surface

    def rendering(self):
        self.convertation()
        self.output()


    def output(self):
        run = True
        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ascii")
        while run:
            events = pygame.event.get()
            for i in events:
                if i.type == pygame.QUIT:
                    run = False
            window.fill("black")
            res = self.convertation()
            window.blit(res, (0, 0))
            pygame.display.flip()


if __name__ == "__main__":
    perem = Converter(r"C:\Users\Marar\Desktop\Rebotica\pirojki.jpg")
    perem.rendering()