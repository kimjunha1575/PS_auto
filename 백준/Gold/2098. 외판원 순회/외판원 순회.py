def solve(idx, visited):
    # 저장된 값이라면 바로 반환
    if dp[idx][visited]:
        return dp[idx][visited]
    res = INF
    for i in range(N):
        # 갈 수 없는 곳은 가지 않는다
        if board[idx][i] == 0: continue
        # 이미 들른 곳은 가지 않는다
        if visited & (1 << i): continue
        # 아직 들르지 않은 곳 중 경로가 최소가 되는 곳을 들른다
        res = min(res, solve(i, visited | 1 << i) + board[idx][i])
    dp[idx][visited] = res
    return dp[idx][visited]


INF = 1_000_000_000
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
for i in range(N):
    if board[i][0]:
        dp[i][(1 << N) - 1] = board[i][0]
    else:
        dp[i][(1 << N) - 1] = INF
print(solve(0, 1))
