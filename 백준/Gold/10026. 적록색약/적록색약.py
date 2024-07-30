def dfs(board):
    st = [(r, c)]
    while st:
        cur = st.pop()
        cur_row = cur[0]
        cur_col = cur[1]
        cur_color = board[cur_row][cur_col]
        for di in range(4):
            nr = cur_row + dr[di]
            nc = cur_col + dc[di]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc]: continue
            if board[nr][nc] != cur_color: continue
            visited[nr][nc] = 1
            st.append((nr, nc))
    pass


N = int(input())
board_normal = []
board_colorblind = [[0] * N for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ans_normal = 0
ans_colorblind = 0
for row in range(N):
    ipt = list(input())
    board_normal.append(ipt)
    for col in range(N):
        if ipt[col] == 'G':
            board_colorblind[row][col] = 'R'
        else:
            board_colorblind[row][col] = ipt[col]
visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            ans_normal += 1
            visited[r][c] = 1
            dfs(board_normal)
visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            ans_colorblind += 1
            visited[r][c] = 1
            dfs(board_colorblind)
print(ans_normal, ans_colorblind)
