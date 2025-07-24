def iterate_(board):
    
    return new_board

def solution(board):
    current_board = board
    while True:
        next_board = iterate_(current_board)
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
