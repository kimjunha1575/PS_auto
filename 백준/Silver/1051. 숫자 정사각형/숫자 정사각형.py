def is_right(board, row, c1, c2):
    sub = c2 - c1
    num = board[row][c1]
    if board[row + sub][c1] == board[row + sub][c2] == num:
        return True
    return False


def solve(matrix, row, col):
    ans = 1
    for r in range(row-1):
        for c in range(col-1):
            left = board[r][c]
            for i in range(c+1, col):
                right = board[r][i]
                if left == right and r + i - c < row:
                    if is_right(board, r, c, i):
                        ans = max(ans, (i - c + 1)**2)
    return ans


row, col = map(int, input().split())
board = [[0] * col for _ in range(row)]
for r in range(row):
    board[r] = list(map(int, input()))
print(solve(board, row, col))
