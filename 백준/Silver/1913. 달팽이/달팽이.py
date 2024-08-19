
N = int(input())
target = int(input())
board = [[0] * N for _ in range(N)]
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
direction = 0
value = N**2
row = 0
col = 0
target_row = 0
target_col = 0
while value:
    if value == target:
        target_row = row
        target_col = col
    board[row][col] = value
    value -= 1

    nr = row + dirs[direction][0]
    nc = col + dirs[direction][1]
    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
        row = nr
        col = nc
        continue
    else:
        direction = (direction + 1) % 4
        row += dirs[direction][0]
        col += dirs[direction][1]
for row in board:
    print(*row, sep=' ')
print(target_row + 1, target_col + 1)
