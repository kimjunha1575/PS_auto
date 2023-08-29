#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

struct Node {
    int y;
    int x;
    int cost;

    bool operator<(Node p) const {
        if (cost <= p.cost) return false;
        else return true;
    }
};

int N;
int map[50][50];
int dist[50][50];
int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};

void dijkstra() {
    priority_queue<Node> pq;
    pq.push((Node){0, 0, 0});
    dist[0][0] = 0;

    while (!pq.empty()) {
        Node now = pq.top(); pq.pop();
        int y = now.y;
        int x = now.x;
        int cost = now.cost;

        if (dist[y][x] < cost) continue;

        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
            if (dist[ny][nx] <= dist[y][x] + map[ny][nx]) continue;

            dist[ny][nx] = dist[y][x] + map[ny][nx];
            pq.push((Node){ny, nx, dist[ny][nx]});
        }

    }
}

void input() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < N; j++) {
            if (tmp[j] == '1') map[i][j] = 0;
            else map[i][j] = 1;
            dist[i][j] = 214738364;
        }
    }
}

int main(void) {
    input();
    dijkstra();
    printf("%d\n", dist[N-1][N-1]);
}