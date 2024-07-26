K = int(input())
move = []
order = [None] * 4
case = [0] * 6
for i in range(6):
    di, dist = map(int, input().split())
    move.append(dist)
    if order[di-1] is None:
        order[di-1] = i
    else:
        case[i] = 1
        case[order[di-1]] = 1
total = 1
for i in range(len(case)):
    if case[i] == 0:
        total *= move[i]
case = ''.join(map(str, case))
if case == "111001":
    total -= move[0] * move[1]
elif case == "110011":
    total -= move[0] * move[5]
elif case == "100111":
    total -= move[4] * move[5]
else:
    i = case.find("1111")
    total -= move[i+1] * move[i+2]
print(total * K)
