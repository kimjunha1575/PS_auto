#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    int weight;
};

vector<Edge> map[100001];
int visited[100001] = {0};
int vertex, robot1, robot2;
int max_weight = 0;
int sum = 0;

void input() {
    cin >> vertex >> robot1 >> robot2;
    for (int i = 0; i < vertex-1; i++) {
        int from, to, weight;
        cin >> from >> to >> weight;
        map[from].push_back((Edge){to, weight});
        map[to].push_back((Edge){from, weight});
    }
}

void DFS(int node) {
    if (node == robot2) {
        cout << sum - max_weight;
        return;
    }
    else {
        for (int i = 0; i < map[node].size(); i++) {
            int next = map[node][i].to;
            int next_w = map[node][i].weight;

            if (visited[next]) continue;

            int tmp = max_weight;
            if (max_weight < next_w) {
                max_weight = next_w;
            }
            sum += next_w;
            visited[next] = 1;
            DFS(next);
            visited[next] = 0;
            sum -= next_w;
            max_weight = tmp;
        }
    }





}

int main() {
    input();
    visited[robot1] = 1;
    DFS(robot1);
}