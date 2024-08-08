def dfs(idx, depth):
    if depth == 5:
        return 1
    res = 0
    for nv in graph[idx]:
        if visited[nv]: continue
        visited[nv] = 1
        res += dfs(nv, depth + 1)
        visited[nv] = 0
    return res


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)
ans = 0
for i in range(N):
    visited[i] = 1
    if dfs(i, 1):
        ans = 1
        break
    visited[i] = 0
print(ans)
