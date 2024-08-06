from collections import deque


def bfs(r, c):
    # 초기값 구성
    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    res = 0
    while que:
        cr, cc = que.popleft()
        # 현재 행 번호에 따라 방향 배열 선택
        if cr % 2 == 1:
            dirs = directions_odd
        else:
            dirs = directions_even
        # 인접한 6개 칸에 대해 조사
        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc
            # 범위를 벗어나면 무시
            if not (0 <= nr < H + 2 and 0 <= nc < W + 2): continue
            # 이미 순회한 곳이면 무시
            if visited[nr][nc]: continue
            # 건물을 만나면 res에 1을 더하고 다음 인접한 칸으로 이동 (건물 내부로는 들어가지 않는다)
            if board[nr][nc] == 1:
                res += 1
                continue
            que.append((nr, nc))
            visited[nr][nc] = 1
    # 누적된 건물 외벽 개수를 반환
    return res


# 지도 구성 상, 행 번호에 따라 인접한 좌표들의 구성이 다르기 때문에 방향 배열을 2개 구성
directions_odd = [(-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (-1, 0)]
directions_even = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
W, H = map(int, input().split())

# 바깥에서만 접근하기 위해 배열의 상하좌우에 0으로 채운 행과 열을 각각 추가함
board = [[0] * (W + 2)]
for _ in range(H):
    board.append([0] + list(map(int, input().split())) + [0])
board.append([0] * (W+2))
visited = [[0] * (W + 2) for _ in range(H + 2)]
# 상하좌우에 0을 채웠기 때문에 (0, 0)은 반드시 '바깥'
# '바깥'에서부터 순회를 시작하여 건물의 외벽을 만날 때 마다 카운트 하는 방식으로 순회
print(bfs(0, 0))
