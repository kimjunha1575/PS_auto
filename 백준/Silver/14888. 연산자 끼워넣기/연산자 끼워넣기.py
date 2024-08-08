def calc(idx, acc, operator):
    cur = numbers[idx+1]
    if operator == 0:
        return acc + cur
    elif operator == 1:
        return acc - cur
    elif operator == 2:
        return acc * cur
    else:
        if acc < 0 < cur:
            return - (-acc // cur)
        return acc // cur


def solve(cnt, acc):
    if cnt == N-1:
        global ans_max
        global ans_min
        ans_max = max(ans_max, acc)
        ans_min = min(ans_min, acc)
        return
    for operator in range(len(operators)):
        if operators[operator] == 0: continue
        operators[operator] -= 1
        solve(cnt + 1, calc(cnt, acc, operator))
        operators[operator] += 1


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
ans_max = -1_000_000_000
ans_min = 1_000_000_000
solve(0, numbers[0])
print(ans_max)
print(ans_min)
