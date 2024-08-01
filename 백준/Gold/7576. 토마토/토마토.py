from collections import deque


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
width, height = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
que = deque()
target_cnt = 0
for r in range(height):
    for c in range(width):
        if board[r][c] == 1:
            que.append((r, c))
        elif board[r][c] == 0:
            target_cnt += 1
ans = 0
if target_cnt == 0:
    que.clear()
    ans = 1
while que:
    cur = que.popleft()
    cr = cur[0]
    cc = cur[1]
    ans = max(ans, board[cr][cc])
    for di in range(4):
        nr = cr + dr[di]
        nc = cc + dc[di]
        if not (0 <= nr < height and 0 <= nc < width): continue
        if board[nr][nc] != 0: continue
        board[nr][nc] = board[cr][cc] + 1
        que.append((nr, nc))
        target_cnt -= 1
if target_cnt:
    print(-1)
else:
    print(ans-1)
