'''
1513 문제 읽기 시작
각 조건에 따라 작동방식이 전부 제시되어 있으므로, 그대로 구현하면 될 듯 함

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    반시계 방향으로 90도 회전한다.
    바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    1번으로 돌아간다.

1518 설계 시작
작동을 멈추는 경우는 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없고, 뒤쪽 칸이 벽이라 후진할 수 없는 경우 뿐이다
이 경우를 만났을 때 break로 반복문을 탈출하면 될 듯 함

방의 크기는 최대 50 * 50
이미 청소된 칸으로 이동하는 선택지는 애초에 없다. 최대 50 * 50
주어진 대로 구현만 하면 시간 안에 해결 가능할 것으로 예상.

1520 구현 시작
1540 구현 완료했으나 예제에서 오답 디버깅 시작
1551 디버거로 단계별 확인했으나 로직에서 큰 이상 없음 -> 다른 실수 확인해봄
     방향배열 잘못 적은 것 확인, 수정 후 예제에서 정답 확인, 제출

'''

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
height, width = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
cleaned = [[0] * width for _ in range(height)]
ans = 0
while True:
    if cleaned[r][c] == 0:
        cleaned[r][c] = 1
        ans += 1
    dirty_around = False
    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < height and 0 <= nc < width): continue
        if cleaned[nr][nc]: continue
        if board[nr][nc]: continue
        dirty_around = True
        break
    if dirty_around:
        d = (d - 1) % 4
        nr = r + DIRECTIONS[d][0]
        nc = c + DIRECTIONS[d][1]
        if not (0 <= nr < height and 0 <= nc < width): continue
        if board[nr][nc]: continue
        if cleaned[nr][nc]: continue
        r = nr
        c = nc
    else:
        nr = r - DIRECTIONS[d][0]
        nc = c - DIRECTIONS[d][1]
        if not (0 <= nr < height and 0 <= nc < width): break
        if board[nr][nc]: break
        r = nr
        c = nc

print(ans)
