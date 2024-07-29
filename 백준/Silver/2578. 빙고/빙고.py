def check_board(i, j):
    global board
    global bingo
    # 빙고가 이미 완성된 칸은 더이상 불리지 않으므로
    # 새롭게 불린 숫자의 칸의 행, 열, 대각선만 검사 후 누적
    
    # 해당 칸의 열 검사
    for col in range(5):
        if board[i][col] > 0:
            break
        if col == 4:
            bingo += 1
    # 해당 칸의 행 검사
    for row in range(5):
        if board[row][j] > 0:
            break
        if row == 4:
            bingo += 1
    # 해당 칸이 대각선 빙고가 가능하다면 해당 대각선 검사
    if i == j:
        for rc in range(5):
            if board[rc][rc] > 0:
                break
            if rc == 4:
                bingo += 1
    if i + j == 4:
        for rc in range(5):
            if board[rc][4-rc] > 0:
                break
            if rc == 4:
                bingo += 1

    # 누적된 빙고가 3개 이상이라면 게임 끝
    if bingo >= 3:
        return True
    return False


def delete_number(num):
    global board
    for i in range(5):
        for j in range(5):
            # 불린 숫자는 -1로 표기
            if board[i][j] == num:
                board[i][j] = -1
                return i, j


board = []
nums = []
bingo = 0
for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(5):
    nums += list(map(int, input().split()))
cnt = 0
for num in nums:
    # 부른 숫자 카운트
    cnt += 1
    # 불린 숫자를 칠하고
    i, j = delete_number(num)
    # 빙고가 3개 이상이 되었다면 게임 끝
    if check_board(i, j):
        break
print(cnt)
