from utils import randcell

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]   
        self.h = h     
        self.w = w
        self.x = rx
        self.y = ry
        self.tank = 0
        self.maxtank = 1
        self.score = 0

    
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 ):
            self.x, self.y = nx, ny

    def print_stats(self):
        print('🚰 ', self.tank, '/', self.maxtank, sep='', end=' | ')
        print('🏅',  self.score)
