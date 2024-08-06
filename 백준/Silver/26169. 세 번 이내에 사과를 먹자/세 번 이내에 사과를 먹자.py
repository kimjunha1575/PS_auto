def solve(game_board, cnt, apple, row, col):
    cur_map = game_board.copy()
    if apple == 2:
        return 1
    if cnt == 3:
        return 0
    for dr, dc in directions:
        nr = row + dr
        nc = col + dc
        if not (0 <= nr < 5 and 0 <= nc < 5): continue
        if cur_map[nr][nc] == -1: continue
        cur_map[row][col] = -1
        if solve(cur_map, cnt + 1, apple + cur_map[nr][nc], nr, nc):
            return 1
        cur_map[row][col] = 0
    return 0


board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
print(solve(board, 0, 0, r, c))
