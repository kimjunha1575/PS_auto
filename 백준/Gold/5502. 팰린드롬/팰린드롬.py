def LCS():
    global dp
    for i in range(1, length+1):
        for j in range(1, length+1):
            if string[i-1] == string_rev[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


N = int(input())
string = input()
string_rev = string[::-1]
length = len(string)
dp = [[0] * (length+1) for _ in range(length+1)]
LCS()
print(length - dp[length][length])
