#include <iostream>
#include <queue>
#include <stack>
using namespace std;

int V, E;
int start;
int graph[1001][1001];
int visited[1001];


void init() {
    cin >> V >> E >> start;
    for (int i = 0; i < E; i++) {
        int from, to;
        cin >> from >> to;
        graph[from][to] = 1;
        graph[to][from] = 1;
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
        for (int i = 1; i <= V; i++) {
            if (graph[cur][i] == 0) continue;
            if (visited[i]) continue;
            que.push(i);
            visited[i] = 1;
        }
    }
}

void dfs(int cur) {
    printf("%d ", cur);
    for (int i = 1; i <= V; i++) {
        if (graph[cur][i] == 0) continue;
        if (visited[i]) continue;
        visited[i] = 1;
        dfs(i);
    }
}

int main(void) {
    init();
    visited[start] = 1;
    dfs(start);
    printf("\n");
    clear();
    bfs(start);
    return 0;
}
