from collections import deque


def bfs():
    que = deque()
    que.append((A, 1))
    while que:
        cur = que.popleft()
        value = cur[0]
        cnt = cur[1]
        if value > B:
            continue
        if value == B:
            return cnt
        que.append((value * 2, cnt + 1))
        que.append((10 * value + 1, cnt + 1))
    return -1


A, B = map(int, input().split())
print(bfs())
