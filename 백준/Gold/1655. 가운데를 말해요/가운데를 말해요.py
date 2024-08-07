import heapq


N = int(input())
numbers = [int(input()) for _ in range(N)]
min_que = []
max_que = []
heapq.heappush(min_que, numbers[0])
print(min_que[0])
for i in range(1, N):
    ipt = numbers[i]
    if ipt >= min_que[0]:
        heapq.heappush(min_que, ipt)
    else:
        heapq.heappush(max_que, -ipt)
    if len(max_que) < len(min_que):
        heapq.heappush(max_que, -heapq.heappop(min_que))
    elif len(min_que) + 1 < len(max_que):
        heapq.heappush(min_que, -heapq.heappop(max_que))
    print(-max_que[0])
