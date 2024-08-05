def get_diff_sum():
    res = 0
    for i in range(len(selected)):
        if selected[i]:
            res += problems[i]
    return res



def choose_problem(idx, cnt, diff_acc, min_diff, max_diff):
    global ans
    global selected
    if idx == len(problems):
        if cnt < 2 or max_diff - min_diff < X or not (L <= diff_acc <= R):
            return
        # print(selected)
        ans += 1
        return

    selected[idx] = 0
    choose_problem(idx + 1, cnt, diff_acc, min_diff, max_diff)
    selected[idx] = 1
    new_problem = problems[idx]
    if min_diff > new_problem:
        min_diff = new_problem
    if max_diff < new_problem:
        max_diff = new_problem
    diff_acc += new_problem
    choose_problem(idx + 1, cnt + 1, diff_acc, min_diff, max_diff)



N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
selected = [0] * len(problems)
ans = 0
choose_problem(0, 0, 0, 1_000_000_000, 0)
print(ans)