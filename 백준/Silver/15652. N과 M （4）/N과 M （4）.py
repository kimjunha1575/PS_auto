def solve(idx, cnt):
    # M개를 모두 선택했다면 출력 후 재귀 종료
    if cnt == M:
        print(*buf, sep=' ')
        return
    # idx부터 N까지 자연수에 대해 중복을 허용하여 선택
    for i in range(idx, N + 1):
        # i를 선택 후
        buf.append(i)
        # 재귀 호출
        solve(i, cnt + 1)
        # buf 배열 복구
        buf.pop()


N, M = map(int, input().split())
buf = []
solve(1, 0)
