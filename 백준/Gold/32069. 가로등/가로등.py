from collections import deque
L, N, K = map(int, input().split())
arr = list(map(int, input().split()))
que = deque()
visited = set()
for pos in arr:
    que.append((pos, 0))
    visited.add(pos)
cnt = 0
while que:
    cnt += 1
    if cnt > K:
        break
    cur = que.popleft()
    cur_pos = cur[0]
    cur_brightness = cur[1]
    print(cur_brightness)
    if 0 <= cur_pos - 1 <= L and (cur_pos-1) not in visited:
        que.append((cur_pos - 1, cur_brightness + 1))
        visited.add(cur_pos - 1)
    if 0 <= cur_pos + 1 <= L and (cur_pos+1) not in visited:
        que.append((cur_pos + 1, cur_brightness + 1))
        visited.add(cur_pos + 1)
