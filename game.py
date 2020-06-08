import random, sys
import numpy as np
import pygame as pg

HEIGHT = 200 #window dimensions
WIDTH = 200
GREY = (128,128,128) #rgb value
WHITE = (200,200,200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)

random.seed(1)

def init_board():
    board = [[0] * 10 for _ in range(10)]
    for i in range(10):
        row = random.randint(1, 9)
        column = random.randint(1, 9)
        board[row][column] = 9
    return board

def init_nums():
    board = init_board()
    # print(np.array(board))
    # print("\n")
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != 9:
                if row !=0:

                    if col != 0:
                        if board[row-1][col-1] == 9:
                            board[row][col]+=1
                    if board[row - 1][col] == 9:
                        board[row][col] += 1
                    if col != 9:
                        if board[row - 1][col + 1] == 9:
                            board[row][col] += 1

                if col != 0:
                    if board[row][col-1]== 9:
                        board[row][col]+=1
                    if row != 9:
                        if board[row+1][col-1]== 9:
                            board[row][col] += 1

                if row != 9:
                    if board[row+1][col]== 9:
                        board[row][col]+=1
                if col != 9:
                    if board[row][col+1]== 9:
                        board[row][col]+=1
                    if row != 9:
                        if board[row+1][col+1]== 9:
                            board[row][col]+=1
    print(np.array(board))
    return board

def create_grid():
    board = init_nums()
    #print(board)
    pg.init()
    square_size = 20
    win = pg.display.set_mode((HEIGHT, WIDTH))
    win.fill(GREY)
    pg.display.set_caption("Minesweeper")
    font = pg.font.SysFont('Arial', 25)
    IMAGE = pg.image.load("bomb.png")
    rect2 = IMAGE.get_rect()
    clickable = True
    done = False

    while not done:
        for x in range(10):
            for y in range(10):
                rectColor = WHITE
                rect = pg.Rect(y * square_size, x * square_size, square_size, square_size)
                pg.draw.rect(win, rectColor, rect, 1)

        for event in pg.event.get():
            if clickable and event.type == pg.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pg.mouse.get_pos()
                if board[Mouse_y //20 ][Mouse_x//20] == 1:
                    win.blit(font.render('1', True, RED),(Mouse_x//20 * 20, Mouse_y//20 * 20) )
                if board[Mouse_y//20 ][Mouse_x//20] == 2:
                    win.blit(font.render('2', True, BLUE),(Mouse_x//20 * 20, Mouse_y//20 * 20) )
                if board[Mouse_y //20 ][Mouse_x//20] == 3:
                    win.blit(font.render('3', True, PURPLE),(Mouse_x//20 * 20, Mouse_y//20 * 20) )
                if board[Mouse_y //20 ][Mouse_x//20] == 9:
                    win.blit(IMAGE, (Mouse_x//20 * 20, Mouse_y//20 * 20), rect2)
                    clickable= False
                    pg.display.set_caption("You lost!")
            if event.type == pg.QUIT:
                done = True
        pg.display.update() #update display

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    create_grid()
