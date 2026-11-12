
n = int(input("Enter value of N: "))

board = [[0 for i in range(n)] for j in range(n)]

# Check if queen can be placed
def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False

    return True

# Solve using backtracking
def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False

# Place first queen
board[0][0] = 1

if solve(1):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")
