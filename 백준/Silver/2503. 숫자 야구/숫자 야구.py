def is_possible(arr):
    for query in queries:
        num = list(map(int, str(query[0])))
        strike = query[1]
        ball = query[2]
        for digit in range(3):
            if num[digit] == arr[digit]:
                strike -= 1
            elif num[digit] in arr:
                ball -= 1
        if strike or ball:
            return False
    return True


def solve(idx):
    if idx == 3:
        if is_possible(buf):
            global ans
            ans += 1
        return
    for i in range(1, 10):
        if used[i]: continue
        buf.append(i)
        used[i] = 1
        solve(idx + 1)
        used[i] = 0
        buf.pop()


N = int(input())
queries = [tuple(map(int, input().split())) for _ in range(N)]
buf = []
used = [0] * 10
ans = 0
solve(0)
print(ans)
