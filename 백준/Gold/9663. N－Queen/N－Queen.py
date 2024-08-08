def solve(row):
    # 모든 선택이 완료되면 1 반환으로 재귀 종료
    if row == N:
        return 1
    # 해당 row에서 얻을 수 있는 모든 경우의 수를 저장할 변수
    res = 0
    for col in range(N):
        # 놓을 수 없는 칸이라면 무시
        if used_col[col]: continue
        if used_lu[row - col + N - 1]: continue
        if used_ru[row + col]: continue
        
        # 방문 표시
        used_col[col] = 1
        used_lu[row - col + N - 1] = 1
        used_ru[row + col] = 1
        # 재귀 호출
        res += solve(row + 1)
        # 다음 재귀 호출을 위해 복구
        used_col[col] = 0
        used_lu[row - col + N - 1] = 0
        used_ru[row + col] = 0
    return res


N = int(input())
# 퀸 기물은 8방향으로 이동하므로 가로 세로 대각선 모든 방향에 대해
# 단 하나의 퀸만 놓을 수 있다
# 따라서 row 마다 재귀를 수행하면서
# 각 열과 두 방향의 대각선에 대해 방문 처리를 하면서 진행한다.
used_col = [0] * N
used_lu = [0] * (2*N)
used_ru = [0] * (2*N)
print(solve(0))
