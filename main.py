def is_valid_move(grid, row, col, number): 
  # check row
  for x in range(9):
    if grid[row][x] == number:
      return False
  # check col
  for x in range (9):
    if grid(x)[col] == number:
      return False
    
  corner_row = row - row % 3
  corner_col = col - col % 3


grid = [[0,0,0,0,0,0,6,8,0],
        [0,0,0,0,7,3,0,0,9],
        [3,0,9,0,0,0,0,4,5],
        [4,9,0,0,0,0,0,0,0],
        [8,0,3,0,5,0,9,0,2],
        [0,0,0,0,0,0,0,3,6],
        [9,6,0,0,0,0,3,0,8],
        [7,0,0,6,8,0,0,0,0],
        [0,2,8,0,0,0,0,0,0]]
