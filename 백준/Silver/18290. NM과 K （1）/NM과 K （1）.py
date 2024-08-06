def solve(acc, cnt, row, col):
    if cnt == K:
        global ans
        ans = max(ans, acc)
        return
    for r in range(N):
        if r < row: continue
        for c in range(M):
            if r == row and c < col: continue
            if visited[r][c]: continue
            cannot_choose = False
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < N and 0 <= nc < M): continue
                if visited[nr][nc] == 1:
                    cannot_choose = True
                    break
            if cannot_choose: continue
            visited[r][c] = 1
            solve(acc + board[r][c], cnt + 1, r, c)
            visited[r][c] = 0


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * M for _ in range(N)]
ans = -1_000_000_000
solve(0, 0, 0, 0)
print(ans)
