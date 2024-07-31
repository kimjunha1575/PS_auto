def find_tank():
    # 전차의 초기 위치와 방향을 찾아서 반환
    for r in range(height):
        for c in range(width):
            if board[r][c] in tanks:
                return r, c, tanks.find(board[r][c])


def execute_command():
    global board
    global cur_tank_dir
    global cur_tank_row
    global cur_tank_col
    # 방향변경, 이동
    if command in direction_commands:
        # 명령받은 방향으로 전차 회전
        cur_tank_dir = direction_commands.find(command)
        board[cur_tank_row][cur_tank_col] = tanks[cur_tank_dir]
        # 회전한 방향으로 이동 가능하다면 한 칸 이동
        nr = cur_tank_row + directions[cur_tank_dir][0]
        nc = cur_tank_col + directions[cur_tank_dir][1]
        if 0 <= nr < height and 0 <= nc < width and board[nr][nc] == '.':
            board[nr][nc] = tanks[cur_tank_dir]
            board[cur_tank_row][cur_tank_col] = '.'
            # 현재 위치 갱신
            cur_tank_row = nr
            cur_tank_col = nc
    # 포탄 발사
    else:
        nr = cur_tank_row + directions[cur_tank_dir][0]
        nc = cur_tank_col + directions[cur_tank_dir][1]
        # 벽을 만나거나 지도 밖으로 나갈 때 까지 전진
        while 0 <= nr < height and 0 <= nc < width and board[nr][nc] not in walls:
            nr += directions[cur_tank_dir][0]
            nc += directions[cur_tank_dir][1]
        # 지도를 나가기 전 벽과 만났고, 벽돌 벽이라면 벽 부수기
        if 0 <= nr < height and 0 <= nc < width and board[nr][nc] == '*':
            board[nr][nc] = '.'
    return None


walls = "#*"
direction_commands = "UDLR"
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
tanks = "^v<>"

T = int(input())
for case in range(1, T+1):
    # 입력
    height, width = map(int, input().split())
    board = [list(input()) for _ in range(height)]
    command_num = int(input())
    commands = input()
    # 전차 초기 상태 저장
    cur_tank_row, cur_tank_col, cur_tank_dir = find_tank()
    # 모든 명령 하나씩 수행
    for command in commands:
        execute_command()
    # 결과 출력
    print(f"#{case}", end=' ')
    for row in range(height):
        print(*board[row], sep='')
