import heapq


N = int(input())
commands = [int(input()) for _ in range(N)]
pq = []
for command in commands:
    if command:
        heapq.heappush(pq, (abs(command), command))
    elif pq:
        print(heapq.heappop(pq)[1])
    else:
        print(0)

