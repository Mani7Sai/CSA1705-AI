def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_queen(board, col, n, solutions):
    if col == n:
        solutions.append([row[:] for row in board])
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_queen(board, col + 1, n, solutions)
            board[row][col] = 0

def print_solution(solution):
    for row in solution:
        line = ['.'] * len(row)
        for i, val in enumerate(row):
            if val == 1:
                line[i] = 'Q'
        print(' '.join(line))
    print()

def main():
    n = int(input("Enter N: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_queen(board, 0, n, solutions)
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()
