#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Bus {
    int to, cost;

    Bus(int to, int cost) : to(to), cost(cost) {}

    int operator<(Bus o) const {
        return cost > o.cost;
    }
};

priority_queue<Bus> que;
vector<Bus> map[1001];
int dist[1001];
int V, E;
int start, dest;

int dijkstra() {
    que.push(Bus(start, 0));
    dist[start] = 0;
    while (!que.empty()) {
        Bus cur = que.top();
        que.pop();
        if (cur.to == dest) {
            return cur.cost;
        }
        for (Bus nxt : map[cur.to]) {
            if (dist[nxt.to] <= cur.cost + nxt.cost) continue;
            dist[nxt.to] = cur.cost + nxt.cost;
            que.push(Bus(nxt.to, cur.cost + nxt.cost));
        }
    }
    return dist[dest];
}


void init(void) {
    cin >> V >> E;
    for (int i = 1; i <= V; i++) {
        dist[i] = 0x7FFFFFFF;
    }
    for (int i = 0; i < E; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        map[from].push_back(Bus(to, cost));
    }
    cin >> start >> dest;
}

int main(void) {
    init();
    printf("%d\n", dijkstra());
    return 0;
}

