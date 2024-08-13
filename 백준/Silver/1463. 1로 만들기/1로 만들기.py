from collections import deque


N = int(input())
que = deque()
visited = [0] * (N + 1)
que.append((1, 1))
visited[1] = 1
ans = 0
while que:
    value, steps = que.popleft()
    if value == N:
        ans = steps - 1
        break
    targets = [value + 1, value * 2, value * 3]
    for target in targets:
        if target > N: continue
        if visited[target]: continue
        que.append((target, steps + 1))
        visited[target] = 1


print(ans)
