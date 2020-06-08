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
BOARD_SIZE = 10

colors = {1:RED, 2:BLUE, 3:GREEN}
random.seed(1)

def init_board():
    board = [[0] * 10 for _ in range(BOARD_SIZE)]
    for i in range(BOARD_SIZE):
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
    SQUARE_SIZE = 20
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
                rect = pg.Rect(y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pg.draw.rect(win, rectColor, rect, 1)

        for event in pg.event.get():
            if clickable and event.type == pg.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pg.mouse.get_pos()
                if board[Mouse_y //20 ][Mouse_x//20] != 9 and board[Mouse_y //20 ][Mouse_x//20] != 0:
                   render_num(win,font, board[Mouse_y //20 ][Mouse_x//20],
                              colors[board[Mouse_y //20][Mouse_x//20]], Mouse_x, Mouse_y)
                if board[Mouse_y //20 ][Mouse_x//20] == 9:
                    win.blit(IMAGE, (Mouse_x//20 * 20, Mouse_y//20 * 20), rect2)
                    clickable= False
                    pg.display.set_caption("You lost!")
            if event.type == pg.QUIT:
                done = True
        pg.display.update() #update display

    pg.quit()
    sys.exit()

def render_num(screen, font, num, color, mouse_x, mouse_y):
    screen.blit(font.render(str(num), True, color), (mouse_x // 20 * 20, mouse_y // 20 * 20))


if __name__ == "__main__":
    create_grid()
