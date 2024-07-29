def tiktok():
    global board
    for r in range(R):
        for c in range(C):
            if board[r][c] != -1:
                board[r][c] += 1
            if cnt % 2 == 0 and board[r][c] == -1:
                board[r][c] = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 3:
                board[r][c] = -1
                for di in range(4):
                    nr = r + dr[di]
                    nc = c + dc[di]
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != 3:
                        board[nr][nc] = -1
    return None


R, C, N = map(int, input().split())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
board = []
for row in range(R):
    string = input()
    tmp = []
    for e in string:
        if e == '.':
            tmp.append(-1)
        else:
            tmp.append(0)
    board.append(tmp)
cnt = 0
while cnt < N:
    cnt += 1
    tiktok()
for row in range(R):
    for col in range(C):
        if board[row][col] >= 0:
            print('O', end='')
        else:
            print('.', end='')
    print()

