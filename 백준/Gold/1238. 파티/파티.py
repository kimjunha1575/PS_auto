from queue import PriorityQueue


class Vertex:
    def __init__(self, st, en, cost):
        self.st = st
        self.en = en
        self.cost = cost

    def __lt__(self, o):
        return self.cost < o.cost


def dijkstra1(arr, target):
    global paths
    que = PriorityQueue()
    que.put(Vertex(target, target, 0))
    arr[target] = 0
    while not que.empty():
        cur_node = que.get()
        cur_town = cur_node.en
        cur_cost = cur_node.cost
        for next_town in range(N):
            if paths[cur_town][next_town] is None:
                continue
            next_cost = cur_cost + paths[cur_town][next_town]
            if next_cost >= arr[next_town]:
                continue
            que.put(Vertex(cur_town, next_town, next_cost))
            arr[next_town] = next_cost
    return None


def dijkstra2(arr, target):
    global paths
    que = PriorityQueue()
    que.put(Vertex(target, target, 0))
    arr[target] = 0
    while not que.empty():
        cur_node = que.get()
        cur_town = cur_node.en
        cur_cost = cur_node.cost
        for next_town in range(N):
            if paths[next_town][cur_town] is None:
                continue
            next_cost = cur_cost + paths[next_town][cur_town]
            if next_cost >= arr[next_town]:
                continue
            que.put(Vertex(cur_town, next_town, next_cost))
            arr[next_town] = next_cost
    return None


N, M, X = map(int, input().split())
paths = [[None for _ in range(N)] for _ in range(N)]

for _ in range(M):
    st, en, cost = map(int, input().split())
    paths[st - 1][en - 1] = cost

dist1 = [10**8 for _ in range(N)]
dist2 = [10**8 for _ in range(N)]
dijkstra1(dist1, X-1)
# print(dist1)
dijkstra2(dist2, X-1)
# print(dist2)

res = 0
for town in range(N):
    tmp = dist1[town] + dist2[town]
    res = max(tmp, res)
print(res)
