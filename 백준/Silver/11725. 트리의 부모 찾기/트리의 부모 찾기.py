
V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    st, en = map(int, input().split())
    tree[st].append(en)
    tree[en].append(st)
parent = [0] * (V+1)
parent[1] = 1
stk = [1]
while stk:
    cur = stk.pop()
    for vtx in tree[cur]:
        if parent[vtx]: continue
        parent[vtx] = cur
        stk.append(vtx)
print(*parent[2:], sep='\n')
