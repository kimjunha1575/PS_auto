from collections import deque


def solve():
    que = deque()
    visited = set()
    
    # 시작위치 설정
    que.append((S, 0))
    visited.add(S)
    
    # 순회 시작
    while que:
        cur, cnt = que.popleft()
        # 도착했다면 이동 회수를 반환
        if cur == G:
            return cnt
        # 각 방향에 대해 방문한 적이 없고, 이동할 수 있는 범위라면 que에 추가
        if cur + U <= F and cur + U not in visited:
            que.append((cur + U, cnt + 1))
            visited.add(cur + U)
        if cur - D >= 1 and cur - D not in visited:
            que.append((cur - D, cnt + 1))
            visited.add(cur - D)
    # 목적지에 도착하지 못했다면 -1 반환
    return -1


# 입력
F, S, G, U, D = map(int, input().split())
# 순회
ans = solve()
# 도착했다면 이동 회수를, 도착할 수 없다면 use the stairs 출력
if ans != -1:
    print(ans)
else:
    print("use the stairs")
