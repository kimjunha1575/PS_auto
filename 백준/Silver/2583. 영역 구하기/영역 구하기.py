def dfs():
    global visited
    stk = [(r, c)]
    visited[r][c] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ret = 0
    while stk:
        cur = stk.pop()
        row = cur[0]
        col = cur[1]
        ret += 1
        for di in range(len(dr)):
            nr = row + dr[di]
            nc = col + dc[di]
            if nr < 0 or nc < 0 or nr >= height or nc >= width: continue
            if board[nr][nc] != 0: continue
            if visited[nr][nc]: continue
            visited[nr][nc] = 1
            stk.append((nr, nc))
    return ret


height, width, rectangles = map(int, input().split())
board = [[0] * width for _ in range(height)]
visited = [[0] * width for _ in range(height)]
for _ in range(rectangles):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = -1
region_cnt = 0
region_sizes = []
for r in range(height):
    for c in range(width):
        if board[r][c] == 0 and visited[r][c] == 0:
            region_cnt += 1
            region_sizes.append(dfs())
region_sizes.sort()
print(region_cnt)
print(*region_sizes, sep=' ')
