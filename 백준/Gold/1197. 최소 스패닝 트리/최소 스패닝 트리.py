import heapq


def find(p):
    if p != parent[p]: parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    pp = find(p)
    pq = find(q)
    if pp == pq:
        return
    if rank[pp] <= rank[pq]:
        parent[pp] = pq
        if rank[pp] == rank[pq]:
            rank[pq] += 1
    else:
        parent[pq] = pp


V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
rank = [1] * (V+1)
for _ in range(E):
    frm, to, cost = map(int, input().split())
    heapq.heappush(edges, (cost, frm, to))
ans = 0
while edges:
    cost, frm, to = heapq.heappop(edges)
    if find(frm) == find(to):
        continue
    union(frm, to)
    ans += cost

print(ans)
