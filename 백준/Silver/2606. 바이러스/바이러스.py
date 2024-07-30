
V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
for edge in range(E):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)
stk = [1]
visited = [0] * (V+1)
visited[1] = 1
ans = 0
while stk:
    cur = stk.pop()
    if cur != 1:
        ans += 1
    for vertex in graph[cur]:
        if visited[vertex]: continue
        visited[vertex] = 1
        stk.append(vertex)
print(ans)
