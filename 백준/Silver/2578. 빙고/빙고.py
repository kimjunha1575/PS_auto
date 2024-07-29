def check_board(i, j):
    global board
    global bingo
    for col in range(5):
        if board[i][col] > 0:
            break
        if col == 4:
            bingo += 1
    for row in range(5):
        if board[row][j] > 0:
            break
        if row == 4:
            bingo += 1
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
    if bingo >= 3:
        return True
    return False


def delete_number(num):
    global board
    for i in range(5):
        for j in range(5):
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
    cnt += 1
    i, j = delete_number(num)
    done = check_board(i, j)
    if done:
        break
print(cnt)
