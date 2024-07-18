#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, M;
int lab[8][8];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
vector<pair<int, int>> wall;

// bfs 1회 당 최대 순회 대충 60이라고 잡고
// 빈 칸 최대 60개
// 60개 중 3칸 선택 -> 60 * 60 * 60 -> 216000 * 60
// 대충 13,000,000
// 최악의 케이스에도 2초 내에 실행 될 것으로 예상

void init() {
    cin >> N >> M;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < M; x++) {
            cin >> lab[y][x];
            if (lab[y][x] == 0) {
                wall.push_back(make_pair(y, x));
            }
        }
    }
}

void bfs(int map[8][8]) {
    int visited[8][8];
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            visited[i][j] = 0;
    queue<pair<int, int>> que;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < M; x++) {
            if (map[y][x] == 2) {
                que.push(make_pair(y, x));
            }
        }
    }
    while (!que.empty()) {
        int y = que.front().first;
        int x = que.front().second;
        visited[y][x] = 1;
        que.pop();

        for (int dir = 0; dir < 4; dir++) {
            int ny = y + dy[dir];
            int nx = x + dx[dir];

            if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
            if (visited[ny][nx]) continue;
            if (map[ny][nx] == 1) continue;

            map[ny][nx] = 2;
            que.push(make_pair(ny, nx));
        }
    }
}

int getMax() {
    int res = 0;
    for (int i = 0; i < wall.size()-2; i++) {
        pair<int, int> first_wall = wall[i];
        lab[first_wall.first][first_wall.second] = 1;
        for (int j = i+1; j < wall.size()-1; j++) {
            pair<int, int> second_wall = wall[j];
            lab[second_wall.first][second_wall.second] = 1;
            for (int k = j+1; k < wall.size(); k++) {
                pair<int, int> third_wall = wall[k];
                lab[third_wall.first][third_wall.second] = 1;
                // copy lab's map
                int map[8][8];
                for (int y = 0; y < N; y++) {
                    for (int x = 0; x < M; x++) {
                        map[y][x] = lab[y][x];
                    }
                }
                // do bfs
                bfs(map);
                // calculate save area
                int cnt = 0;
                for (int y = 0; y < N; y++) {
                    for (int x = 0; x < M; x++) {
                        if (map[y][x] == 0)
                            cnt++;
                    }
                }
                if (cnt > res) {
                    res = cnt;
                }
                // remove wall
                lab[third_wall.first][third_wall.second] = 0;
            }
            lab[second_wall.first][second_wall.second] = 0;
        }
        lab[first_wall.first][first_wall.second] = 0;
    }
    return res;
}

int main(void) {
    init();
    printf("%d\n", getMax());
    return 0;
}
