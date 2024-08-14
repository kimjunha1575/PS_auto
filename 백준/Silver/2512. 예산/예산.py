def is_possible(budget):
    left = 0
    right = len(budgets) - 1
    while left <= right:
        mid = (left + right) // 2
        if budgets[mid] < budget:
            left = mid + 1
        else:
            right = mid - 1
    if not left >= len(budgets):
        idx = left
    else:
        idx = right
    return sum(budgets[:idx]) + budget * (len(budgets) - idx) <= limit


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
