from utils import randbool
from utils import randcell
from utils import randcell2
from utils import randnumber

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
        trees = []
        for ri in range(self.h):
            for ci in range(self.w):
                if self.cells[ri][ci] == 1:
                    trees.append([ri , ci])
        max = len(trees)
        r = randnumber(max-1)
        
        if (max > 1):
            tx, ty = trees[r][0], trees[r][1]   
            self.cells[tx][ty] = 5




    
    # Сжечь деревья, добавить новые пожары 
    def update_fire(self):
        tr =  1
        for ri in range(self.h):
            for ci in range(self.w):
                if self.cells[ri][ci] == 5:
                    self.cells[ri][ci] = 6
                    tr += 1
                
        for i in range(tr, 0, -1):
            self.generate_fire()

    # Добавление новых деревьев
    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    # Место для увеличения бака воды 
    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4


    # Механика тушения пожара и набора очков
    def check_water(self, helico):
        if self.cells[helico.x][helico.y] == 2:
            helico.tank = helico.maxtank
        elif (self.cells[helico.x][helico.y] == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += 100
            self.cells[helico.x][helico.y] = 1
        elif (self.cells[helico.x][helico.y] == 4 and helico.score >= 500):
            helico.maxtank += 1
            helico.score -= 500