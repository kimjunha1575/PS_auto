def solve(i, j):
    global dp
    global s1
    global s2
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])


s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
solve(0, 0)
print(dp[l1][l2])
