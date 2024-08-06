def solve(row):
    if row == N:
        return 1
    res = 0
    for col in range(N):
        if used_col[col]: continue
        if used_lu[row - col + N - 1]: continue
        if used_ru[row + col]: continue
        used_col[col] = 1
        used_lu[row - col + N - 1] = 1
        used_ru[row + col] = 1
        res += solve(row + 1)
        used_col[col] = 0
        used_lu[row - col + N - 1] = 0
        used_ru[row + col] = 0
    return res


N = int(input())
used_col = [0] * N
used_lu = [0] * (2*N)
used_ru = [0] * (2*N)
print(solve(0))
