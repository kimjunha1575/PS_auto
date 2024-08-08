def find_odd(row, cnt):
    if row == odd_size:
        global cnt_odd
        cnt_odd = max(cnt_odd, cnt)
        return
    for i in range(odd_size):
        if odd[row][i] in [-1, 0]: continue
        if visited[i]: continue
        visited[i] = 1
        find_odd(row + 1, cnt + 1)
        visited[i] = 0
    find_odd(row + 1, cnt)


def find_even(row, cnt):
    if row == even_size:
        global cnt_even
        cnt_even = max(cnt_even, cnt)
        return
    for i in range(even_size):
        if even[row][i] in [-1, 0]: continue
        if visited[i]: continue
        visited[i] = 1
        find_even(row + 1, cnt + 1)
        visited[i] = 0
    find_even(row + 1, cnt)

board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]
if board_size % 2:
    odd_size = board_size - 1
    even_size = board_size
else:
    odd_size = board_size
    even_size = board_size
odd = [[-1] * odd_size for _ in range(odd_size)]
even = [[-1] * even_size for _ in range(even_size)]

if board_size % 2:
    for r in range(board_size):
        for c in range(board_size):
            if (r + c) % 2:
                odd[(r + c) // 2][(odd_size + 1) // 2 + (c - r - 1) // 2] = board[r][c]
            else:
                even[(r+c)//2][(even_size-(r+c))//2 + c] = board[r][c]
else:
    for r in range(board_size):
        for c in range(board_size):
            if (r + c) % 2:
                odd[(r + c) // 2][(odd_size + 1) // 2 + (c - r - 1) // 2] = board[r][c]
            else:
                even[(r+c)//2][(even_size-(r+c))//2 + c] = board[r][c]


# for row in odd:
#     print(row)
#
# for row in even:
#     print(row)
# odd
cnt_odd = 0
visited = [0] * odd_size
find_odd(0, 0)

# even
cnt_even = 0
visited = [0] * even_size
find_even(0, 0)


print(cnt_odd + cnt_even)


'''

'''