N = int(input())
dp = [0, 1] + [0] * N
for i in range(2, N + 1):
    res = 1_000_000_000
    if not i % 3:
        res = min(res, dp[i//3] + 1)
    if not i % 2:
        res = min(res, dp[i//2] + 1)
    res = min(res, dp[i-1] + 1)
    dp[i] = res

print(dp[N] - 1)
