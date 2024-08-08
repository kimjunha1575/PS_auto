'''

- TSP(외판원 순회) 알고리즘을 변형해서 사용
- N!의 시간복잡도를 2^N * N^2의 시간복잡도로 낮출 수 있을 것으로 기대

- dp[employee][visited]를 아래와 같이 정의
- 현재 일 분배 상태가 visited 이고 employee 번째 직원이 선택할 차례일 때,
- 현재 직원부터 마지막 직원까지의 선택에서 구할 수 있는 성공률의 최대값

- 따라서 dp[0][0]는
- 아무 직원도 선택하지 않았고(0번째 직원의 차례)
- 아무런 일도 선택되지 않았을 때 (visited == 0)
- 그 이후 단계 전체에서 구할 수 있는 성공률의 최대값
- 즉, 모든 경우의 수 중 최대값을 구할 수 있다.

- 점화식
- dp[employee][visited] = max(dp[employee][visited], dp[employee + 1][visited | (1 << i)] for i in range(N))

'''


def dfs(employee, visited):
    # 현재 employee번 직원이 일을 선택할 차례이고, 일 분배 상태가 visited 일 때,
    # 현재 단계를 포함한 이후 단계 전체에서의 성공 확률 최대값

    # 모든 직원이 선택한 다음에는 이후 선택이 없다. 따라서 1 반환
    if employee == N:
        return 1

    # 이미 이후 단계의 값을 저장해 두었다면 바로 반환
    if dp[employee][visited] != -1:
        return dp[employee][visited]

    # 현재 직원이 선택할 수 있는 일들에 대해 최대값 구하기
    for i in range(N):
        # 이미 완료한 일은 무시
        if visited & (1 << i): continue

        # 현재 직원이 i번째 일을 선택했을 때 다음 직원부터 마지막 직원까지의 최대 성공률과
        # 기존에 저장되어 있던 초기값
        # 위 둘 중 큰 값으로 dp 배열을 갱신
        dp[employee][visited] = max(
            float(dp[employee][visited]), dfs(employee + 1, visited | (1 << i)) * board[employee][i]
        )
    # dp 배열에 저장 후 반환
    return dp[employee][visited]


T = int(input())
for case in range(1, T + 1):
    # 필요한 변수 초기화
    N = int(input())
    board = [list(map(lambda x: int(x) * 0.01, input().split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N)]

    # 0번째 직원이 선택해야 하고, 아무도 선택하지 않았을 때의 최대 확률을
    # 퍼센트 단위로 소수점 6번째 자리까지 출력
    print(f"#{case} {dfs(0, 0) * 100:0.6f}")
