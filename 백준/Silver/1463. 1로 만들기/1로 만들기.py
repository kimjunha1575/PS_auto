from collections import deque


N = int(input())
dp = [0, 1] + [0] * N
que = deque()
que.append((1, 1))
while que:
    if dp[N]: break
    value, steps = que.popleft()
    if value + 1 <= N and not dp[value + 1]:
        dp[value + 1] = steps + 1
        que.append((value + 1, steps + 1))
    if value * 2 <= N and not dp[value * 2]:
        dp[value * 2] = steps + 1
        que.append((value * 2, steps + 1))
    if value * 3 <= N and not dp[value * 3]:
        dp[value * 3] = steps + 1
        que.append((value * 3, steps + 1))

print(dp[N] - 1)
