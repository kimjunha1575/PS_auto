board = [[0 for _ in range(100)] for _ in range(100)]
N, M = map(int, input().split())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(1, 101):
        for x in range(1, 101):
            if y1 <= y <= y2 and x1 <= x <= x2:
                board[y-1][x-1] += 1

res = 0
for y in range(100):
    for x in range(100):
        if board[y][x] > M:
            res += 1

print(res)