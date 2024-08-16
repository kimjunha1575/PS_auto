from collections import deque
import heapq


def dijkstra():
    que = [(0, 0, 0)]
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    while que:
        # 항상 최소경로로 움직이기 위해 queue가 아닌 priority queue 사용
        # cost가 낮은 순서로 정렬하기 위해 cost를 튜플의 첫 번째 원소로 둠
        cost, r, c = heapq.heappop(que)

        # 도착지에 다다르면 즉시 종료해도 됨
        if (r, c) == (N-1, N-1):
            return cost

        # 나머지는 queue와 pq의 차이를 제외하면 동일
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            ncost = cost + board[nr][nc]
            if dist[nr][nc] <= ncost: continue
            dist[nr][nc] = ncost
            # priority queue
            heapq.heappush(que, (ncost, nr, nc))
    return dist[N-1][N-1]


def bfs():
    que = deque()
    # 경로의 누적 cost를 저장할 매트릭스
    board_acc = [[INF] * N for _ in range(N)]

    # 일반 queue 사용
    que.append((0, 0, 0))
    while que:
        r, c, cost = que.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            ncost = cost + board[nr][nc]

            # 최소 경로를 갱신 가능할 때만 이동
            if board_acc[nr][nc] <= ncost: continue
            board_acc[nr][nc] = ncost
            que.append((nr, nc, ncost))
    return board_acc[N-1][N-1]


INF = 1_000_000_000
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    # print(f"#{case} {bfs()}")
    print(f"#{case} {dijkstra()}")
