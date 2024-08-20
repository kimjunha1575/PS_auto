
M, N = map(int, input().split())
board = [[1] * M for _ in range(M)]
grow = [0] * (2*M - 1)
for _ in range(N):
    zeros, ones, twos = map(int, input().split())
    idx = zeros
    while ones:
        grow[idx] += 1
        idx += 1
        ones -= 1
    while twos:
        grow[idx] += 2
        idx += 1
        twos -= 1
for i in range(M):
    for j in range(M):
        if j == 0:
            print(grow[(M-1) - i] + 1, end=' ')
        else:
            print(grow[(M-1) + j] + 1, end=' ')
    print()
