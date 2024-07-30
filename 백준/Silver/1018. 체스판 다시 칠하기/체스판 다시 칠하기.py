white = list("WBWBWBWB")
black = list("BWBWBWBW")
white_first = [white, black] * 4
black_first = [black, white] * 4
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = 64
for r in range(N-7):
    for c in range(M-7):
        cnt_white = 0
        cnt_black = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if board[i][j] != white_first[r-i][c-j]:
                    cnt_white += 1
                if board[i][j] != black_first[r-i][c-j]:
                    cnt_black += 1
        ans = min(ans, cnt_white, cnt_black)
print(ans)
