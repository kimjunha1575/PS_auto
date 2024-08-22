
height, width = map(int, input().split())
obstacle_cnt = int(input())
obstacles = []
for _ in range(obstacle_cnt):
    obstacles.append(tuple(map(int, input().split())))
row, col = map(int, input().split())
dir_indeces = list(map(int, input().split()))
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [[0] * width for _ in range(height)]
for r, c in obstacles:
    board[r][c] = 1
tried = [0] * 4
can_move = True
dir_idx = 0
while can_move:
    if tried == [1, 1, 1, 1]:
        break
    nr = row + DIRECTIONS[dir_indeces[dir_idx] - 1][0]
    nc = col + DIRECTIONS[dir_indeces[dir_idx] - 1][1]
    if not (0 <= nr < height and 0 <= nc < width) or board[nr][nc]:
        dir_idx = (dir_idx + 1) % 4
        tried[dir_idx] = 1
        continue
    board[row][col] = 1
    row = nr
    col = nc
    tried = [0] * 4
    
print(row, col)
