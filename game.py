import random
import numpy as np

def init_board():
    board = [[0] * 10 for _ in range(10)]
    for i in range(10):
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        board[row][column] = 9
    return board

def init_nums():
    board = init_board()



if __name__ == "__main__":
    init_board()
