from collections import deque 

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
invited = [0] * (n + 1)
for _ in range(m):
    frm, to = map(int, input().split())
    graph[frm].append(to)
    graph[to].append(frm)
ans = 0
que = deque()
que.append((1, 0))
invited[1] = 1
while que:
    cur, depth = que.popleft()
    for nxt in graph[cur]:
        if invited[nxt]: continue
        if depth + 1 > 2: continue
        invited[nxt] = 1
        que.append((nxt, depth + 1))
        ans += 1
        
print(ans) 
