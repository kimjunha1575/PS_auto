from collections import deque


def bfs(r, c):
    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    res = 0
    while que:
        cr, cc = que.popleft()
        res += 1
        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr < N and 0 <= nc < M): continue
            if visited[nr][nc]: continue
            if board[nr][nc] == 0: continue
            que.append((nr, nc))
            visited[nr][nc] = 1
    return res


N, M, K = map(int, input().split())
visited = [[0] * M for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
ans = 0
for row in range(N):
    for col in range(M):
        if board[row][col] and visited[row][col] == 0:
            ans = max(ans, bfs(row, col))
print(ans)
