import heapq


def find(p):
    if p != parent[p]: parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    pp = find(p)
    pq = find(q)
    if pp == pq:
        return
    # find 함수의 재귀 깊이를 제한하기 위해 rank 방식 사용
    if rank[pp] <= rank[pq]:
        parent[pp] = pq
        if rank[pp] == rank[pq]:
            rank[pq] += 1
    else:
        parent[pq] = pp


V, E = map(int, input().split())
# 간선들을 저장할 우선순위 큐
edges = []
parent = [i for i in range(V+1)]
# find 함수의 재귀호출 깊이를 log(n)으로 제한하기 위해 rank 사용
rank = [1] * (V+1)
for _ in range(E):
    frm, to, cost = map(int, input().split())
    # 큐를 가중치가 낮은 순으로 정렬하기 위해 cost를 첫 번째 원소로 하는 튜플로 저장
    heapq.heappush(edges, (cost, frm, to))
ans = 0
# MST를 완성할 때 까지
while edges:
    # 가장 가중치가 낮은 간선이
    cost, frm, to = heapq.heappop(edges)
    # 연결되지 않은 두 노드를 연결한다면
    if find(frm) == find(to):
        continue
    # 두 노드를 해당 간선으로 연결하고
    union(frm, to)
    # 가중치 값을 누적한다
    ans += cost

print(ans)
