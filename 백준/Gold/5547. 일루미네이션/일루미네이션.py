from collections import deque


def bfs(r, c):
    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    res = 0
    while que:
        cr, cc = que.popleft()
        if cr % 2 == 1:
            dirs = directions_odd
        else:
            dirs = directions_even
        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr < H + 2 and 0 <= nc < W + 2): continue
            if visited[nr][nc]: continue
            if board[nr][nc] == 1:
                res += 1
                continue
            que.append((nr, nc))
            visited[nr][nc] = 1
    return res


directions_odd = [(-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (-1, 0)]
directions_even = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
W, H = map(int, input().split())
board = [[0] * (W + 2)]
for _ in range(H):
    board.append([0] + list(map(int, input().split())) + [0])
board.append([0] * (W+2))
visited = [[0] * (W + 2) for _ in range(H + 2)]
print(bfs(0, 0))
