
def calc_score():
    cur_idx = 0
    score = 0
    for i in range(N):
        if score + best_left[i] < ans:
            return 0
        out_count = 0
        base1 = 0
        base2 = 0
        base3 = 0
        while out_count < 3:
            hit = matrix[i][buf[cur_idx]]
            if hit == 0:
                out_count += 1
            elif hit == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif hit == 2:
                score += base3 + base2
                base3 = base1
                base2 = 1
                base1 = 0
            elif hit == 3:
                score += base3 + base2 + base1
                base3 = 1
                base2 = 0
                base1 = 0
            else:
                score += base3 + base2 + base1 + 1
                base3 = 0
                base2 = 0
                base1 = 0
            cur_idx = (cur_idx + 1) % 9
    return score


def solve(cnt):
    global ans
    if ans == best_left[0]:
        return
    if cnt == 9:
        ans = max(ans, calc_score())
        return
    if cnt == 3:
        buf[cnt] = 0
        solve(cnt + 1)
        return
    for i in range(1, 9):
        if visited[i]: continue
        buf[cnt] = i
        visited[i] = 1
        solve(cnt + 1)
        visited[i] = 0


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
best = []
for row in matrix:
    outs = row.count(0)
    if outs == 1:
        best.append(24)
    elif outs == 2:
        best.append(14)
    else:
        best.append(9 - outs)
best_left = [0] * (N + 1)
for i in range(N-1, -1, -1):
    best_left[i] = best_left[i+1] + best[i]
buf = [0] * 9
visited = [0] * 9
ans = 0
solve(0)
print(ans)
