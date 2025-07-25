import copy

def iterate_(board):
    new_board = copy.deepcopy(board)

    num_rows = len(board)
    if num_rows == 0:
        return new_board
    num_cols = len(board[0])
    col_index = 0
    # Loop for every column (from 0 to the last one)
    explosions = []
    while col_index < num_cols:
        row_index = num_rows -2
        while row_index >= 0:
            if new_board[row_index][col_index] == '#':
                if new_board[row_index+1][col_index] == '-':
                    new_board[row_index+1][col_index] = '#'
                    new_board[row_index][col_index] = '-'
                if new_board[row_index+1][col_index] == '*':
                    explosions.append((row_index+1,col_index))
            row_index -=1
        col_index+=1
    print(f"explosions: {explosions}")
    for explo in explosions:
        assign_surrounding_cells(new_board, explo[0], explo[1], '-', '*')
    return new_board

def assign_surrounding_cells(matrix, row_idx, col_idx, value_to_assign, value_to_ignore):
    num_rows = len(matrix)
    if num_rows == 0:
        return

    num_cols = len(matrix[0])
    if num_cols == 0:
        return
    surrounding_deltas = [
        (-1, -1), (-1, 0), (-1, 1),  # Top row
        (0, -1),           (0, 1),   # Middle row (excluding center)
        (1, -1), (1, 0), (1, 1)    # Bottom row
    ]

    for dr, dc in surrounding_deltas:
        new_row, new_col = row_idx + dr, col_idx + dc

        # Check if the new coordinates are within the matrix boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if matrix[new_row][new_col] != value_to_ignore:
                matrix[new_row][new_col] = value_to_assign

def solution(board):
    current_board = board
    iteration_number = 1
    while True:
        next_board = iterate_(current_board)
        print(f"iteration n. {iteration_number}:{next_board}")
        if next_board == current_board:
            return next_board
        current_board = next_board
        iteration_number +=1
  
if __name__=="__main__":
    inpu = [
    ['#', '-', '#', '#', '*'],
    ['#', '-', '-', '#', '#'],
    ['-', '#', '-', '#', '-'],
    ['-', '-', '#', '-', '#'],
    ['#', '*', '-', '-', '-'],
    ['-', '-', '*', '#', '-']
    ]    
    print(f"inpu:{inpu}")
    exp_output = [
    ['-', '-', '-', '-', '*'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '*', '-', '-', '#'],
    ['#', '-', '*', '-', '#']
    ]
    print(f"exp_output:{exp_output}")
    sol = solution(inpu)
    print(f"sol:{sol}")
    print(f"sol==exp_output:{sol==exp_output}")
