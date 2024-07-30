def dfs():
    global visited
    stk = [(r, c)]
    visited[r][c] = 1
    while stk:
        cur = stk.pop()
        row = cur[0]
        col = cur[1]
        for di in range(len(dr)):
            nr = row + dr[di]
            nc = col + dc[di]
            if not (0 <= nr < height and 0 <= nc < width): continue
            if board[nr][nc] != 1: continue
            if visited[nr][nc]: continue
            visited[nr][nc] = 1
            stk.append((nr, nc))


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for case in range(T):
    width, height, E = map(int, input().split())
    board = [[0] * width for _ in range(height)]
    visited = [[0] * width for _ in range(height)]
    ans = 0
    for _ in range(E):
        col, row = map(int, input().split())
        board[row][col] = 1
    for r in range(height):
        for c in range(width):
            if board[r][c] == 1 and visited[r][c] == 0:
                ans += 1
                dfs()
    print(ans)
