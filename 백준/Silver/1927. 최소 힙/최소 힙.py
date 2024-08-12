import heapq


N = int(input())
pq = []
commands = []
for _ in range(N):
    commands.append(int(input()))
for command in commands:
    if command:
        heapq.heappush(pq, command)
    elif len(pq):
        print(heapq.heappop(pq))
    else:
        print(0)
