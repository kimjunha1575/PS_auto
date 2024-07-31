from collections import deque


def bfs():
    # 초기화
    que = deque()
    que.append(start_point)
    visited = [[0] * board_size for _ in range(board_size)]
    visited[start_point[0]][start_point[1]] = 1
    while que:
        cur = que.popleft()
        cur_row = cur[0]
        cur_col = cur[1]
        # 목적지에 도착하면 이동한 회수 반환
        if cur_row == destination[0] and cur_col == destination[1]:
            return visited[cur_row][cur_col] -1
        # 이동 가능한 모든 방향에 대해 순회
        for dr, dc in moves:
            next_row = cur_row + dr
            next_col = cur_col + dc
            # 체스판 밖이거나 이미 방문한 곳은 무시
            if not (0 <= next_row < board_size and 0 <= next_col < board_size): continue
            if visited[next_row][next_col]: continue
            que.append((next_row, next_col))
            # 방문 표시와 동시에 이동한 회수 저장
            visited[next_row][next_col] = visited[cur_row][cur_col] + 1
    # 목적지에 도달할 수 없다면 -1 반환(문제에서는 언급 없긴 함)
    return -1


moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
T = int(input())
for case in range(1, T+1):
    board_size = int(input())
    start_point = tuple(map(int, input().split()))
    destination = tuple(map(int, input().split()))
    print(bfs())
