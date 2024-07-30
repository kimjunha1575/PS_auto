from collections import deque


L, N, K = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (L+1)
que = deque()
for pos in arr:
    visited[pos] = 1
    que.append(pos)
cnt = 0
while que:
    cnt += 1
    if cnt >= K:
        break
    cur = que.popleft()
    brightness = visited[cur]
    if L >= cur - 1 >= 0 == visited[cur - 1]:
        que.append(cur - 1)
        visited[cur - 1] = brightness + 1
    if L >= cur + 1 >= 0 == visited[cur + 1]:
        que.append(cur + 1)
        visited[cur + 1] = brightness + 1
visited.sort(key=lambda x: x or L+1)
for i in range(K):
    print(visited[i]-1)
