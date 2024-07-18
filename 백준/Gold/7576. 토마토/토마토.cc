#include <iostream>
#include <queue>

using namespace std;

int width, height;
int box[1000][1000];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

void init() {
    cin >> width >> height;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            cin >> box[y][x];
        }
    }
}

void bfs() {
    queue<pair<int, int>> que;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (box[y][x] == 1) {
                que.push(make_pair(y, x));
            }
        }
    }
    while (!que.empty()) {
        int cy = que.front().first;
        int cx = que.front().second;
        que.pop();
        for (int dir = 0; dir < 4; dir++) {
            int ny = cy + dy[dir];
            int nx = cx + dx[dir];
            int nday = box[cy][cx]+1;
            if (ny >= height || nx >= width || ny < 0 || nx < 0) continue;
            if (box[ny][nx] == 0) {
                box[ny][nx] = nday;
                que.push(make_pair(ny, nx));
            }
        }
    }
}

int main(void) {
    init();
    bfs();
    int res = 0;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int tmp = box[y][x];
            if (tmp == -1) continue;
            if (tmp == 0) {
                printf("%d\n", -1);
                return 0;
            }
            if (tmp > res) {
                res = tmp;
                continue;
            }
        }
    }
    printf("%d\n", res-1);
    return 0;
}