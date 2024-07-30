def solve(idx):
    global operators
    global combination
    global ans_max
    global ans_min
    if idx == N - 1:
        tmp = arr[0]
        for i in range(N-1):
            operator = combination[i]
            operand = arr[i+1]
            if operator == 0:
                tmp += operand
            elif operator == 1:
                tmp -= operand
            elif operator == 2:
                tmp *= operand
            else:
                if tmp < 0 < operand:
                    tmp = -((-tmp)//operand)
                else:
                    tmp //= operand
        ans_max = max(ans_max, tmp)
        ans_min = min(ans_min, tmp)
        return None
    for i in range(len(operators)):
        if operators[i] == 0: continue
        combination[idx] = i
        operators[i] -= 1
        solve(idx + 1)
        operators[i] += 1
    return None


N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))
ans_max = -1000000000
ans_min = 1000000000
combination = [None] * (N - 1)
solve(0)
print(ans_max)
print(ans_min)
