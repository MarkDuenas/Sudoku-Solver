import pygame
import random

pygame.font.init()

screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("Sudoku Solver")


def createBoard():
    Grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0

    for i in range(17):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)

        while(not checkValid(Grid, row, col, num) or Grid[row][col] != 0):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        Grid[row][col] = num
    
    return Grid

def checkValid(Grid, row, col, num):
    valid = True

    for x in range(9):
        if(Grid[x][col] == num):
            valid = False
    for y in range(9):
        if(Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    
    for x in range(3):
        for y in range(3):
            if(Grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid

x = 0
y = 0
dif = 500/9
val = 0

board = createBoard()

font1 = pygame.font.SysFont("comicsans", 40) 
font2 = pygame.font.SysFont("comicsans", 20) 
def get_cord(pos): 
    global x 
    x = pos[0]//dif 
    global y 
    y = pos[1]//dif 
  
# selected  cells
def draw_box(): 
    for i in range(2): 
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7) 
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)    
  
# draw lines for making Sudoku grid          
def draw(): 
    # Draw the lines 
    for i in range (9): 
        for j in range (9): 
            if board[i][j]!= 0: 
                pygame.draw.rect(screen, (148, 0, 211), (i * dif, j * dif, dif + 1, dif + 1)) 
                text1 = font1.render(str(board[i][j]), 1, (0, 0, 0)) 
                screen.blit(text1, (i * dif + 15, j * dif + 15)) 

    for i in range(10): 
        if i % 3 == 0 : 
            line = 7
        else: 
            line = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), line) 
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), line)       
  

def draw_val(val): 
    text1 = font1.render(str(val), 1, (0, 0, 0)) 
    screen.blit(text1, (x * dif + 15, y * dif + 15))     

def draw_val2(val):
    text1 = font1.render(str(val), 1, (255, 0, 0)) 
    screen.blit(text1, (x * dif + 15, y * dif + 15))     
  
# errors 
def error1(): 
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0)) 
    screen.blit(text1, (20, 570))   
def error2(): 
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0)) 
    screen.blit(text1, (20, 570))   
  
# Check if the value entered in board is valid 
def valid(m, i, j, val): 
    for it in range(9): 
        if m[i][it]== val: 
            return False
        if m[it][j]== val: 
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3): 
        for j in range (jt * 3, jt * 3 + 3): 
            if m[i][j]== val: 
                return False
    return True
  
# Solves board with back tracking
def solve(board, i, j): 
    while board[i][j]!= 0: 
        if i<8: 
            i+= 1
        elif i == 8 and j<8: 
            i = 0
            j+= 1
        elif i == 8 and j == 8: 
            return True

    pygame.event.pump()     
    for it in range(1, 10): 
        if valid(board, i, j, it) == True: 
            board[i][j]= it 
            global x, y 
            x = i 
            y = j 
            screen.fill((255, 255, 255)) 
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(20) 
            if solve(board, i, j)== 1: 
                return True
            else: 
                board[i][j]= 0
            
            screen.fill((255, 255, 255)) 
          
            draw()
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(50)     
    return False  
  

def instruction(): 
    text1 = font2.render("Press D to start over with new board", 1, (0, 0, 0)) 
    text2 = font2.render("Press Enter to solve", 1, (0, 0, 0)) 
    screen.blit(text1, (20, 520))         
    screen.blit(text2, (20, 540)) 
  
def result(): 
    text1 = font1.render("FINISHED PRESS D", 1, (0, 0, 0)) 
    screen.blit(text1, (20, 570))

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# main loop
while run: 
      
    # background
    screen.fill((255, 255, 255)) 
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False  
        # mouse position
        if event.type == pygame.MOUSEBUTTONDOWN: 
            flag1 = 1
            pos = pygame.mouse.get_pos() 
            get_cord(pos) 
        # key presses
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1: 
                val = 1
            if event.key == pygame.K_2: 
                val = 2    
            if event.key == pygame.K_3: 
                val = 3
            if event.key == pygame.K_4: 
                val = 4
            if event.key == pygame.K_5: 
                val = 5
            if event.key == pygame.K_6: 
                val = 6 
            if event.key == pygame.K_7: 
                val = 7
            if event.key == pygame.K_8: 
                val = 8
            if event.key == pygame.K_9: 
                val = 9  
            if event.key == pygame.K_RETURN: 
                flag2 = 1   
            # get new random board
            if event.key == pygame.K_d: 
                rs = 0
                error = 0
                flag2 = 0
                board = createBoard() 
    if flag2 == 1: 
        if solve(board, 0, 0) == False: 
            error = 1
        else: 
            rs = 1
        flag2 = 0    
    if val != 0:             
        draw_val2(val) 
        if valid(board, int(x), int(y), val)== True: 
            board[int(x)][int(y)]= val 
            flag1 = 0
            error = 0
        else: 
            error = 1
            board[int(x)][int(y)]= 0
        val = 0    
        
    if error == 1: 
        error1()

    if rs == 1: 
        result()

    draw()
       
    if flag1 == 1: 
        draw_box()

    instruction()     

    pygame.display.update()   
  

pygame.quit()      