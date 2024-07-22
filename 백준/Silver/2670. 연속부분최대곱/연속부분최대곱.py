def solve(arr, memo, idx):
    if memo[idx]:
        return memo[idx]
    if idx == 0:
        memo[idx] = arr[0]
        return memo[idx]
    prev = solve(arr, memo, idx-1)
    if prev > 1:
        memo[idx] = prev * arr[idx]
    else:
        memo[idx] = arr[idx]
    return memo[idx]


N = int(input())
nums = []
dp = [None for _ in range(N)]
for _ in range(N):
    nums.append(float(input()))
ans = 0
for i in range(N):
    ans = max(ans, solve(nums, dp, i))

print(f"{ans:0.3f}")
