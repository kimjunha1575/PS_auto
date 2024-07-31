from collections import deque


def bfs():
    que = deque()
    que.append(start)
    visited = [0] * (V+1)
    visited[start] = 1
    while que:
        cur = que.popleft()
        if cur == end:
            return visited[cur] - 1
        for family_member in tree[cur]:
            if visited[family_member]: continue
            visited[family_member] = visited[cur] + 1
            que.append(family_member)
    return -1


V = int(input())
start, end = map(int, input().split())
E = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(E):
    child, parent = map(int, input().split())
    tree[parent].append(child)
    tree[child].append(parent)
print(bfs())
    