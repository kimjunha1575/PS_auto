#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Edge {
    int cost;
    int from;
    int to;

    bool operator<(Edge e) const {
        if (cost < e.cost) return true;
        return false;
    }
};

int cntVertex, cntEdge;
int parent[1001];
int cnt[1001];
char gender[1001];
Edge edges[10000];

int Find(int n) {
    if (parent[n] == n) return n;
    return parent[n] = Find(parent[n]);
}

void Union(int n1, int n2) {
    int r1 = Find(n1);
    int r2 = Find(n2);
    parent[r2] = r1;
    cnt[r1] += cnt[r2];
    cnt[r2] = 0;
}

void input() {
    cin >> cntVertex >> cntEdge;
    for (int i = 1; i <= cntVertex; i++) {
        cin >> gender[i];
        parent[i] = i;
        cnt[i] = 1;
    }
    for (int i = 0; i < cntEdge; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        edges[i] = (Edge){cost, from, to};
    }
    sort(edges, edges+cntEdge);
}

int main(void) {
    input();
    int validity = 0;
    int ans = 0;
    for (int i = 0; i < cntEdge; i++) {
        Edge now = edges[i];
        if (gender[now.from] == gender[now.to]) continue;
        if (Find(now.from) == Find(now.to)) continue;
        Union(now.from, now.to);
        ans += now.cost;
        if (cnt[Find(cntVertex)] == cntVertex) {
            validity = 1;
            break;
        }
    }
    if (validity) cout << ans;
    else cout << -1;
    return 0;
}