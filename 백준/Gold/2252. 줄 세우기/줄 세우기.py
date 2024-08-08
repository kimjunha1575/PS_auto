from collections import deque


N, M = map(int, input().split())
graph = [[0, []] for _ in range(N+1)]
que = deque()
for _ in range(M):
    smaller, taller = map(int, input().split())
    graph[smaller][1].append(taller)
    graph[taller][0] += 1
for student in range(1, N+1):
    if graph[student][0] == 0:
        que.append(student)
while que:
    cur = que.popleft()
    print(cur, end=' ')
    for nxt in graph[cur][1]:
        graph[nxt][0] -= 1
        if graph[nxt][0] == 0:
            que.append(nxt)

