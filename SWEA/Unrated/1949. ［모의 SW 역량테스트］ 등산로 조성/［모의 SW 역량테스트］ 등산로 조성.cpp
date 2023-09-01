#include <iostream>
#include <vector>
using namespace std;

#define MAX_MAP_SIZE 8

// 가장 높은 봉우리에서 시작
// 높은 지형에서 낮은 지형으로 가로/세로 방향 연결
// 단 한 곳의 높이를 최대 K만큼 깎을 수 있다.

int N, K;
int map[MAX_MAP_SIZE][MAX_MAP_SIZE];
int dp[MAX_MAP_SIZE][MAX_MAP_SIZE];
bool visited[MAX_MAP_SIZE][MAX_MAP_SIZE];
vector<pair<int, int>> start_points;

int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};

int input() {
    int res = 0;
    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
            if (map[i][j] > res) res = map[i][j];
        }
    }
    return res;
}

void findHighest(int highest) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (map[i][j] == highest) {
                start_points.push_back({i, j});
            }
        }
    }
}

void initVisited() {
    for (int i = 0; i < MAX_MAP_SIZE; i++) {
        for (int j = 0; j < MAX_MAP_SIZE; j++) {
            visited[i][j] = false;
        }
    }
}

void initDP() {
    for (int i = 0; i < MAX_MAP_SIZE; i++) {
        for (int j = 0; j < MAX_MAP_SIZE; j++) {
            dp[i][j] = 0;
        }
    }
}

int DFS(int y, int x, bool worked) {
    // printf("visited (%d,%d)\n", y, x);
    // if (not worked and dp[y][x]) return dp[y][x];
    int res = 0;
    int tmp = 0;

    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
        if (visited[ny][nx]) continue;
        if (map[ny][nx] - map[y][x] >= K) continue;
        if (worked and map[ny][nx] >= map[y][x]) continue;

        if (not worked && map[ny][nx] >= map[y][x] && map[ny][nx] - map[y][x] < K) {
            // 공사 ㅇ
            visited[ny][nx] = true;
            int recover = map[ny][nx];
            map[ny][nx] = map[y][x] - 1;
            // printf("worked ( (%d,%d): %d -> %d )\n", ny, nx, recover, map[ny][nx]);
            tmp = DFS(ny, nx, true);
            // printf("recovered ( (%d,%d): %d -> %d )\n", ny, nx, map[ny][nx], recover);
            map[ny][nx] = recover;
            visited[ny][nx] = false;
            if (tmp > res) res = tmp;
        }
        else if (map[ny][nx] < map[y][x]) {
            // 공사 ㄴ
            visited[ny][nx] = true;
            tmp = DFS(ny, nx, worked);
            visited[ny][nx] = false;
            if (tmp > res) res = tmp;
        }
    }
    // if (not worked) dp[y][x] = res + 1;
    // printf("return %d\n", res+1);
    return res+1;
}

int main(void) {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int highest = input();
        findHighest(highest);
        int ans = 0;
        for (int i = 0; i < start_points.size(); i++) {
            int ys = start_points[i].first;
            int xs = start_points[i].second;
            initVisited();
            visited[ys][xs] = true;
            // printf("start searching at (%d,%d)\n", ys, xs);
            int tmp = DFS(ys, xs, false);
            visited[ys][xs] = false;
            if (tmp > ans) ans = tmp;
        }
        printf("#%d %d\n", test, ans);
        start_points.clear();
        // initDP();
    }
}

/*
#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19
*/