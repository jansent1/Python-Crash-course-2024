class Board:
    def __init__(self, board):
        self.board = board
    def __str__(self):
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str
    # check for the first empty cell (0):
    def find_empty_cell(self):
      for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row,col
            except ValueError:
                pass
    # indicate the board is completely filled:
      return None
    # check if a given number can be added into a specified row of the board: 
    def valid_in_row(self, row, num):
        return num not in self.board[row]
    # Check if a given number can be added into a specified col of the board:
    def valid_in_col(self, col, num):
        return all((self.board[row][col] != num for row in range(9)))
    # Check if a given number can be added into a specified 3x3 square:
    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True
    # Check if a given number is a valid choice for an empty cell in the sudoku board by validating its compatibility with the row, column, and 3x3 square of the specified empty cell:
    def is_valid(self, empty, num):
        row,col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])
    # Method for solving the actual sudoku:
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1,10):
            if self.is_valid(next_empty, guess):
                row,col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver() == True:
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard


# the board will be a list of lists with 0 indicating the empty fields to solve:
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)

# gameboard = Board(puzzle)
# print(gameboard.board)
# print(gameboard.valid_in_row(0,8))
# print(gameboard.valid_in_col(0,7))
# print(gameboard.valid_in_square(1,0,3))