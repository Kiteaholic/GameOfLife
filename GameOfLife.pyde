import random
import copy

w = 20
grid = []
gen = 0


#Rules
#1) 1 dead cell with 3 living neighbors becomes alive
#2) 1 living cell with less then 2 living neighbors dies
#3) 1 living cell with 2 or 3 neighbors stays alive
#4) 1 living cell with more then 3 living neighbors dies


def setup():
#    size(600,600)
    fullScreen()
    global cols
    global rows
    cols = int(width/w)
    rows = int(height/w)
    [[grid.append(Cell(x,y)) for x in range(cols)] for y in range(rows)]
    for i in range(int(len(grid)* 0.2)):
        random.choice(grid).alive = True



def draw():
#    noLoop()
    frameRate(5)
    global grid
    nextGen = []
    background(0)
    [x.show() for x in grid]
#Rules
    for i, x in enumerate(grid):
        n = x.checkNeighbors(grid)
        if not x.alive and n == 3:
            nextGen.append(i)
        elif x.alive and n == 2 or n ==3:
            nextGen.append(i)
    for x in grid:
        x.alive = False
    for i in nextGen:
        grid[i].alive = True

def index(i, j):
    if i < 0 or j < 0 or i > cols-1 or j > rows-1:
        return -1
    
    return i + j * cols
    

class Cell():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.x = i * w
        self.y = j * w
        self.alive = False
    
    def checkNeighbors(self, grid):
        count = 0
        i = self.i
        j = self.j
        neighbors = [[i-1,j-1],[i-1,j],[i-1,j+1],
        [i,j-1],[i,j+1],
        [i+1,j-1],[i+1,j],[i+1,j+1]]
        indexNeighbors = [index(x[0], x[1]) for x in neighbors]

        
        indexNeighbors = [x for x in indexNeighbors if x >= 0 and x <= len(grid)]
        for x in indexNeighbors:
            if grid[x].alive:
                count +=1
        return count
        
    
    
    def show(self):
        fill(255)
        stroke (0)
        strokeWeight(1)
        rect(self.x,self.y, w, w)
        if self.alive:
            fill(100 ,100 ,200 , 100)
            noStroke()
            rect(self.x,self.y,w,w)
        
        
        
        
        
