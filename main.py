def iterate_(board):
    return board+1
def solution(board):
    iteration = iterate_(board)
    return(board)
  
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
