#include <iostream>
using namespace std;

#define MAX_HEIGHT 1000
#define MAX_WIDTH 1000

int height, width;
char map[MAX_HEIGHT][MAX_WIDTH];
int visited[MAX_HEIGHT][MAX_WIDTH];
int dy[4] = {0, 1, 0, -1}; // R D L U
int dx[4] = {1, 0, -1, 0};

bool dfs(int y, int x, int cnt);
void init();

int main(void) {
    init();
    int result = 0;
    int cnt = 1;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (visited[y][x]) continue;
            visited[y][x] = cnt;
            if (dfs(y, x, cnt))
                result++;
            cnt++;
        }
    }
    cout << result;
}

void init() {
    cin >> height >> width;
    for (int y = 0; y < height; y++) {
        string tmp;
        cin >> tmp;
        for (int x = 0; x < width; x++) {
            map[y][x] = tmp[x];
            visited[y][x] = 0;
        }
    }
}

bool dfs(int y, int x, int cnt) {
    int dir;
    if (map[y][x] == 'U') dir = 3;
    else if (map[y][x] == 'D') dir = 1;
    else if (map[y][x] == 'L') dir = 2;
    else dir = 0;

    int ny = y + dy[dir];
    int nx = x + dx[dir];

    if (visited[ny][nx] > 0 && visited[ny][nx] < cnt) return false;
    else if (visited[ny][nx] == cnt) return true;

    visited[ny][nx] = cnt;
    return dfs(ny, nx, cnt);
}
