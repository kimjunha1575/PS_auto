from collections import deque


def bfs():
    global visited
    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    while que:
        cur = que.popleft()
        cr = cur[0]
        cc = cur[1]
        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc]: continue
            if board[nr][nc] <= rain: continue
            que.append((nr, nc))
            visited[nr][nc] = 1


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

mi = 100
ma = 0
for r in range(N):
    for c in range(N):
        mi = min(mi, board[r][c])
        ma = max(ma, board[r][c])
ans = 1
for rain in range(mi, ma):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            if board[r][c] <= rain: continue
            bfs()
            cnt += 1
    ans = max(ans, cnt)
print(ans)
