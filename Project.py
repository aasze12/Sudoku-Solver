board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Problem 1
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

# Problem 2
def find_zero(board):
    num_rols = len(board)
    num_cols = len(board[0])
    for i in range(num_rols):
        for j in range(num_cols):
            if board[i][j] == 0:
                return [i,j]

# Problem 3
def is_valid(board, row, col, value):
    num_rols = len(board)
    num_cols = len(board[0])
    
    for i in num_rols[row]:
        if i == value:
            return False
    
    for j in num_cols[col]:
        if j == value:
            return False
    return True