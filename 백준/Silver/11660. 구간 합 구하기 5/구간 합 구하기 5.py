def get_area(position):
    # 좌표 정보 -> 넓이
    y1, x1, y2, x2 = position
    return areas[y2][x2] - areas[y1-1][x2] - areas[y2][x1-1] + areas[y1-1][x1-1]


def render_areas():
    # 부분합 2차배열 생성
    global areas
    acc = board[0][0]
    for r in range(N+1):
        if r > 0:
            acc += board[r][0]
        tmp = acc
        for c in range(N+1):
            if c > 0:
                tmp += sum(board_t[c][:r+1])
            areas[r][c] = tmp


# 입력
N, M = map(int, input().split())
board = [[0] * (N+1)] # 좌표 계산을 쉽게 하기 위해 0으로 채운 행과 열 추가함
for _ in range(N):
    board.append([0] + list(map(int, input().split())))
board_t = list(zip(*board))
targets = [list(map(int, input().split())) for i in range(M)]
areas = [[0] * (N+1) for _ in range(N+1)] # 부분합을 저장할 행렬
render_areas()

for target in targets:
    # 각 좌표정보에 대해 계산 후 출력
    print(get_area(target))
