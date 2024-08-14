'''
매직 스타를 이루는 부분들만 따로 리스트에 저장
매직 스타를 이루는 각 인덱스들에 대해 직접 접근해서 유효성 검사
'''


def print_star():
    print(f"....{chr(board_list[0] + 64)}....")
    print(f".{chr(board_list[1] + 64)}.{chr(board_list[2] + 64)}.{chr(board_list[3] + 64)}.{chr(board_list[4] + 64)}.")
    print(f"..{chr(board_list[5] + 64)}...{chr(board_list[6] + 64)}..")
    print(f".{chr(board_list[7] + 64)}.{chr(board_list[8] + 64)}.{chr(board_list[9] + 64)}.{chr(board_list[10] + 64)}.")
    print(f"....{chr(board_list[11] + 64)}....")


def get_sum(one, two, three, four):
    return board_list[one] + board_list[two] + board_list[three] + board_list[four]


def is_occupied(one, two, three, four):
    return board_list[one] and board_list[two] and board_list[three] and board_list[four]


def is_possible():
    tmp = get_sum(1, 2, 3, 4)
    if tmp > 26: return False
    if is_occupied(1, 2, 3, 4) and tmp != 26: return False
    tmp = get_sum(0, 2, 5, 7)
    if tmp > 26: return False
    if is_occupied(0, 2, 5, 7) and tmp != 26: return False
    tmp = get_sum(0, 3, 6, 10)
    if tmp > 26: return False
    if is_occupied(0, 3, 6, 10) and tmp != 26: return False
    tmp = get_sum(7, 8, 9, 10)
    if tmp > 26: return False
    if is_occupied(7, 8, 9, 10) and tmp != 26: return False
    tmp = get_sum(1, 5, 8, 11)
    if tmp > 26: return False
    if is_occupied(1, 5, 8, 11) and tmp != 26: return False
    tmp = get_sum(4, 6, 9, 11)
    if tmp > 26: return False
    if is_occupied(4, 6, 9, 11) and tmp != 26: return False
    return True


def is_valid():
    if get_sum(1, 2, 3, 4) != 26: return False
    if get_sum(0, 2, 5, 7) != 26: return False
    if get_sum(0, 3, 6, 10) != 26: return False
    if get_sum(7, 8, 9, 10) != 26: return False
    if get_sum(1, 5, 8, 11) != 26: return False
    if get_sum(4, 6, 9, 11) != 26: return False
    return True


def solve(n):
    global done
    if done: return
    if not is_possible(): return
    if n == 12:
        if is_valid():
            done = True
            print_star()
            return
    for i in range(1, 13):
        if used[i]: continue
        used[i] = 1
        cur_idx = 0
        for j in range(12):
            if board_list[j] == 0:
                cur_idx = j
                board_list[j] = i
                break
        solve(n+1)
        board_list[cur_idx] = 0
        used[i] = 0


board = [input() for _ in range(5)]
board_list = []
used = [0] * 13
done = False
for row in board:
    for letter in row:
        if letter != '.' and letter != 'x':
            used[ord(letter) - 64] = 1
        if letter != '.':
            if letter == 'x':
                board_list.append(0)
            else:
                board_list.append(ord(letter) - 64)
cnt = sum(used)
solve(cnt)
