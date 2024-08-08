from collections import deque


def check_arround(r, c):
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < N and 0 <= nc < N): continue
        if board[nr][nc] == '*':
            return True
    return False


def bfs(r, c):
    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    while que:
        cr, cc = que.popleft()
        if check_arround(cr, cc): continue
        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc]: continue
            if board[nr][nc] != '.': continue
            visited[nr][nc] = 1
            que.append((nr, nc))


directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
T = int(input())
for case in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.' and visited[r][c] == 0:
                cnt += 1
                if check_arround(r, c):
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if not (0 <= nr < N and 0 <= nc < N): continue
                        if visited[nr][nc]: continue
                        if board[nr][nc] != '.': continue
                        if check_arround(nr, nc): continue
                        bfs(nr, nc)
                else:
                    bfs(r, c)
    print(f"#{case} {cnt}")

'''
아직 들르지 않은 빈 칸을 만난다
인접한 칸 검사
주변에 지뢰가 있다
    주변에 다른 빈 칸 중 주변에 지뢰가 없는 칸이\
        존재한다면 거기서 bfs
        존재하지 않는다면 다음 칸으로 이동
주변에 지뢰가 없다
    바로 bfs


'''