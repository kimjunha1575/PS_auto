def solve(i, j):
    if dp[i][j] is not None:
        return dp[i][j]
    tmp = 0
    for dr, dc in moves:
        nr = i + dr
        nc = j + dc
        if not (0 <= nr < height and 0 <= nc < width): continue
        if board[nr][nc] <= board[i][j]: continue
        tmp += solve(nr, nc)
    dp[i][j] = tmp
    return dp[i][j]


moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
height, width = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
dp = [[None] * width for _ in range(height)]
dp[0][0] = 1
solve(height-1, width-1)
print(dp[height-1][width-1])
