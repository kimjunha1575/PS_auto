
N = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N+1)]
for i in range(10):
    dp[0][i][1 << i] = 1

for n in range(N):
    for i in range(10):
        for used in range(1 << 10):
            if i > 0:
                dp[n+1][i-1][used | (1 << (i-1))] += dp[n][i][used]
            if i < 9:
                dp[n+1][i+1][used | (1 << (i+1))] += dp[n][i][used]

ans = 0
for i in range(1, 10):
    ans += dp[N-1][i][(1 << 10) - 1]
print(ans % 1_000_000_000)
