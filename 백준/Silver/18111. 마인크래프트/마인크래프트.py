N, M, B = map(int, input().split())
board = []
total = B
ans = 1_000_000_000
final_height = 0
for row in range(N):
    board.append(list(map(int, input().split())))
    total += sum(board[row])
for height in range(total//(N*M) + 1):
    tmp = 0
    for row in range(N):
        for col in range(M):
            diff = board[row][col] - height
            if diff > 0:
                tmp += 2 * diff
            elif diff < 0:
                tmp -= diff
    if tmp <= ans:
        ans = tmp
        final_height = height
print(ans, final_height)
