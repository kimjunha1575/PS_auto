from collections import deque


def ahri_move():
    global ahri_row, ahri_col, ahri_direction, ahri_hp
    for direction in range(ahri_direction, ahri_direction + 4):
        direction %= 4
        nr = ahri_row + DIRECTIONS[direction][0]
        nc = ahri_col + DIRECTIONS[direction][1]
        if not (0 <= nr < height and 0 <= nc < width) or cave[nr][nc] in [1, 3]:
            ahri_hp -= 1
            continue
        ahri_direction = direction
        cave[ahri_row][ahri_col] = 0
        ahri_row = nr
        ahri_col = nc
        cave[ahri_row][ahri_col] = 2
        break


def ahri_attack():
    global boss_hp
    boss_hp -= ahri_atk


def boss_move():
    global boss_row, boss_col, boss_direction
    if prev_ahri_row == ahri_row and prev_ahri_col == ahri_col:
        return
    boss_direction = ahri_direction
    cave[boss_row][boss_col] = 0
    boss_row = prev_ahri_row
    boss_col = prev_ahri_col
    cave[boss_row][boss_col] = 3


def find_stone():
    cr, cc = boss_row, boss_col
    visited = set()
    visited.add((cr, cc))
    searched = 1
    direction = boss_direction
    cr += DIRECTIONS[direction][0]
    cc += DIRECTIONS[direction][1]
    while searched < height * width:
        visited.add((cr, cc))
        if not (0 <= cr < height and 0 <= cc < width):
            right = (direction + 1) % 4
            nr = cr + DIRECTIONS[right][0]
            nc = cc + DIRECTIONS[right][1]
            if (nr, nc) in visited:
                cr += DIRECTIONS[direction][0]
                cc += DIRECTIONS[direction][1]
                continue
            direction = right
            cr = nr
            cc = nc
            continue
        searched += 1
        if cave[cr][cc] == 1:
            return cr, cc
        right = (direction + 1) % 4
        nr = cr + DIRECTIONS[right][0]
        nc = cc + DIRECTIONS[right][1]
        if (nr, nc) in visited:
            cr += DIRECTIONS[direction][0]
            cc += DIRECTIONS[direction][1]
            continue
        direction = right
        cr = nr
        cc = nc
    return -1, -1


def boss_attack():
    global ahri_hp
    tr, tc = find_stone()
    if tr < 0:
        return
    que = deque()
    visited = [[0] * width for _ in range(height)]
    que.append((tr, tc, boss_atk))
    visited[tr][tc] = 1
    while que:
        cr, cc, left_atk = que.popleft()
        if cave[cr][cc] == 2:
            ahri_hp -= left_atk
            return
        if left_atk == 1: continue
        for dr, dc in DIRECTIONS:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr < height and 0 <= nc < width): continue
            if visited[nr][nc]: continue
            if cave[nr][nc] in [1, 3]: continue
            que.append((nr, nc, left_atk - 1))
            visited[nr][nc] = 1


DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

height, width = map(int, input().split())
cave = [list(map(int, input().split())) for _ in range(height)]
ahri_hp, ahri_atk, boss_hp, boss_atk = map(int, input().split())

for r in range(height):
    for c in range(width):
        if cave[r][c] == 2:
            ahri_row = r
            ahri_col = c
            for i, (dr, dc) in enumerate(DIRECTIONS):
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < height and 0 <= nc < width): continue
                if cave[nr][nc] != 3: continue
                boss_row = nr
                boss_col = nc
                boss_direction = (i + 2) % 4
                ahri_direction = boss_direction
            break
    else:
        continue
    break

while True:
    ahri_attack()
    if boss_hp <= 0: break
    prev_ahri_row = ahri_row
    prev_ahri_col = ahri_col
    ahri_move()
    if ahri_hp <= 0: break
    boss_attack()
    if ahri_hp <= 0: break
    boss_move()

if ahri_hp > 0:
    print("VICTORY!")
else:
    print("CAVELIFE...")
