from collections import deque


# 각 온풍기가 온도를 올리는 bfs 함수
def blow_warm_wind(row, col, direction):
    result = []
    que = deque()
    visited = [[0] * width for _ in range(height)]
    # 가장 초기 온도 증가량은 5
    init_heat = 5
    # 시계방향으로 90도 회전한 방향
    clockwise = (direction + 1) % 4
    # 반시계방향으로 90도 회전한 방향
    reverse_clockwise = (direction - 1) % 4
    # 인자로 주어진 행, 열의 값은 온풍기의 위치이므로 시작점은 방향에 따라 구해줘야 함
    sr = row + DIRECTIONS[direction][0]
    sc = col + DIRECTIONS[direction][1]
    # 시작위치 설정
    que.append((sr, sc, init_heat))
    visited[sr][sc] = 1
    while que:
        cr, cc, ch = que.popleft()
        # 온도 올려주기
        result.append((cr, cc, ch))
        # 온도가 1 올라간 곳은 더이상 다른 칸의 온도를 올려주지 못한다
        if ch == 1:
            continue
        # 바람의 이동방향(3방향)을 미리 저장해두고 사용함
        # i는 각 방향에 따라 다르게 처리해야 하는 부분이 있기 때문에 사용
        for i, (dr, dc) in enumerate(WIND_DIRECTIONS[direction]):
            nr = cr + dr
            nc = cc + dc
            nh = ch - 1
            if not (0 <= nr < height and 0 <= nc < width): continue
            if visited[nr][nc]: continue
            # 여기까지 평범한 bfs
            if i == 0:
                # i가 0이라면 진행방향의 좌측 대각선으로 이동하는 방향이다.
                # 이 때는 진행방향의 반시계 90도 방향에 있는 칸을 경유해서 지나가야 하고,
                # 중간에 벽이 있으면 안된다

                # 경유할 칸의 좌표
                tr = cr + DIRECTIONS[reverse_clockwise][0]
                tc = cc + DIRECTIONS[reverse_clockwise][1]
                # 경유할 칸에 목적지 방향으로 벽이 존재한다면 진행불가
                if wall[tr][tc] & (1 << direction): continue
                # 경유할 칸에 현재 위치 방향으로 벽이 존재한다면 진행 불가
                if wall[tr][tc] & (1 << clockwise): continue
            elif i == 1:
                # 대각선 방향이 아니라면 목적지와 현재 위치 사이에만 벽이 없으면 된다
                # 목적지와 현재 위치 사이에 벽이 존재한다면 진행 불가
                if wall[cr][cc] & (1 << direction): continue
            else:
                # i가 2라면 진행방향의 우측 대각선 방향으로 이동하는 방향이다
                # 이 때는 진행 방향의 시계 90도 방향에 있는 칸을 경유해서 지나간다

                # 경유할 칸의 좌표
                tr = cr + DIRECTIONS[clockwise][0]
                tc = cc + DIRECTIONS[clockwise][1]
                # 경유할 칸에 목적지방향, 혹은 현재위치 방향으로 벽이 있으면 진행 불가
                if wall[tr][tc] & (1 << direction): continue
                if wall[tr][tc] & (1 << reverse_clockwise): continue
            # 진행 가능하다면 que에 추가
            que.append((nr, nc, nh))
            visited[nr][nc] = 1
    return result


def calc_heat():
    for r, c, d in warmers:
        heated_result.append(blow_warm_wind(r, c, d))


def get_warm():
    for res in heated_result:
        for r, c, h in res:
            temp[r][c] += h



# 온도 조절 함수
def regulate():
    # 온도가 변화는 좌표와 변화량을 저장할 배열
    changes = []
    # 모든 좌표에 대해
    for r in range(height):
        for c in range(width):
            # 우, 하 방향으로만 탐색하면 된다 (모든 좌표에 대해 확인하므로)
            for direction, (dr, dc) in enumerate(DIRECTIONS[:2]):
                # 해당 방향으로 벽이 있다면 무시
                if wall[r][c] & (1 << direction):
                    continue
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < height and 0 <= nc < width): continue

                # 변화량 계산
                diff = abs(temp[r][c] - temp[nr][nc]) // 4
                # 변화량이 없다면 무시
                if diff == 0: continue
                # 변화량이 있다면 변화량 배열에 저장
                if temp[r][c] > temp[nr][nc]:
                    changes.append((r, c, -diff))
                    changes.append((nr, nc, diff))
                else:
                    changes.append((r, c, diff))
                    changes.append((nr, nc, -diff))
    # 온도 변화를 적용시켜준다 (동시에 적용되므로 따로 저장했다가 적용한다)
    for r, c, diff in changes:
        temp[r][c] += diff


# 테두리 부분의 온도를 1 낮추는 함수
def get_cold():
    # 온도가 0이 아닌 모든 테두리 칸들의 온도를 1 낮춘다
    for r, c in outer_areas:
        if temp[r][c]:
            temp[r][c] -= 1


# 온도를 조사할 칸의 온도가 K도 이상인지 확인하는 함수
def is_done():
    for r, c in target_positions:
        if temp[r][c] < target_temp:
            return False
    return True


DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
WIND_DIRECTIONS = (((-1, 1), (0, 1), (1, 1)),
                   ((1, 1), (1, 0), (1, -1)),
                   ((1, -1), (0, -1), (-1, -1)),
                   ((-1, -1), (-1, 0), (-1, 1)))

height, width, target_temp = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
wall_cnt = int(input())
wall = [[0] * width for _ in range(height)]
temp = [[0] * width for _ in range(height)]

outer_areas = []
warmers = []
target_positions = []
for r in range(height):
    for c in range(width):
        # 온풍기 정보를 온풍기 배열에 저장
        if 0 < board[r][c] < 5:
            if board[r][c] == 1:
                warmers.append((r, c, 0))
            elif board[r][c] == 2:
                warmers.append((r, c, 2))
            elif board[r][c] == 3:
                warmers.append((r, c, 3))
            elif board[r][c] == 4:
                warmers.append((r, c, 1))
        # 온도를 조사할 칸이라면 따로 배열에 저장
        elif board[r][c] == 5:
            target_positions.append((r, c))
        # 테두리 칸들의 좌표 미리 저장
        if r == 0 or c == 0 or r == height - 1 or c == width - 1:
            outer_areas.append((r, c))

# 벽 정보를 wall 매트릭스에 저장 (비트마스킹)
for _ in range(wall_cnt):
    r, c, t = map(int, input().split())
    if t:
        wall[r-1][c-1] = wall[r-1][c-1] | (1 << 0)
        wall[r-1][c] = wall[r-1][c] | (1 << 2)
    else:
        wall[r-2][c-1] = wall[r-2][c-1] | (1 << 1)
        wall[r-1][c-1] = wall[r-1][c-1] | (1 << 3)

heated_result = []
calc_heat()

# 초기값 설정
chocolate = 0
success = False
while True:
    # 모든 온풍기에서 바람을 쏴주고
    get_warm()
    # 온도를 조절하고
    regulate()
    # 테두리의 온도를 낮추고
    get_cold()
    # 초콜릿을 먹고
    chocolate += 1
    # 완료되었는 지 확인
    success = is_done()
    if chocolate == 100 or success:
        break

if success:
    print(chocolate)
else:
    print(101)
