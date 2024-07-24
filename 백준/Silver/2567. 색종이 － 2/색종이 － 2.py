
board = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    col, row = map(int, input().split())
    for y in range(row, row + 10):
        for x in range(col, col + 10):
            board[y][x] = 1
ans = 0
board_t = list(zip(*board))
for y in range(1, 100):
    for x in range(1, 100):
        cur_color = board[y][x]
        prev_color = board[y][x-1]
        cur_color_t = board_t[y][x]
        prev_color_t = board_t[y][x-1]
        if prev_color == 0 and cur_color == 1:
            ans += 2
        if prev_color_t == 0 and cur_color_t == 1:
            ans += 2
print(ans)
