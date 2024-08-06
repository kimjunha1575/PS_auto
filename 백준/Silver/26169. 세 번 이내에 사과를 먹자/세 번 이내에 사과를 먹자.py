def solve(game_board, cnt, apple, row, col):
    '''
    인자로 받은 상태의 맵에서 문제의 조건을 만족할 수 있는 경우의 수가
    발견되면 1 반환
    발견하지 못하면 0 반환
    :param game_board: 현재 map의 상태 (각 단계에서의 상태)
    :param cnt: 현재까지의 누적 이동 회수
    :param apple: 현재까지 먹은 사과의 수
    :param row: 현재 학생 위치의 행
    :param col: 현재 학생 위치의 열
    :return: 문제 조건을 만족할 수 있는 지에 따라 0 혹은 1 반환
    '''
    # 원본 맵 유지
    cur_map = game_board.copy()
    # 2개의 사과를 먹었다면 1 반환
    if apple == 2:
        return 1
    # 2개의 사과를 먹지 못했지만 이동 회수가 3이라면 재귀 종료
    if cnt == 3:
        return 0
    # 네 방향에 대해
    for dr, dc in directions:
        nr = row + dr
        nc = col + dc
        # 이동 불가능한 곳은 무시하고
        if not (0 <= nr < 5 and 0 <= nc < 5): continue
        if cur_map[nr][nc] == -1: continue
        # 이전에 있던 위치는 이동 불가 처리
        cur_map[row][col] = -1
        # 이동한 상태로 재귀 호출
        if solve(cur_map, cnt + 1, apple + cur_map[nr][nc], nr, nc):
            # 이후 단계에서 사과를 2개 이상 먹을 수 있는 방법이 발견되면 즉시 1 반환
            return 1
        # 재귀 호출 이후 원 상태 복구
        cur_map[row][col] = 0
    # 사과를 2개 이상 먹을 수 있는 방법을 발견하지 못하면 0 반환
    return 0


board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
print(solve(board, 0, 0, r, c))
