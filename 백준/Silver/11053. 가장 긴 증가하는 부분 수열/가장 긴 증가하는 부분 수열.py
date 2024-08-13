'''
Longest Increasing Subsequence (LIS)
dp[i]: 현재 원소를 마지막으로 가지는 가장 긴 증가하는 부분 수열의 길이
0번째부터 i-1번째까지 순회하면서 dp[i]를 갱신한다
0 <= p < q일 때
arr[q]가 arr[p]보다 크다면 dp[q] = max(dp[q], dp[p] + 1)
'''
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
