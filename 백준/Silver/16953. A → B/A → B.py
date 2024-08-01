from collections import deque
A, B = map(int, input().split())
q = deque()
q.append((A, 1))
a = 0
while q:
    v = q[0][0]
    r = q.popleft()[1]
    if v > B: continue
    if v == B:
        a = r
        break
    q.append((v*2, r+1))
    q.append((v*10 + 1, r+1))
if a: print(a)
else: print(-1)