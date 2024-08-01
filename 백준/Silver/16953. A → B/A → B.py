A, B = map(int, input().split())
q = [(A, 1)]
a = 0
h = 0
while h < len(q):
    v, r = q[h]
    h += 1
    if v > B: continue
    if v == B:
        a = r
        break
    q.append((v*2, r+1))
    q.append((v*10+1, r+1))
if a: print(a)
else: print(-1)