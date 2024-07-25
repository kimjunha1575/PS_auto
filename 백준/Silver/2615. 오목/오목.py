def is_game_over(r, c):
    global win_y
    global win_x
    color = board[r][c]
    dr = [0, 1, 1, -1]
    dc = [1, 1, 0, 1]
    for di in range(4):
        pr = r - dr[di]
        pc = c - dc[di]
        if 0 <= pr < 19 and 0 <= pc < 19 and board[pr][pc] == color:
            continue
        nr = r
        nc = c
        length = 1
        for _ in range(5):
            nr += dr[di]
            nc += dc[di]
            if 0 <= nr < 19 and 0 <= nc < 19:
                if board[nr][nc] == color:
                    length += 1
                else:
                    break
        if length == 5:
            win_y = r + 1
            win_x = c + 1
            return color
    return 0


def search():
    for y in range(19):
        for x in range(19):
            if board[y][x] > 0:
                winner = is_game_over(y, x)
                if winner:
                    return winner


board = []
for _ in range(19):
    row = list(map(int, input().split()))
    board.append(row)
win_y = 0
win_x = 0
ans = search()
if ans:
    print(ans)
    print(win_y, win_x)
else:
    print(0)
