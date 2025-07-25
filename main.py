import copy

def iterate_(board):
    new_board = copy.deepcopy(board)

    num_rows = len(board)
    if num_rows == 0:
        return new_board
    num_cols = len(board[0])
    col_index = 0
    # Loop for every column (from 0 to the last one)
    while col_index < num_cols:
        # Step 1: Check if the current column contains '#'
        column_contains_hash = False
        for row_index_check in range(num_rows):
            if board[row_index_check][col_index] == '#':
                column_contains_hash = True
                break # Found '#', no need to check further in this column

        # If the column does not contain '#', move to the next column
        if column_contains_hash:
            row_index = num_rows -1
            while row_index >= 0:
                if new_board[row_index][col_index] == '#':
                    if row_index == num_rows -1:
                        pass
                    else:
                        pass
                if new_board[row_index][col_index] == '-':
                    pass
                if new_board[row_index][col_index] == '*':
                    pass
        col_index+=1

    return new_board
    
def solution(board):
    current_board = board
    while True:
        next_board = iterate_(current_board)
        print(f"next_board:{next_board}")
        if next_board == current_board:
            return next_board
        current_board = next_board
  
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
