# # def updateBoard(board, move):
# #     """
# #     :type board: List[List[str]]
# #     :type move: List[int]
# #     :rtype: List[List[str]]
# #     """
# #     if board[move[0]][move[1]] == 9:
# #         #board[move[0]][move[1]] = -1
# #         return board
# #     neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
# #     dfs(move[0], move[1], len(board), len(board[0]), board, neighbors)
# #     return board
# #
# #
# # def dfs(i, j, m, n, board, neighbors):
# #     if board[i][j] != 0:
# #         return
# #     mine_count = 0
# #     for d in neighbors:
# #         if 0 <= i + d[0] < m and 0 <= j + d[1] < n and board[i + d[0]][j + d[1]] == 9:
# #             mine_count += 1
# #     if mine_count == 0:
# #         board[i][j] = -1
# #     else:
# #         board[i][j] = mine_count
# #         return
# #     for d in neighbors:
# #         if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
# #             dfs(i + d[0], j + d[1], m, n, board, neighbors)
# #
# #
# # def run(board):
# #     while True:
# #         a=[int(x) for x in (input("Choose square").split())]
# #         print(updateBoard(board, a))
# #     print("done")
# # if __name__ == "__main__":
# #     print(run([[0,0,9,9],
# #                [0,0,0,0],
# #                [0,0,0,0],
# #                [0,9,0,0]]))
#
# def updateBoard(board, click):
#     """
#     :type board: List[List[str]]
#     :type click: List[int]
#     :rtype: List[List[str]]
#     """
#     if not board or not board[0]:
#         return []
#     i, j = click[0], click[1]
#     if board[i][j] == "M":
#         board[i][j] = "X"
#         return board
#     m, n = len(board), len(board[0])
#     directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#     dfs(i, j, m, n, board, directions)
#     return board
#
# def dfs(i, j, m, n, board, directions):
#     if board[i][j] != "E":
#         return
#     mine_count = 0
#     for d in directions:
#         di, dj = i + d[0], j + d[1]
#         if 0 <= di < m and 0 <= dj < n and board[di][dj] == "M":
#             mine_count += 1
#     if mine_count == 0:
#         board[i][j] = "B"
#     else:
#         board[i][j] = str(mine_count)
#         return
#     for d in directions:
#         di, dj = i + d[0], j + d[1]
#         if 0 <= di < m and 0 <= dj < n:
#             dfs(di, dj, m, n, board, directions)
#
#
# if __name__ == "__main__":
#     print(updateBoard([['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']], [3,0]))


def uncover_squares(board, move):
    """
    :type board: List[List[str]]
    :type move: List[int]
    :rtype: List[List[str]]
    """
    if board[move[0]][move[1]] == 9:
        #board[move[0]][move[1]] = -1
        return board
    neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    dfs(move[0], move[1], len(board), len(board[0]), board, neighbors)
    return board


def dfs(i, j, m, n, board, neighbors):
    if board[i][j] != 0:
        return
    mine_count = 0
    for d in neighbors:
        if 0 <= i + d[0] < m and 0 <= j + d[1] < n and board[i + d[0]][j + d[1]] == 9:
            mine_count += 1
    if mine_count == 0:
        board[i][j] = -1
    else:
        board[i][j] = mine_count
        return
    for d in neighbors:
        if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
            dfs(i + d[0], j + d[1], m, n, board, neighbors)

if __name__ == "__main__":
    print(uncover_squares([[0,0,9,9],
               [0,0,0,0],
               [0,0,0,0],
               [0,9,0,0]], [1,0]))

    # def init_nums():
    #     board = init_board()
    #     print(np.array(board))
    #     print("\n")
    #     for row in range(len(board)):
    #         for col in range(len(board)):
    #             if board[row][col] != 9:
    #                 if row !=0:
    #                     if board[row - 1][col] == 9:
    #                         board[row][col] += 1
    #
    #                     if col != 0:
    #                         if board[row-1][col-1] == 9:
    #                             board[row][col]+=1
    #                     if col != 9:
    #                         if board[row - 1][col + 1] == 9:
    #                             board[row][col] += 1
    #
    #                 if col != 0:
    #                     if board[row][col-1]== 9:
    #                         board[row][col]+=1
    #                     if row != 9:
    #                         if board[row+1][col-1]== 9:
    #                             board[row][col] += 1
    #
    #                 if row != 9:
    #                     if board[row+1][col]== 9:
    #                         board[row][col]+=1
    #                 if col != 9:
    #                     if board[row][col+1]== 9:
    #                         board[row][col]+=1
    #                     if row != 9:
    #                         if board[row+1][col+1]== 9:
    #                             board[row][col]+=1
    #     print(np.array(board))
    #     return board
