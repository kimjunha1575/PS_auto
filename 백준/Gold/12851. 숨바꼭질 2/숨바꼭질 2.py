from collections import deque


N, K = map(int, input().split())
que = deque()
que.append((N, 0))
visited = dict()
visited[N] = 0
ans = []
fastest_time = 100_001
move_cnt = 0
while que:
    cur_position, cur_time = que.popleft()
    if cur_time > fastest_time: break
    if cur_position == K:
        ans.append(cur_time)
        fastest_time = cur_time
    targets = [cur_position - 1, cur_position + 1, cur_position * 2]
    for target in targets:
        if target < 0: continue
        if target > min(100000, max(N, K) * 2): continue
        if visited.get(target) is not None and cur_time + 1 > visited[target]: continue
        if visited.get(target) is None:
            visited[target] = cur_time+1
        que.append((target, cur_time + 1))
print(fastest_time)
print(ans.count(fastest_time))
