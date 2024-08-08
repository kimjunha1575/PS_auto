'''
1. 입력으로 그래프 구성
2. 임의의 노드에 대해 dfs 완전탐색
3. 재귀 깊이가 5 이상인 경우가 존재한다면 1
4. 존재하지 않는다면 0
'''


def dfs(idx, depth):
    # depth가 5에 도달할 수 있다면 문제 조건을 완수하므로 1 반환
    if depth == 5:
        return 1
    res = 0
    for nv in graph[idx]:
        if visited[nv]: continue
        visited[nv] = 1
        res += dfs(nv, depth + 1)
        visited[nv] = 0
    return res


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)
ans = 0
for i in range(N):
    # 모든 노드를 출발지로 잡고 각각 순회
    visited[i] = 1
    if dfs(i, 1):
        # 가능한 경우가 발견된다면 즉시 종료
        ans = 1
        break
    visited[i] = 0
print(ans)
