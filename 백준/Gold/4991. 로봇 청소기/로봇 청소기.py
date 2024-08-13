from collections import deque


def solve(n):
    if n == dirty_idx:
        global ans
        res = start_to_dirt[dirt_order[0]]
        for i in range(1, dirty_idx):
            res += dirt_to_dirt[dirt_order[i- 1]][dirt_order[i]]
        ans = min(ans, res)
        return
    for i in range(dirty_idx):
        if cleaned[i]: continue
        cleaned[i] = 1
        dirt_order.append(i)
        solve(n+1)
        dirt_order.pop()
        cleaned[i] = 0


def get_dist(sr, sc):
    que = deque()
    visited = [[0] * width for _ in range(height)]
    si = board[sr][sc]
    que.append((sr, sc, 0))
    visited[sr][sc] = 1
    while que:
        cr, cc, cd = que.popleft()
        if isinstance(board[cr][cc], int):
            dirt_to_dirt[si][board[cr][cc]] = cd
        if board[cr][cc] == 'o':
            start_to_dirt[si] = cd
        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            nd = cd + 1
            if not (0 <= nr < height and 0 <= nc < width): continue
            if visited[nr][nc]: continue
            if board[nr][nc] == FURNITURE: continue
            que.append((nr, nc, nd))
            visited[nr][nc] = 1


FURNITURE = 'x'
DIRTY = '*'
CLEAN = '.'
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while True:
    width, height = map(int, input().split())
    if not width and not height:
        break
    board = [list(input()) for _ in range(height)]
    dirty_blocks = []
    dirty_idx = 0
    for r in range(height):
        for c in range(width):
            if board[r][c] == 'o':
                starting_point = (r, c)
            elif board[r][c] == DIRTY:
                dirty_blocks.append((r, c))
                board[r][c] = dirty_idx
                dirty_idx += 1
    # r번 더러운 칸에서 c번 더러운 칸 까지 가는 최단경로
    dirt_to_dirt = [[0] * len(dirty_blocks) for _ in range(len(dirty_blocks))]
    start_to_dirt = [0] * dirty_idx
    for r in range(height):
        for c in range(width):
            if isinstance(board[r][c], int):
                get_dist(r, c)
    can_clean = True
    for dist in start_to_dirt:
        if not dist:
            can_clean = False
            break
    if can_clean:
        ans = 1_000_000_000
        dirt_order = []
        cleaned = [0] * dirty_idx
        solve(0)
        print(ans)
    else:
        print(-1)
