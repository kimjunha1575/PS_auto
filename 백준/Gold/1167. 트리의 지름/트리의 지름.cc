#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int V;
vector<pair<int, int>> tree[100001];
vector<int> edges[100001];
int visited[100001];

void init() {
    cin >> V;
    for (int i = 0; i < V; i++) {
        int st, en, weight;
        cin >> st;
        while (true) {
            cin >> en;
            if (en > 0) {
                cin >> weight;
                tree[st].push_back(make_pair(en, weight));
            }
            else break;
        }
    }
}

int search(int vertex, int cur_acc, int prev_weight) {
    edges[vertex].push_back(cur_acc);
    bool is_edge = true;
    for (int i = 0; i < tree[vertex].size(); i++) {
        int next_vertex = tree[vertex][i].first;
        int next_weight = tree[vertex][i].second;
        if (visited[next_vertex]) continue;
        is_edge = false;
        visited[next_vertex] = 1;
        edges[vertex].push_back(search(next_vertex, cur_acc + next_weight, next_weight));
    }
    if (is_edge) {
        edges[vertex].clear();
        edges[vertex].push_back(prev_weight);
        return prev_weight;
    }
    else {
        sort(edges[vertex].begin()+1, edges[vertex].end());
        return prev_weight + edges[vertex][edges[vertex].size()-1];
    }
}


int main(void) {
    init();
    visited[1] = 1;
    search(1, 0, 0);
    int ans = 0;
    for (int i = 1; i < V+1; i++) {
        int tmp = edges[i][edges[i].size()-1] + edges[i][edges[i].size()-2];
        ans = max(ans, tmp);
    }
    printf("%d\n", ans);
}
