# Suoku-Solver

Problem 1: Print the Sudoku board

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0]]
         
Problem 2: Find empty cell
Write a function that finds the first empty cell. This will be useful for your function to know which cell to try to fill. In our case, let’s read the board from left to right, and top down. So in our example, the first cell is the cell in the first row and on the 3rd column.

The output of that function should be a list of size 2. The first element of the list is the row number and the second element of the list is the col number.

Problem 3: Is Valid Placement?
Write a function that takes in the board, the position (row and column) and a value (1 to 9) and determines if it’s legal to place that number on the cell. To do that, you will check the entire row to see if there is a number that matches your value. If there is, then you cannot place that value on that cell. You will do the same with the entire column, and then you will do the same with the 3x3 grid. The output should simply be a Boolean value.

The output of the function should be True or False. True meaning you can place that value on that cell.
