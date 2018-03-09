from __future__ import print_function
import numpy as np


def exist_word(board, x, y, word, visited):
    if len(word) == 0 or (len(word) == 1 and word == board[x][y]):
        return True

    if word[0] != board[x][y]:
        return False

    visited[x][y] = 1
    sub_word = word[1:]
    m = len(board)
    n = len(board[0])

    if x - 1 >= 0 and visited[x - 1][y] == 0:
        if exist_word(board, x - 1, y, sub_word, visited):
            return True

    if x + 1 < m and visited[x + 1][y] == 0:
        if exist_word(board, x + 1, y, sub_word, visited):
            return True

    if y - 1 >= 0 and visited[x][y - 1] == 0:
        if exist_word(board, x, y - 1, sub_word, visited):
            return True

    if y + 1 < n and visited[x][y + 1] == 0:
        if exist_word(board, x, y + 1, sub_word, visited):
            return True

    visited[x][y] = 0
    return False


def find_word(board, word):
    if board is None or len(board) == 0:
        return False
    m = len(board)
    n = len(board[0])
    visited = np.zeros((m, n))
    for i in range(0, m):
        for j in range(0, n):
            if exist_word(board, i, j, word, visited):
                return True

    return False


def main():
    board = [['D', 'O', 'G'],
             ['A', 'Y', 'G'],
             ['C', 'D', 'B']]

    word = 'DOGGY'
    result = find_word(board, word)
    print(result)


if __name__ == '__main__':
    main()
