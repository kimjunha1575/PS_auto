def done(game_board):
    '''
    현재 게임판 상황에서 움직일 수 있는 핀이 있는 지 확인
    :param game_board: 현재 게임 판
    :return: True or False
    '''
    res = True
    for row in range(len(game_board)):
        for col in range(len(game_board[0])):
            if game_board[row][col] == 'o' and is_movable(game_board, row, col):
                res = False
    return res


def is_movable(game_board, row, col):
    '''
    현재 게임 판 내에 (row, col)에 있는 핀이 움직일 수 있는 핀인지 검사
    :param game_board: 게임 판 정보를 담은 2차원 배열
    :param row: 핀이 위치한 행
    :param col: 핀이 위치한 열
    :return:
    '''
    for dr, dc in directions:
        nr = row + dr
        nc = col + dc
        nnr = nr + dr
        nnc = nc + dc
        if not (0 <= nnr < height and 0 <= nnc < width): continue
        if not (board[nr][nc] == 'o' and board[nnr][nnc] == '.'): continue
        return True
    return False


def count_pins(game_board):
    '''
    현재 게임 판에서 핀의 위치를 찾아 핀 위치 배열 갱신
    :param game_board: 게임 판 2차 배열
    :return: 현재 게임판에 남아있는 핀의 개수
    '''
    cnt = 0
    for row in range(len(game_board)):
        for col in range(len(game_board[0])):
            if board[row][col] == 'o':
                cnt += 1
    return cnt


def solve(game_board, cnt):
    global ans
    global move_cnt
    # 현재 맵의 복사본으로 사용 (원본 훼손 방지)
    cur_board = game_board.copy()
    cur_pin_cnt = count_pins(cur_board)
    if done(cur_board):
        if cur_pin_cnt < ans:
            ans = cur_pin_cnt
            move_cnt = cnt
            return
        if cur_pin_cnt == ans:
            move_cnt = min(move_cnt, cnt)
        ans = min(ans, cur_pin_cnt)
        return
    # 현재 맵에서 핀의 좌표 목록 찾기
    pins = []
    for row in range(len(game_board)):
        for col in range(len(game_board[0])):
            if board[row][col] == 'o':
                pins.append((row, col))
    for pr, pc in pins:
        for dr, dc in directions:
            nr = pr + dr
            nc = pc + dc
            nnr = nr + dr
            nnc = nc + dc
            if not (0 <= nnr < height and 0 <= nnc < width): continue
            if board[nr][nc] != 'o' or board[nnr][nnc] != '.': continue
            cur_board[nr][nc] = '.'
            cur_board[nnr][nnc] = 'o'
            cur_board[pr][pc] = '.'
            solve(cur_board, cnt + 1)
            cur_board[nr][nc] = 'o'
            cur_board[nnr][nnc] = '.'
            cur_board[pr][pc] = 'o'


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
height = 5
width = 9
T = int(input())
for case in range(1, T+1):
    if case > 1:
        input()
    board = [list(input()) for _ in range(5)]
    ans = 8
    move_cnt = 8
    solve(board, 0)
    print(ans, move_cnt)
