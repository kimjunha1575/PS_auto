#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int V, E;
int start;
vector<int> graph[1001];
int visited[1001];


void init() {
    cin >> V >> E >> start;
    for (int i = 0; i < E; i++) {
        int from, to;
        cin >> from >> to;
        graph[from].push_back(to);
        graph[to].push_back(from);
    }
    for (int i = 1; i <= V; i++) {
        sort(graph[i].begin(), graph[i].end());
    }
}

void clear() {
    for (int i = 1; i <= V; i++) {
        visited[i] = 0;
    }
}

void bfs(int start) {
    queue<int> que;
    que.push(start);
    visited[start] = 1;
    while (!que.empty()) {
        int cur = que.front();
        que.pop();
        printf("%d ", cur);
        for (int vertex : graph[cur]) {
            if (visited[vertex]) continue;
            que.push(vertex);
            visited[vertex] = 1;
        }
    }
}

void dfs(int cur) {
    printf("%d ", cur);
    for (int vertex : graph[cur]) {
        if (visited[vertex]) continue;
        visited[vertex] = 1;
        dfs(vertex);
    }
}

int main(void) {
    init();
    visited[start] = 1;
    dfs(start);
    printf("\n");
    clear();
    bfs(start);
    printf("\n");
    return 0;
}
