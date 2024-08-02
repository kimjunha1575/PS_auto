import sys


def get_area(position):
    # 좌표 정보 -> 넓이
    y1, x1, y2, x2 = position
    return areas[y2][x2] - areas[y1-1][x2] - areas[y2][x1-1] + areas[y1-1][x1-1]


# 누적합 배열 생성
def render_prefix():
    global areas
    for r in range(1, N+1):
        for c in range(1, N+1):
            areas[r][c] = board[r][c] + areas[r-1][c] + areas[r][c-1] - areas[r-1][c-1]


# 입력
N, M = map(int, sys.stdin.readline().split())
# 좌표 계산을 쉽게 하기 위해 0으로 채운 행과 열 추가함
board = [[0] * (N+1)]
for _ in range(N):
    board.append([0] + list(map(int, sys.stdin.readline().split())))
targets = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 누적합 배열 생성
areas = [[0] * (N+1) for _ in range(N+1)]
render_prefix()

# 각 좌표에 대해 계산 후 출력
for target in targets:
    print(get_area(target))
