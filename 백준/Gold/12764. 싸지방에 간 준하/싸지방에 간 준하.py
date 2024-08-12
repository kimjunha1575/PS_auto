import heapq


N = int(input())
usages = [tuple(map(int, input().split())) for _ in range(N)]
usages.sort()
ans = 0
pc_users = [0] * (N+1)
cur_using = []
ready_for_use = [x for x in range(1, 100001)]
for use in usages:
    cur_time = use[0]
    while cur_using and cur_using[0][0] <= cur_time:
        heapq.heappush(ready_for_use, heapq.heappop(cur_using)[1])
    target_pc = heapq.heappop(ready_for_use)
    pc_users[target_pc] += 1
    ans = max(ans, target_pc)
    heapq.heappush(cur_using, (use[1], target_pc))

print(ans)
for pc in range(1, ans + 1):
    print(pc_users[pc], end=' ')


'''
'현재 비어 있는 컴퓨터'를 상수 시간에 알아낼 수 있어야 할 듯 함(최소 log(n))
'컴퓨터'를 pq에 넣어두면 현재 사용 가능한 가장 낮은 번호의 컴퓨터를 log(n)에 알아낼 수 있음
'현재 사용 가능한 컴퓨터' pq
'현재 사용 중인 컴퓨터' pq



'''