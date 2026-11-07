#!/usr/bin/python3
"""Solve the N queens puzzle and print every solution."""
import sys


def is_safe(cols, row, col):
    """Return True if a queen at (row, col) is not attacked by earlier ones.

    Args:
        cols (list): cols[r] is the column of the queen placed on row r.
        row (int): the row of the new queen.
        col (int): the column of the new queen.
    """
    for r in range(row):
        c = cols[r]
        if c == col or abs(c - col) == row - r:
            return False
    return True


def solve(n, row, cols):
    """Place queens row by row with backtracking and print each solution.

    Args:
        n (int): the size of the board.
        row (int): the row on which the next queen is placed.
        cols (list): the columns of the queens already placed.
    """
    if row == n:
        print([[r, cols[r]] for r in range(n)])
        return
    for col in range(n):
        if is_safe(cols, row, col):
            cols.append(col)
            solve(n, row + 1, cols)
            cols.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [])
