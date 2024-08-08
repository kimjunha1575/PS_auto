'''
dp[n]: n일 차를 포함한 그 이후로 얻을 수 있는 최대 수익
따라서
n일 차에 잡힌 상담이 x일이 걸린다고 했을 때,
dp[n]는
k는 0 ~ x-1에 대해
max( sum( dp[n+k] ), dp[n+x] + + arr[n] )
'''


def solve(idx):
    if idx >= N:
        return 0
    if dp[idx]:
        return dp[idx]
    effort, pay = meetings[idx]
    if idx + effort > N:
        pay = 0
    nxt = solve(idx + effort)
    res = nxt + pay
    for i in range(1, effort):
        res = max(res, solve(idx + i))
    dp[idx] = res
    return dp[idx]


N = int(input())
meetings = []
for _ in range(N):
    effort, pay = map(int, input().split())
    meetings.append((effort, pay))
dp = [0] * N
solve(0)
print(dp[0])
