def dfs(idx, prev, preprev, ans_cnt):
    if ans_cnt < idx - 5:
        return 0
    if idx == 10:
        if ans_cnt >= 5:
            return 1
        return 0
    res = 0
    for i in range(1, 6):
        if i == prev == preprev: continue
        buf.append(i)
        if i == answers[idx]:
            ans_cnt += 1
        res += dfs(idx+1, i, prev, ans_cnt)
        buf.pop()
        if i == answers[idx]:
            ans_cnt -= 1
    return res


def count_correct():
    cnt = 0
    for i in range(len(buf)):
        if buf[i] == answers[i]:
            cnt += 1
    return cnt


answers = list(map(int, input().split()))
buf = []
print(dfs(0, 0, 0, 0))
