def solve(cnt, acc, prev):
    global cur_best
    if acc + 200 * (N-cnt) < cur_best:
        return
    if cnt == N:
        cur_best = max(cur_best, acc)
        return
    for i in range(N):
        if used[i]: continue
        used[i] = 1
        solve(cnt + 1, acc + abs(arr[i] - prev), arr[i])
        used[i] = 0


N = int(input())
arr = list(map(int, input().split()))
cur_best = 0
used = [0] * N
for i in range(N):
    used[i] = 1
    solve(1, 0, arr[i])
    used[i] = 0
print(cur_best)
