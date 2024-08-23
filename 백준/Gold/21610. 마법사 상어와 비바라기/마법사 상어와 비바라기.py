'''
1432 1번문제 읽기시작
2차원 배열에서의 완전탐색
배열 크기 최대 50 * 50, 명령 회수 최대 100
다만 배열 밖으로 나가면 반대쪽으로 나오도록 연결해야하고
절차에 따라 구현 + 상태체크 필요
시간복잡도에 대한 고민은 크게 하지 않아도 될 듯 함


1436 2번문제 읽기시작
2N 크기의 1차배열에서 올리는 위치와 내리는 위치를 투포인터처럼 움직이면서
단계별 시뮬레이션 구현

1440 난이도 차이 크게 느껴지지 않으나 구현 조건이 2번이 더 간단해보이므로 2번 풀이 시작
구상 1
2N 크기의 1차배열을 선언한 뒤 올리는 위치, 내리는 위치의 인덱스를 옮겨가면서 단계 진행
단계가 넘어갈 때 마다 올리는 위치와 내리는 위치의 인덱스를 1 씩 빼준다(컨베이어 벨트 진행)
나머지는 문제에 제시된 그대로 진행
1453 간단히 구현 완료(디테일한 부분 아직 고려 안함), 예제 테스트, 인덱스에러
1457 다른 인덱스에러까지 확인 후 에러는 아니지만 오답 출력. 디버깅 시작
(인덱싱이 의심스러움)
벨트가 한 칸 이동하면서 시작하는게 맞는지..?? 맞는거였음
1518 수정 후 예제에 대해 정답 확인, 제출 -> 정답

1521 1번문제 설계 시작
2번문제와 비슷하게 문제에서 제시한 순서대로 그대로 구현하면 될 듯 함
입력 조건 상 크게 자료구조나 알고리즘적으로 고민할 부분 없어보임
디테일한 부분은 구현하면서 수정
1523 구현 시작
1530 간단한 플로우만 잡은 스켈레톤 완성, 입력만 테스트
1541 어느정도 구현 완료, 예제 테스트 -> 오답 디버깅 시작
1554 예제에 대해 정답 확인, 제출
'''
from collections import deque

DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
DIAG_DIRECTIONS = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
prev_cloud = [[0] * N for _ in range(N)]
prev_cloud[N-1][0] = 1
prev_cloud[N-2][0] = 1
prev_cloud[N-1][1] = 1
prev_cloud[N-2][1] = 1
for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    cloud = [[0] * N for _ in range(N)]
    cloud_disappeared = [[0] * N for _ in range(N)]
    # 모든 구름이 d 방향으로 s 칸 이동한다
    dr, dc = DIRECTIONS[d]
    dr *= s
    dc *= s
    for r in range(N):
        for c in range(N):
            if prev_cloud[r][c] == 0: continue
            nr = (r + dr) % N
            nc = (c + dc) % N
            cloud[nr][nc] = 1
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다
    water_bug_targets = deque()
    for r in range(N):
        for c in range(N):
            if not cloud[r][c]: continue
            board[r][c] += 1
            water_bug_targets.append((r, c))
    # 구름이 모두 사라진다
    for r in range(N):
        for c in range(N):
            if cloud[r][c]:
                cloud_disappeared[r][c] = 1
            cloud[r][c] = 0
    # 물의 양이 증가한 칸에 대해 물복사버그 마법 시전
        # 대각선 방향 거리 1인 칸에 물이 있는 '바구니 수'만큼 물 양 증가
        # 경계 넘어가는 칸은 대상으로 하지 않는다
    while water_bug_targets:
        r, c = water_bug_targets.popleft()
        tmp = 0
        for dr, dc in DIAG_DIRECTIONS:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            if not board[nr][nc]: continue
            tmp += 1
        board[r][c] += tmp
    # 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다
        # 이번 차례에 구름이 사라진 칸이 아니어야 한다
    for r in range(N):
        for c in range(N):
            if cloud_disappeared[r][c]: continue
            if board[r][c] < 2: continue
            cloud[r][c] = 1
            board[r][c] -= 2

    prev_cloud = cloud.copy()

ans = 0
for r in range(N):
    for c in range(N):
        ans += board[r][c]
print(ans)
