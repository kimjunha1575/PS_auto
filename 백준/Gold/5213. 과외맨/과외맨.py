import heapq


class Edge:
    def __init__(self, frm, to, dist, path):
        self.frm = frm
        self.to = to
        self.dist = dist
        self.path = path

    def __lt__(self, other):
        return self.dist < other.dist


N = int(input())
board = [[0] * (N * 2) for _ in range(N)]
idx = 0
pos_to_num = dict()
cur_max = 0
cur_max_path = None
cur_max_dist = 0
for _ in range(N*N - N//2):
    left, right = map(int, input().split())
    row = (idx // (2 * N - 1)) * 2
    col = idx % (2 * N - 1)
    if col >= N:
        row += 1
        col %= N
    idx += 1
    if row % 2 == 0:
        board[row][2*col] = left
        board[row][2*col + 1] = right
        pos_to_num[(row, 2*col)] = idx
        pos_to_num[(row, 2*col + 1)] = idx
    else:
        board[row][2*col + 1] = left
        board[row][2*col + 2] = right
        pos_to_num[(row, 2*col + 1)] = idx
        pos_to_num[(row, 2*col + 2)] = idx

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited_pos = [[0] * 2 * N for _ in range(N)]
visited_tile = [0] * (N * N + 1)
pq = []
heapq.heappush(pq, Edge((0, 0), (0, 0), 1, [1]))
visited_pos[0][0] = 1
visited_tile[1] = 1
found_target = False
while pq:
    cur_edge = heapq.heappop(pq)
    cur = cur_edge.to
    dist = cur_edge.dist
    path = cur_edge.path
    row = cur[0]
    col = cur[1]
    cur_num = pos_to_num[(row, col)]
    if cur_num > cur_max:
        cur_max = cur_num
        cur_max_path = path
        cur_max_dist = dist
    if cur_num == N * N - N // 2:
        found_target = True
        print(dist)
        print(*path, sep=' ')
        break
    for dr, dc in directions:
        nr = row + dr
        nc = col + dc
        # 범위를 벗어나면 무시
        if not (0 <= nr < N and 0 <= nc < 2*N): continue
        # 타일이 아닌 곳은 무시
        if board[nr][nc] == 0: continue
        # 이미 방문한 좌표라면 무시
        if visited_pos[nr][nc]: continue
        nxt_num = pos_to_num[(nr, nc)]
        # 다른 타일인데 이미 방문한 타일이라면 무시
        if nxt_num != cur_num and visited_tile[nxt_num]: continue
        # 다른 타일인데 숫자가 다르다면 무시
        if nxt_num != cur_num and board[nr][nc] != board[row][col]: continue
        if nxt_num == cur_num:
            heapq.heappush(pq, Edge((row, col), (nr, nc), dist, path))
            visited_pos[nr][nc] = 1
        else:
            heapq.heappush(pq, Edge((row, col), (nr, nc), dist + 1, path + [nxt_num]))
            visited_tile[nxt_num] = 1

if not found_target:
    print(cur_max_dist)
    print(*cur_max_path, sep=' ')
