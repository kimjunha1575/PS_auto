import heapq


# 각 버스의 운행 정보를 담는 클래스
class Bus:
    # 도착지와 비용을 저장한다
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

    # pq의 우선순위 설정을 위한 연산자 설정
    def __lt__(self, other):
        return self.cost < other.cost


def dijkstra():
    # 출발지를 향하는 비용 0의 버스를 초기값으로 넣어두고 시작
    que = [Bus(start, 0)]
    dist = [INF] * (V + 1)
    # 출발지까지의 최소비용을 0으로 초기화
    dist[start] = 0
    while que:
        cur = heapq.heappop(que)
        cur_cost, dest = cur.cost, cur.dest
        # 도착했다면 즉시 누적된 비용을 반환
        if dest == end:
            return cur_cost
        # 현재 도시에서 탈 수 있는 버스 중
        for bus in bus_map[dest]:
            nxt_dest, nxt_cost = bus.dest, bus.cost
            # 비용이 최소가 되는 버스만 탑승
            if dist[nxt_dest] <= cur_cost + nxt_cost: continue
            dist[nxt_dest] = cur_cost + nxt_cost
            heapq.heappush(que, Bus(nxt_dest, cur_cost + nxt_cost))
    return dist[end]


INF = 2_100_000_000

V = int(input())
E = int(input())
# 버스 운행 정보를 저장할 배열
bus_map = [[] for _ in range(V + 1)]
for _ in range(E):
    frm, to, cost = map(int, input().split())
    # 출발지에서 탈 수 있는 버스 정보를 저장
    bus_map[frm].append(Bus(to, cost))
start, end = map(int, input().split())
print(dijkstra())
