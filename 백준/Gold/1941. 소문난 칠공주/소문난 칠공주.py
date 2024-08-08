from collections import deque


def validate():
    que = deque()
    visited = [[0] * 5 for _ in range(5)]
    sr, sc = group[0]
    visited[sr][sc] = 1
    que.append((sr, sc))
    cnt = 0
    while que:
        cr, cc = que.popleft()
        cnt += 1
        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr < 5 and 0 <= nc < 5): continue
            if (nr, nc) not in group: continue
            if visited[nr][nc]: continue
            que.append((nr, nc))
            visited[nr][nc] = 1
    return cnt == 7


def select(r, c, cnt, dasom):
    if dasom + (7 - cnt) < 4:
        return
    if cnt == 7:
        if validate():
            global ans
            ans += 1
        return
    for i in range(5):
        if i < r: continue
        for j in range(5):
            if i == r and j < c: continue
            group.append((i, j))
            if board[i][j] == 'S':
                select(i ,j, cnt + 1, dasom + 1)
            else:
                select(i, j, cnt + 1, dasom)
            group.pop()


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(input()) for _ in range(5)]
group = []
ans = 0
select(0, 0, 0, 0)
print(ans)
