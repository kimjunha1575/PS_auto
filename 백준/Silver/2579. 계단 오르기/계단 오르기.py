'''
직전 계단을 밟았다면 다음 계단은 밟지 못한다
dp[n]: n 번째 계단 까지의 최대점수

n번째 계단을 밟으면서 얻을 수 있는 최대 점수는
n-3번째 계단 > n-1번째 계단 > n번째 계단 순서로 밟아 올라오거나
n-3번째 계단 > n-2번째 계단 > n번째 계단 순서로 밟아 올라오는
2가지 경우 중 하나이다.
(한번에 세 계단을 오를 수 없고, 연속된 세 계단을 오를 수 없기 때문에)

따라서 점화식은
dp[n] = stairs[n] + max(stairs[n-1] + dp[n-3], dp[n-2])
'''


def solve(n):
    if n <= 0: return 0
    if dp[n]: return dp[n]
    dp[n] = stairs[n] + max(stairs[n-1] + solve(n-3), solve(n-2))
    return dp[n]


N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)
solve(N)
print(dp[N])
