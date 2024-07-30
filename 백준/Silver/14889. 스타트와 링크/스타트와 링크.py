def build_team(idx, t1, t2):
    global ans
    if idx == N:
        tmp1 = 0
        tmp2 = 0
        for i in range(N//2):
            for j in range(N//2):
                tmp1 += board[team1[i]][team1[j]]
                tmp2 += board[team2[i]][team2[j]]
        ans = min(ans, abs(tmp1 - tmp2))
        return None
    if t1 < N//2:
        team1.append(idx)
        t1 += 1
        build_team(idx + 1, t1, t2)
        team1.pop()
        t1 -= 1
    if t2 < N//2:
        team2.append(idx)
        t2 += 1
        build_team(idx + 1, t1, t2)
        team2.pop()
        t2 -= 1
    return None


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 1_000_000
team1 = []
team2 = []
build_team(0, 0, 0)
print(ans)
