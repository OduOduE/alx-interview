#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    ''' Check if a queen can be placed at the given position
    without attacking other queens.
    '''
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def print_solution(board):
    # Print the solution in the desired format
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def nqueens(N, row=0, board=None):
    if board is None:
        board = [-1] * N

    if row == N:
        # Base case: all queens have been placed successfully
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens(N, row + 1, board)
            board[row] = -1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    nqueens(N)
