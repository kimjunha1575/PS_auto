#include <iostream>
#include <queue>
using namespace std;

#define MAX_ROW  50
#define MAX_COL  50
#define MAX_TIME 20

// vector<pair<int, int>> points[MAX_TIME + 1];
vector<int> dirs[8];
int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};

int height, width;
int map[MAX_ROW][MAX_COL];
// int pipe[MAX_ROW][MAX_COL];
int rs, cs, past;

void input() {

    cin >> height >> width;
    cin >> rs >> cs >> past;
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cin >> map[i][j];
        }
    }
}

bool isConnected(int dir, int ny, int nx) {
    for (int i = 0; i < dirs[map[ny][nx]].size(); i++) {
        if (dirs[map[ny][nx]][i] == (dir + 2) % 4) return true;
    }
    return false;
}

int solve() {
    int res = 0;
    queue<pair<int, int>> que;
    int dist[MAX_ROW][MAX_COL] = {0};
    que.push({rs, cs});
    dist[rs][cs] = 1;

    while (not que.empty()) {
        int y = que.front().first;
        int x = que.front().second;
        que.pop();

        // printf("visited (%d,%d)\n", y, x);

        res++;

        if (dist[y][x] >= past) continue;

        for (int dir = 0; dir < dirs[map[y][x]].size(); dir++) {
            int ny = y + dy[dirs[map[y][x]][dir]];
            int nx = x + dx[dirs[map[y][x]][dir]];

            if (ny < 0 || nx < 0 || ny >= height || nx >= width) continue;
            if (dist[ny][nx]) continue;
            if (map[ny][nx] == 0) continue;

            if (isConnected(dirs[map[y][x]][dir], ny, nx)) {
                dist[ny][nx] = dist[y][x] + 1;
                que.push({ny, nx});
            }
        }
    }

    return res;
}

void init() {
    dirs[1].push_back(0);
    dirs[1].push_back(1);
    dirs[1].push_back(2);
    dirs[1].push_back(3);

    dirs[2].push_back(1);
    dirs[2].push_back(3);

    dirs[3].push_back(0);
    dirs[3].push_back(2);

    dirs[4].push_back(0);
    dirs[4].push_back(3);

    dirs[5].push_back(0);
    dirs[5].push_back(1);

    dirs[6].push_back(1);
    dirs[6].push_back(2);

    dirs[7].push_back(2);
    dirs[7].push_back(3);
}

int main(void) {
    int T;
    cin >> T;
    init();
    for (int test = 1; test <= T; test++) {
        input();
        // for (int i = 0; i <= MAX_TIME; i++) points[i].clear();
        int ans = solve();
        printf("#%d %d\n", test, ans);
    }
}

/*
#1 5
#2 15
#3 29
#4 67
#5 71
*/