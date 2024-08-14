'''
1 2 3 4
0 2 5 7
0 3 6 10
7 8 9 10
1 5 8 11
4 6 9 11

그냥 완전 주먹구구식으로 한번 해보고싶어서 해봤습니다
자리를 채우는 '.'이 아닌 문자만 순서대로 받아서 따로 배열에 순서대로 저장한 다음
각 인덱스 별로 '매직스타'에서 한 줄을 이루는 인덱스들을 미리 정리해두고 (주석 맨 위)
그냥 모든 경우에 대해 순서대로 빈 자리에 순열을 넣어서
유효한 매직스타인지 검사 후 맞으면 출력하고 종료했습니다
'''


def prt_board():
    print(f"....{chr(board_list[0] + 64)}....")
    print(f".{chr(board_list[1] + 64)}.{chr(board_list[2] + 64)}.{chr(board_list[3] + 64)}.{chr(board_list[4] + 64)}.")
    print(f"..{chr(board_list[5] + 64)}...{chr(board_list[6] + 64)}..")
    print(f".{chr(board_list[7] + 64)}.{chr(board_list[8] + 64)}.{chr(board_list[9] + 64)}.{chr(board_list[10] + 64)}.")
    print(f"....{chr(board_list[11] + 64)}....")


def get_sum(one, two, three, four):
    return board_list[one] + board_list[two] + board_list[three] + board_list[four]


def verify():
    if get_sum(1, 2, 3, 4) > 26:
        return False
    if get_sum(0, 2, 5, 7) > 26:
        return False
    if get_sum(0, 3, 6, 10) > 26:
        return False
    if get_sum(7, 8, 9, 10) > 26:
        return False
    if get_sum(1, 5, 8, 11) > 26:
        return False
    if get_sum(4, 6, 9, 11) > 26:
        return False
    return True


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
    if not verify():
        return
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
