def find_zero(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None


def is_valid(board, guess, row, col):

    # Check the rows first
    if guess in board[row]:
        return False

    # Then check the cols
    col_vals = []
    for i in range(9):
        col_vals.append(board[i][col])
    if guess in col_vals:
        return False

    # Check the 3x3 grid

    x = (row // 3) * 3
    y = (col // 3) * 3

    for r in range(x, x + 3):
        for c in range(y, y + 3):
            if board[r][c] == guess:
                return False

    return True


def solve(board):

    row, col = find_zero(board)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess
            if solve(board):
                return True

        board[row][col] = 0

    return False


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


print(solve(board))
print(board)
