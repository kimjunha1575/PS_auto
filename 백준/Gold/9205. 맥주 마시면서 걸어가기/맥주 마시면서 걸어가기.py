def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def search(store):
    if get_dist(store, festival) <= 1000:
        return 1
    for i in range(n):
        if visited[i]: continue
        if get_dist(store, stores[i]) > 1000: continue
        visited[i] = 1
        if search(stores[i]):
            return 1
    return 0


T = int(input())
for case in range(1, T+1):
    n = int(input())
    home = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    festival = tuple(map(int, input().split()))
    if get_dist(home, festival) <= 1000:
        print("happy")
        continue
    ans = False
    visited = [0] * n
    for store in stores:
        if get_dist(home, store) <= 1000:
            if search(store):
                ans = True
                break
    if ans:
        print("happy")
    else:
        print("sad")
