'''
좌표 (r, c) 까지 이동했을 때 가져올 수 있는 사탕의 최대 개수는
(r-1, c-1), (r-1, c), (r, c-1) 중 가장 많은 사탕을 가져올 수 있는 좌표에서 이동했을 때

dp[r][c] = board[r][c] + max(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
'''


height, width = map(int, input().split())
dp = [[0] * (width + 1) for _ in range(height + 1)]
# 계산 편하게 하려고 첫 행과 첫 열을 0으로 만들어서 채워줌
board = [[0] * (width + 1)]
for _ in range(height):
    board.append([0] + list(map(int, input().split())))
for r in range(1, height + 1):
    for c in range(1, width + 1):
        dp[r][c] = board[r][c] + max(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
print(dp[height][width])
