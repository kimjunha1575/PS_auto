'''
union-find (disjoint set)
입력에 따라 그때그때 실행하면서 출력해주면 된다.
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def find(p, d):
    global depth
    depth = max(depth, d)
    if parent[p] != p:
        parent[p] = find(parent[p], d + 1)
    return parent[p]


def union(p, q):
    pp = find(p, 0)
    pq = find(q, 0)
    if pp == pq: return
    if pp < pq:
        parent[pq] = pp
    else:
        parent[pp] = pq


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
depth = 0
for _ in range(m):
    command, p, q = map(int, input().split())
    if command:
        if find(p, 0) == find(q, 0):
            print("YES")
        else:
            print("NO")
    else:
        union(p, q)

# print(parent)
# print(depth)
