#include <iostream>
#include <algorithm>
using namespace std;

int DP[1000001][2] = {0};
vector<int> map[1000001];
int visited[1000001] = {0};
int N;

void input() {
    cin >> N;
    for (int i = 0; i < N-1; i++) {
        int from, to;
        cin >> from >> to;
        map[from].push_back(to);
        map[to].push_back(from);
    }
}

void DFS(int node) {
    visited[node] = 1;
    DP[node][1] = 1;

    for (int i = 0; i < map[node].size(); i++) {
        int child = map[node][i];
        
        if (visited[child]) continue;
        DFS(child);
        DP[node][0] += DP[child][1];
        DP[node][1] += min(DP[child][1], DP[child][0]);
    }
}


int main(void) {
    input();
    DFS(1);
    cout << min(DP[1][0], DP[1][1]);
}

