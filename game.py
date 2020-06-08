import random, sys
import numpy as np
import pygame as pg


#random.seed(1)
HEIGHT = 200 #window dimensions
WIDTH = 200 #window dimensions
GREY = (128,128,128) #rgb value
WHITE = (200,200,200) #rgb value
BLACK = (255, 0, 0)

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

    done = False
    while not done:
        for x in range(10):
            for y in range(10):
                rectColor = WHITE
                rect = pg.Rect(x * square_size, y * square_size, square_size, square_size)
                if board[x][y]==9:
                    rectColor=BLACK
                    pg.draw.rect(win, rectColor, rect, 0)
                pg.draw.rect(win, rectColor, rect, 1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        pg.display.update() #update display

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    create_grid()
