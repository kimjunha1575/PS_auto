'''
0부터 총 예산까지의 예산 중 가능한 최대 예산을 이진탐색
'''


def is_possible(budget):
    acc = 0
    for i in range(N):
        if budgets[i] < budget:
            acc += budgets[i]
        else:
            acc += (N - i) * budget
            break
    return acc <= limit


def binary_search():
    left = 0
    right = limit
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            left = mid + 1
        else:
            right = mid - 1
    if not right < 0:
        return right
    return left


N = int(input())
budgets = list(map(int, input().split()))
budgets.sort()
limit = int(input())
ans = binary_search()
if ans >= budgets[-1]:
    print(budgets[-1])
else:
    print(ans)
