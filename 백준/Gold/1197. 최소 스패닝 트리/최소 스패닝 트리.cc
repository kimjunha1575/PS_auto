#include <algorithm>
#include <queue>
#include <iostream>
#include <vector>
using namespace std;

struct Edge {
    int from;
    int to;
    int cost;

    // pq는 아니지만, algorithm 헤더의 sort를 사용하기 때문에 이거 필요함.
    bool operator<(Edge e) const {
        if (cost < e.cost) return true;
        return false;
    }
};

int V, E;
Edge edges[100001];
int visited[10001] = {0};
int parent[10001];

void input() {
    cin >> V >> E;
    for (int i = 0; i < E; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        edges[i] = (Edge){from, to, cost};
    }
    // 이미 노드가 존재하는 상황이므로 전부 바로 초기화
    for (int i = 1; i <= V; i++)
        parent[i] = i;
}

int Find(int n) {
    if (parent[n] == n) return n;
    return parent[n] = Find(parent[n]);
}

void Union(int n1, int n2) {
    int r1 = Find(n1);
    int r2 = Find(n2);
    parent[r2] = r1;
}

int main(void) {
    int ans = 0;
    input();
    // kruskal's algorithm이므로 정렬해주기~
    // ++ edge의 추가가 자주 이루어지는 상황이 아니므로
    // 그냥 배열에 저장하여 정렬 후 사용!
    sort(edges, edges + E);

    for (int i = 0; i < E; i++) {
        Edge now = edges[i];
        // 현재 엣지로 이어진 두 노드가 이미 연결되어 있는 경우 무시
        if (Find(now.from) == Find(now.to)) continue;
        // 연결되어 있지 않은 경우, 그룹을 형성시켜주고
        // 엣지의 cost를 정답에 누적해준다.
        // 이 때, 문제 상황에서는 이미 그래프가 존재하는 상태에서 MST를 형성하는 데 필요한
        // 최소의 cost만 구하면 되므로, 그룹 형성, 누적합만 구해주면 된다! 다른 처리 필요 없음.
        Union(now.from, now.to);
        ans += now.cost;
    }
    cout << ans;
}