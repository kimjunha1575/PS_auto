from collections import deque


def bfs():
    visited = dict()
    que = deque()
    que.append(A)
    visited[A] = 0
    while que:
        cur = que.popleft()
        if cur > B:
            continue
        if cur == B:
            return visited[cur] + 1
        tmp = cur * 2
        if visited.get(tmp) is None:
            que.append(tmp)
            visited[tmp] = visited[cur] + 1
        tmp = 10 * cur + 1
        if visited.get(tmp) is None:
            que.append(tmp)
            visited[tmp] = visited[cur] + 1
    return -1


A, B = map(int, input().split())
print(bfs())
