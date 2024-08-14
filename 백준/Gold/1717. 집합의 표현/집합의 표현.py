'''
union-find (disjoint set)
입력에 따라 그때그때 실행하면서 출력해주면 된다.
'''
import sys
sys.setrecursionlimit(100000)


def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    pp = find(p)
    pq = find(q)
    if pp == pq: return
    if pp < pq:
        parent[pq] = pp
    else:
        parent[pp] = pq


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    command, p, q = map(int, input().split())
    if command:
        if find(p) == find(q):
            print("YES")
        else:
            print("NO")
    else:
        union(p, q)
