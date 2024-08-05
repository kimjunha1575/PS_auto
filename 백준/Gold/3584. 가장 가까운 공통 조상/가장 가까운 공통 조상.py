
T = int(input())
for case in range(1, T+1):
    V = int(input())
    tree = [None for _ in range(V+1)]
    for _ in range(V-1):
        parent, child = map(int, input().split())
        tree[child] = parent
    target1, target2 = map(int, input().split())
    parents_of_target1 = []
    v = target1
    while v:
        parents_of_target1.append(v)
        parent = tree[v]
        v = parent
    v = target2
    while v not in parents_of_target1:
        v = tree[v]
    print(v)
