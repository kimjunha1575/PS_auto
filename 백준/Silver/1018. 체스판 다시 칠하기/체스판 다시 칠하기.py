N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = 64
for r in range(N-7):
    for c in range(M-7):
        cnt_white = 0
        cnt_black = 0
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    if board[r+i][c+j] == 'W':
                        cnt_black += 1
                    else:
                        cnt_white += 1
                else:
                    if board[r+i][c+j] == 'B':
                        cnt_black += 1
                    else:
                        cnt_white += 1
        ans = min(ans, cnt_white, cnt_black)
print(ans)
