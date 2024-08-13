'''
1 2 3 4
0 2 5 7
0 3 6 10
7 8 9 10
1 5 8 11
4 6 9 11
'''


def prt_board():
    print(f"....{chr(board_list[0] + 64)}....")
    print(f".{chr(board_list[1] + 64)}.{chr(board_list[2] + 64)}.{chr(board_list[3] + 64)}.{chr(board_list[4] + 64)}.")
    print(f"..{chr(board_list[5] + 64)}...{chr(board_list[6] + 64)}..")
    print(f".{chr(board_list[7] + 64)}.{chr(board_list[8] + 64)}.{chr(board_list[9] + 64)}.{chr(board_list[10] + 64)}.")
    print(f"....{chr(board_list[11] + 64)}....")


def get_sum(one, two, three, four):
    return board_list[one] + board_list[two] + board_list[three] + board_list[four]


def is_possible():
    if get_sum(1, 2, 3, 4) != 26:
        return False
    if get_sum(0, 2, 5, 7) != 26:
        return False
    if get_sum(0, 3, 6, 10) != 26:
        return False
    if get_sum(7, 8, 9, 10) != 26:
        return False
    if get_sum(1, 5, 8, 11) != 26:
        return False
    if get_sum(4, 6, 9, 11) != 26:
        return False
    return True


def solve(n):
    global done
    if done: return
    if n == 12:
        if is_possible():
            done = True
            prt_board()
            return
    for i in range(1, 13):
        if used[i]: continue
        used[i] = 1
        for j in range(12):
            if board_list[j] == 0:
                tmp = j
                board_list[j] = i
                break
        solve(n+1)
        board_list[tmp] = 0
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
