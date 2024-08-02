from collections import deque

# 입력
N, K = map(int, input().split())

que = deque()
visited = dict()

# 시작위치 설정
que.append((N, 0))
visited[N] = 0

# 도착지에 방문했을 때의 이동 회수 저장할 배열
ans = []

# 도착할 수 있는 가장 빠른 시간 (순회하면서 갱신)
fastest_time = 100_001
# 도착했을 때의 이동 회수
move_cnt = 0

# 순회 시작
while que:
    cur_position, cur_time = que.popleft()
    # 목적지에 도착한 이후의 순회는 진행하지 않음
    if cur_time > fastest_time: break
    
    # 목적지에 도착하면 도착했을 때의 이동회수를 ans 배열에 넣고 최단시간 변수를 갱신
    if cur_position == K:
        ans.append(cur_time)
        fastest_time = cur_time
    
    # 3가지 경우의 수에 대해 순회
    targets = [cur_position - 1, cur_position + 1, cur_position * 2]
    for target in targets:
        # 범위를 벗어나면 무시
        if target < 0: continue
        if target > min(100000, max(N, K) * 2): continue
        # 더 적은 이동회수로 방문한 적이 있는 숫자는 무시
        if visited.get(target) is not None and cur_time + 1 > visited[target]: continue
        # 첫 방문이라면 방문한 시간 표시
        if visited.get(target) is None:
            visited[target] = cur_time+1
        # que에 추가
        que.append((target, cur_time + 1))
# 출력
print(fastest_time)
print(ans.count(fastest_time))
