import heapq

N, K = map(int, input().split())
jewels = []
bags = []
for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))
for _ in range(K):
    bags.append(int(input()))

jewels.sort()
bags.sort()

res = 0
jewel_idx = 0
pq = []
for cur_bag in bags:
    while jewel_idx < N and jewels[jewel_idx][0] <= cur_bag:
        jewel = jewels[jewel_idx]
        heapq.heappush(pq, (-jewel[1], jewel))
        jewel_idx += 1
    if pq:
        res += heapq.heappop(pq)[1][1]

print(res)
