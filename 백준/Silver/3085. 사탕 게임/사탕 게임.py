def cnt_line(row):
    try:
        return dp[''.join(row)]
    except:
        pass
    ans = 1
    prev = row[0]
    tmp = 1
    for i in range(1, len(row)):
        if row[i] == prev:
            tmp += 1
        else:
            prev = row[i]
            tmp = 1
        ans = max(ans, tmp)
    dp[''.join(row)] = ans
    return ans


def find_longest(y, x):
    global board
    longest = 0
    dy = [0, 1]
    dx = [1, 0]
    for di in range(len(dy)):
        ny = y + dy[di]
        nx = x + dx[di]
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if board[ny][nx] == board[y][x]:
            continue
        board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
        tmp = 0
        board_t = list(zip(*board))
        for row in range(N):
            tmp1 = cnt_line(board[row])
            tmp2 = cnt_line(board_t[row])
            tmp = max(tmp, tmp1, tmp2)
        longest = max(longest, tmp)
        board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
    return longest


N = int(input())
board = []
dp = dict()
for i in range(N):
    board.append(list(input()))
ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, find_longest(i, j))
print(ans)
