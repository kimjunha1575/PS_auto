from collections import deque


def dfs(cur):
    print(cur, end=' ')
    for vertex in tree[cur]:
        if visited[vertex]: continue
        visited[vertex] = 1
        dfs(vertex)


def bfs():
    que = deque()
    que.append(start)
    visited = [0] * (V+1)
    visited[start] = 1
    while que:
        cur = que.popleft()
        print(cur, end=' ')
        for vertex in tree[cur]:
            if visited[vertex]: continue
            visited[vertex] = 1
            que.append(vertex)


V, E, start = map(int, input().split())
tree = [[] for _ in range(V+1)]
for _ in range(E):
    st, en = map(int, input().split())
    tree[st].append(en)
    tree[en].append(st)
for arr in tree:
    arr.sort()
visited = [0] * (V+1)
visited[start] = 1
dfs(start)
print()
bfs()
