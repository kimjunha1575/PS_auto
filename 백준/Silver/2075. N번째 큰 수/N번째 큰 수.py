import heapq


N = int(input())
pq = []
for _ in range(N):
    ipt = list(map(int, input().split()))
    for e in ipt:
        heapq.heappush(pq, e)
    while len(pq) > N:
        heapq.heappop(pq)

print(heapq.heappop(pq))
