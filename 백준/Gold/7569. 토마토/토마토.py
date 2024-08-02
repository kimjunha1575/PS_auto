from collections import deque


def solve():
    global board
    que = deque()
    premature = 0
    ret = 0
    for h in range(height):
        box = []
        for r in range(depth):
            row = list(map(int, input().split()))
            box.append(row)
            for c in range(len(row)):
                tomato = row[c]
                if tomato == 0:
                    premature += 1
                elif tomato == 1:
                    que.append((h, r, c))
        board.append(box)
    if premature == 0:
        return 0
    while que:
        cur_h, cur_r, cur_c = que.popleft()
        ret = max(ret, board[cur_h][cur_r][cur_c])
        for dh, dr, dc in directions:
            nh = cur_h + dh
            nr = cur_r + dr
            nc = cur_c + dc
            if not (0 <= nh < height and 0 <= nr < depth and 0 <= nc < width): continue
            if board[nh][nr][nc] != 0: continue
            board[nh][nr][nc] = board[cur_h][cur_r][cur_c] + 1
            que.append((nh, nr, nc))
            premature -= 1
    if premature:
        return -1
    return ret - 1


directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
width, depth, height = map(int, input().split())
board = []

print(solve())
