import cv2
import pygame
import numpy as np

class Converter:
    def __init__(self, path, fsize = 8, depth = 8):
        self.fsize = fsize
        self.depth = depth
        self.path = path
        self.blacknwhite, self.colpic = self.load()
        self.width, self.height = self.blacknwhite.shape[:2]
        self.SYMBOLS = ' .,":;!-~+xmo*#W&8@'
        self.KOFF = 255 // (len(self.SYMBOLS) - 1)
        self.STEP = int(self.fsize * 0.3)
        pygame.init()
        self.font = pygame.font.SysFont('consolas', self.fsize, bold=True)
        self.RENDERS = [self.font.render(sym, True, "white") for sym in self.SYMBOLS]
        self.PALITRA, self.colkoff = self.palitre()

    def load(self):
        pic = cv2.imread(self.path)
        pic = cv2.transpose(pic)
        pic = cv2.resize(pic, dsize=(360, 384))
        blacknwhite = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)
        pic = cv2.cvtColor(pic, cv2.COLOR_RGB2BGR)
        #cv2.imshow("pic", blacknwhite)
        #cv2.waitKey(0)
        return blacknwhite, pic

    def convertation(self):
        surface = pygame.Surface((self.width, self.height))
        #print(self.blacknwhite)
        indexes = tuple(self.blacknwhite // self.KOFF)
        colindexes = tuple(self.colpic // self.colkoff)
        #print(indexes)
        for x in range(0, self.width, self.STEP):
            for y in range(0, self.height, self.STEP):
                index = indexes[x][y]
                if index:
                    color = tuple(colindexes[x][y])
                    sym = self.SYMBOLS[index]
                    surface.blit(self.PALITRA[sym][color], (x, y))
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

    def palitre(self):
        nums, col = np.linspace(0, 255, num=self.depth, dtype=int, retstep=True)
        print(nums, col)
        colpalitre = [np.array([r,g,b]) for r in nums for g in nums for b in nums]
        print(len(colpalitre))
        sympalitre = dict.fromkeys(self.SYMBOLS, None)
        for sym in sympalitre:
            singlesym = {}
            for color in colpalitre:
                key = tuple(color // col)
                singlesym[key] = self.font.render(sym, True, tuple(color))
            sympalitre[sym] = singlesym
        return sympalitre, col


if __name__ == "__main__":
    perem = Converter(r"C:\Users\Marar\Desktop\Rebotica\pirojki.jpg")
    perem.rendering()