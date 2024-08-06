def solve():
    if len(buf) == M:
        # 고른 숫자의 개수가 M개이면 출력
        print(*buf, sep=' ')
        return
    for i in range(1, N + 1):
        if used[i]: continue
        used[i] = 1
        buf.append(i)
        solve()
        buf.pop()
        used[i] = 0


N, M = map(int, input().split())
# 수열을 저장하기 위한 배열
buf = []
# 중복 체크
used = [0] * (N+1)
solve()
