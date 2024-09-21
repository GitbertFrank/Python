def ft_ten_queens_puzzle():
    def is_safe(board, row, col):
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solve(board, col):
        if col == 10:
            solutions.append(board[:])
            return
        for row in range(10):
            if is_safe(board, row, col):
                board[col] = row
                solve(board, col + 1)
                board[col] = -1

    solutions = []
    board = [-1] * 10
    solve(board, 0)
    
    for solution in solutions:
        print(''.join(map(str, solution)))
    
    return len(solutions)

# Test the function
print(ft_ten_queens_puzzle())