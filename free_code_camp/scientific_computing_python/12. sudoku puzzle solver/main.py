class Board:
    def __init__(self, board):
        self.board = board
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
        pass


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

gameboard = Board(puzzle)
# print(gameboard.board)
# print(gameboard.valid_in_row(0,8))
# print(gameboard.valid_in_col(0,7))