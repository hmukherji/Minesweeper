import random, sys
import numpy as np
import pygame as pg


random.seed(1)
HEIGHT = 400 #window dimensions
WIDTH = 400 #window dimensions
GREY = (128,128,128) #rgb value
WHITE = (200,200,200) #rgb value

def init_board():
    board = [[0] * 10 for _ in range(10)]
    for i in range(10):
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        board[row][column] = 9
    return board

def init_nums():
    board = init_board()
    # print(np.array(board))
    # print("\n")
    for row in range(1, len(board)-1):
        for col in range(1, len(board)-1):
            if board[row][col] !=9:
                neighbors(board, row, col)
    print(np.array(board))

def neighbors(board, row, col):
    return board

def create_grid():
    pg.init()
    square_size = 20
    win = pg.display.set_mode((HEIGHT, WIDTH))
    win.fill(GREY)
    done = False

    while not done:
        for x in range(WIDTH):
            for y in range(HEIGHT):
                rect = pg.Rect(x * square_size, y * square_size, square_size, square_size)
                pg.draw.rect(win, WHITE, rect, 1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        pg.display.update() #update display

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    init_nums()
    create_grid()
