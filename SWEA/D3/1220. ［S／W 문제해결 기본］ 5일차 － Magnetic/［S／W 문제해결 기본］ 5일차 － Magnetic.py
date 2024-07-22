def pull(table, col):
    ret = 0
    flag = False
    for i in range(100):
        if flag is False and table[i][col] == 1:
            flag = True
        elif flag is True and table[i][col] == 2:
            ret += 1
            flag = False
    return ret


def solve():
    input()
    table = [[None for _ in range(100)] for _ in range(100)]
    for row in range(100):
        table[row] = list(map(int, input().split()))
    ret = 0
    for col in range(100):
        ret += pull(table, col)
    return ret


for tc in range(1, 11):
    res = solve()
    print(f"#{tc} {res}")
