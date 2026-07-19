#!/usr/bin/python3
"""N Queens puzzle solver"""
import sys


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions"""
    board = []

    def is_safe(row, col):
        """Check if a queen can be placed at row, col"""
        for r, c in board:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row):
        """Use backtracking to find all solutions"""
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_safe(row, col):
                board.append([row, col])
                backtrack(row + 1)
                board.pop()

    backtrack(0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_nqueens(N)
