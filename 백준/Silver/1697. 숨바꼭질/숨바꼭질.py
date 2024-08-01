from collections import deque


def bfs():
    que = deque()
    que.append((N, 0))
    visited = set()
    visited.add(N)
    while que:
        cur, cnt = que.popleft()
        if cur == K:
            return cnt
        if cur > 100_000 or cur < 0: continue
        for nxt in [cur-1, cur+1, cur*2]:
            if nxt not in visited:
                que.append((nxt, cnt + 1))
                visited.add(nxt)
    return -1


N, K = map(int, input().split())
print(bfs())
