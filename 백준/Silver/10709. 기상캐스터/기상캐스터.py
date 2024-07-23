
H, W = map(int, input().split())
board = [[None for _ in range(W)] for _ in range(H)]
for row in range(H):
    board[row] = list(input())

ans = board.copy()
for r in range(H):
    cur_cnt = 0
    for c in range(W):
        if board[r][c] == 'c':
            ans[r][c] = 0
            cur_cnt = 1
        elif board[r][c] == '.' and cur_cnt:
            ans[r][c] = cur_cnt
            cur_cnt += 1
        elif board[r][c] == '.' and not cur_cnt:
            ans[r][c] = -1

for r in range(H):
    for c in range(W):
        print(ans[r][c], end=' ')
    print()
