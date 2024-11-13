'''
**상어**
 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.
번호가 작을수록 강한 상어다
 M개의 칸에 상어가 한 마리씩 들어 있다
맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

냄새를 뿌리고 나서 이동하기 때문에
인접한 칸 중 자신의 냄새가 있는 칸이 없는 경우는 없다

상어의 이동방향 간 우선순위는 상어마다 다르고, 입력으로 주어진다

'''


class Shark:
    def __init__(self, row, col, idx, direction, priority):
        self.row = row
        self.col = col
        self.idx = idx
        self.direction = direction
        self.priority = priority

    def __lt__(self, other):
        return self.idx < other.idx

    def __repr__(self):
        return f"({self.idx + 1} {self.direction})"


# def fight():
#     for r in range(size):
#         for c in range(size):
#             if len(board[r][c]) > 1:
#                 board[r][c].sort()
#                 board[r][c] = board[r][c][:1]


def is_only_one():
    for r in range(size):
        for c in range(size):
            if board[r][c] is None: continue
            if board[r][c].idx:
                return False
    return True


def move_shark():
    new_board = [[None] * size for _ in range(size)]
    for shark in sharks:
        if shark_survivals[shark.idx] == 0: continue
        cur_row = shark.row
        cur_col = shark.col
        cur_direction = shark.direction
        cur_priority = shark.priority[cur_direction]
        nxt_row = -1
        nxt_col = -1
        candidates = []
        for direction in cur_priority:
            nr = cur_row + DIRECTIONS[direction][0]
            nc = cur_col + DIRECTIONS[direction][1]
            if not (0 <= nr < size and 0 <= nc < size): continue
            if smell[nr][nc][0] == -1:
                nxt_row = nr
                nxt_col = nc
                shark.row = nxt_row
                shark.col = nxt_col
                shark.direction = direction
                break
            elif smell[nr][nc][0] == shark.idx:
                candidates.append((nr, nc, direction))
        if nxt_row == -1:
            if candidates:
                nxt_row = candidates[0][0]
                nxt_col = candidates[0][1]
                shark.row = nxt_row
                shark.col = nxt_col
                shark.direction = candidates[0][2]
            else:
                continue

        # smell[nxt_row][nxt_col] = [shark.idx, smell_last]
        if new_board[nxt_row][nxt_col] is None:
            new_board[nxt_row][nxt_col] = shark
        elif new_board[nxt_row][nxt_col].idx > shark.idx:
            shark_survivals[new_board[nxt_row][nxt_col].idx] = 0
            new_board[nxt_row][nxt_col] = shark
        else:
            shark_survivals[shark.idx] = 0

    return new_board


def erase_smell():
    for r in range(size):
        for c in range(size):
            if smell[r][c][0] != -1:
                smell[r][c][1] -= 1
                if smell[r][c][1] == 0:
                    smell[r][c] = [-1, -1]

def make_smell():
    for r in range(size):
        for c in range(size):
            if board[r][c] is None: continue
            smell[r][c] = [board[r][c].idx, smell_last]




DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
DIRECTION_MAP = (None, 3, 1, 2, 0)
size, shark_cnt, smell_last = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(size)]
smell = [[[-1, -1] for _ in range(size)] for _ in range(size)]
shark_directions = [DIRECTION_MAP[direction] for direction in map(int, input().split())]
sharks = []
shark_survivals = [1] * shark_cnt

for shark_idx in range(shark_cnt):
    tmp = []
    for _ in range(4):
        tmp.append([DIRECTION_MAP[direction] for direction in map(int, input().split())])
    tmp[0], tmp[1], tmp[2], tmp[3] = tmp[3], tmp[1], tmp[2], tmp[0]
    sharks.append(Shark(-1, -1, shark_idx, shark_directions[shark_idx], tmp))

for r in range(size):
    for c in range(size):
        if board[r][c] == 0:
            board[r][c] = None
        else:
            sharks[board[r][c] - 1].row = r
            sharks[board[r][c] - 1].col = c
            board[r][c] = sharks[board[r][c]-1]

make_smell()

second = 0
while True:
    second += 1
    board = move_shark()
    erase_smell()
    make_smell()
    # print(second)
    # for row in board:
    #     print(row)
    success = is_only_one()
    if second == 1000 or success:
        break

if success:
    print(second)
else:
    print(-1)
