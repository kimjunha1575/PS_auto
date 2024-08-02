from collections import deque
def solve():
    que = deque()
    que.append((S, 0))
    visited = set()
    visited.add(S)
    while que:
        cur, cnt = que.popleft()
        if cur == G:
            return cnt
        if cur + U <= F and cur + U not in visited:
            que.append((cur + U, cnt + 1))
            visited.add(cur + U)
        if cur - D >= 1 and cur - D not in visited:
            que.append((cur - D, cnt + 1))
            visited.add(cur - D)
    return -1


F, S, G, U, D = map(int, input().split())
ans = solve()
if ans != -1:
    print(ans)
else:
    print("use the stairs")
