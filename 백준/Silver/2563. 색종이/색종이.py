
board = [[0] * 100 for _ in range(100)]
paper_num = int(input())
ans = 0
for i in range(paper_num):
    col, row = map(int, input().split())
    for y in range(row, row + 10):
        for x in range(col, col + 10):
            if board[y][x] == 0:
                board[y][x] = 1
                ans += 1
print(ans)
