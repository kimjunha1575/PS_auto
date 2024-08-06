def solve(idx, cnt):
    if cnt == M:
        print(*buf, sep=' ')
        return
    for i in range(idx, N + 1):
        buf.append(i)
        solve(i, cnt + 1)
        buf.pop()


N, M = map(int, input().split())
buf = []
solve(1, 0)
