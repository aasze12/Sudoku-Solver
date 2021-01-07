board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def print_board(board):
    
    # If there is no board
    if board is None:
        return None
        print("Nothing!")

    if board == []:
        return None
        print("This is empty!")

    # boundary
    hor_boundary = "-" * 25
    ver_boundary = "| "

    num_rols = len(board)
    num_cols = len(board[0])

    for i in range(num_rols):
        if i % 3 == 0:
            print(hor_boundary)
        print_row = ""
        
        for j in range(num_cols):
            if j % 3 == 0:
                print_row += ver_boundary
            value = str(board[i][j])
            if board[i][j] != 0:
                value is True
            else:
                value == " "
            print_row += value + " "
        print_row += ver_boundary
        print(print_row)   

    print(hor_boundary)

def find_zero(board):
    num_rols = len(board)
    num_cols = len(board[0])

    for i in range(num_rols):
        for j in range(num_cols):
            if board[i][j] == 0:
                return [i,j]


def is_valid(board, row, col, value):

    # Check the row
    for i in board[row]:
        if i == value:
            return False

    # Check the column
    for j in board[col]:
        if j == value:
            return False

    # Check the grid
    x = (row // 3) * 3
    y = (col // 3) * 3

    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] == value:
                return False
    return True
