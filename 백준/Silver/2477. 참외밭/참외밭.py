K = int(input())
move = []
order = [None] * 4
case = [0] * 6
for i in range(6):
    di, dist = map(int, input().split())
    move.append((di, dist))
    if order[di-1] is None:
        order[di-1] = i
    else:
        case[i] = 1
        case[order[di-1]] = 1
total = 1
for i in range(len(case)):
    if case[i] == 0:
        total *= move[i][1]
case = ''.join(map(str, case))
if "1111" in case:
    i = case.find("1111")
    sub = move[i+1][1] * move[i+2][1]
elif case == "110011":
    sub = move[0][1] * move[5][1]
elif case == "100111":
    sub = move[4][1] * move[5][1]
elif case == "111001":
    sub = move[0][1] * move[1][1]

print((total - sub) * K)

'''
        x x x _ _ x -> 첫 두개
        x _ _ x x x -> 마지막 두개
        x x _ _ x x -> 처음과 마지막
        x x x x     -> 2,3번째
    - 안들어간 곳 3개 (변형 없는 곳)
        - 어떻게 돌든 4번 중 2,3번째가 들어간 곳
'''