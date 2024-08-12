import heapq
import sys


N = int(sys.stdin.readline())
pq = []
for _ in range(N):
    ipt = int(sys.stdin.readline())
    if ipt:
        heapq.heappush(pq, ipt)
    elif pq:
        print(heapq.heappop(pq))
    else:
        print(0)
