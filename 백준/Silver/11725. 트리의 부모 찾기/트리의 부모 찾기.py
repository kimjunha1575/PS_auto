def find_parent_recursion(idx):
    global visited
    global parents
    visited[idx] = 1
    children = tree[idx]
    for child in children:
        if visited[child]:
            continue
        visited[child] = 1
        parents[child] = idx
        find_parent_recursion(child)


def find_parent_loop(idx, root):
    global visited
    global parents
    que = [root]
    while que:
        cur_node = que.pop(0)
        visited[cur_node] = 1
        targets = tree[cur_node]
        for target in targets:
            if visited[target]:
                continue
            parents[target] = cur_node
            que.append(target)
    return None


tree_size = int(input())
tree = [[] for _ in range(tree_size + 1)]
for _ in range(tree_size - 1):
    m, n = map(int, input().split())
    tree[m].append(n)
    tree[n].append(m)

parents = [None] * (tree_size + 1)
visited = [0] * (tree_size + 1)
find_parent_loop(1, 1)

for node in range(2, tree_size + 1):
    print(parents[node])
