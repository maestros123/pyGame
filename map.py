from utils import randbool
from utils import randcell
from utils import randcell2

CELL_TYPES = '🧱🌴🌊🏥🏪🔥⚫️'

class Map:
    def __init__(self, w, h):
            self.w = w
            self.h = h
            self.cells =[[0 for i in range(w)] for j in range(h)]

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x>= self.h or y >= self.w):
            return False
        return True

    def print_map(self, helico):
        print('🔲' * (self.w + 2))
        for ri in range(self.h):
            print('🔲', end='')
            for ci in range(self.w): 
                cell = self.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif (cell >= 0 and cell < len(CELL_TYPES)):  
                    print(CELL_TYPES[cell], end='')
            print('🔲')        
        print('🔲' * (self.w + 2))
    
    

    

    # Генерируем реку
    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[1], rc[0]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                if (self.cells[rx2][ry2] == 2):
                    rx, ry = rx2, ry2
                    l -= 1

                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    # Генерируем деревья
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    # Зажечь огонь на рандомном дереве
    def generate_fire(self):
        fc = randcell(self.w, self.h)
        fx, fy = fc[1], fc[0]

        if self.cells[fx][fy] == 1:
            self.cells[fx][fy] = 5
    
    # Сжечь деревья, добавить новые пожары 
    def update_fire(self):
        fire = 1
        for ri in range(self.h):
            for ci in range(self.w):
                if self.cells[ri][ci] == 5:
                    self.cells[ri][ci] = 0

                    rc2 = randcell2(ri, ci)
                    rx2, ry2 = rc2[0], rc2[1]
                    
                    if (self.check_bounds(rx2, ry2) and self.cells[rx2][ry2] == 1):
                        self.cells[rx2][ry2] = 5
                        fire += 1    

        for i in range(fire, 0, -1):
            self.generate_fire()


    # Добавление новых деревьев
    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1



    
    

