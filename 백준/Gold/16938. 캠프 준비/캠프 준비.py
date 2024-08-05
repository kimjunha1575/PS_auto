def choose_problem(idx, cnt, diff_acc, min_diff, max_diff):
    # 사용할 문제를 고른 후 조건에 맞으면 ans에 1을 더한다
    if idx == len(problems):
        # 모든 문제에 대해 사용 여부가 결정되면
        # 조건에 맞는 지 확인 후 맞다면 ans에 1을 더한다
        if cnt < 2 or max_diff - min_diff < X or not (L <= diff_acc <= R):
            return 0
        return 1

    res = 0

    # idx번째 문제를 사용하지 않는 경우
    res += choose_problem(idx + 1, cnt, diff_acc, min_diff, max_diff)

    # idx번째 문제를 사용하는 경우
    # 사용할 경우 난이도 합, 최대난이도, 최소난이도를 갱신 후 재귀 호출
    new_problem = problems[idx]
    if min_diff > new_problem:
        min_diff = new_problem
    if max_diff < new_problem:
        max_diff = new_problem
    diff_acc += new_problem
    res += choose_problem(idx + 1, cnt + 1, diff_acc, min_diff, max_diff)
    return res


N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
print(choose_problem(0, 0, 0, 2_000_000, 0))
