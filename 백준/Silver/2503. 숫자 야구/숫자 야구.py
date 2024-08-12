def is_possible(arr):
    for query in queries:
        num = list(map(int, str(query[0])))
        strike = query[1]
        ball = query[2]
        strike_cnt = 0
        ball_cnt = 0
        for digit in range(3):
            if num[digit] == arr[digit]:
                strike_cnt += 1
            elif num[digit] in arr:
                ball_cnt += 1
        if strike != strike_cnt or ball != ball_cnt:
            return False
    return True


def choose_digit(idx):
    if idx == 3:
        if is_possible(buf):
            global ans
            ans += 1
        return
    for i in range(1, 10):
        if used[i]: continue
        buf.append(i)
        used[i] = 1
        choose_digit(idx + 1)
        used[i] = 0
        buf.pop()


N = int(input())
ans = 0
buf = []
used = [0] * 10
queries = [tuple(map(int, input().split())) for _ in range(N)]
choose_digit(0)
print(ans)
