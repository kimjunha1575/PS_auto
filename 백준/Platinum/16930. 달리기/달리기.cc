#include <iostream>
#include <queue>
using namespace std;

void init();
int solve();

constexpr int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};


int height = 0;
int width = 0;
int gap = 0;
char map[1000][1000] = {};
int visited[1000][1000] = {};
int sr = 0;
int sc = 0;
int er = 0;
int ec = 0;

void init() {
    cin >> height >> width >> gap;
    for (int r = 0; r < height; r++) {
        for (int c = 0; c < width; c++) {
            cin >> map[r][c];
        }
    }
    cin >> sr >> sc >> er >> ec;
    sr--;
    sc--;
    er--;
    ec--;
}

int solve() {
    queue<pair<int, int>> que;
    que.emplace(sr, sc);
    visited[sr][sc] = 1;
    while (not que.empty()) {
        const auto [cr, cc] = que.front(); que.pop();
        if (cr == er && cc == ec)
            return visited[cr][cc] - 1;
        for (const auto& [dr, dc] : dirs) {
            for (int m = 1; m <= gap; m++) {
                const int nr = cr + dr * m;
                const int nc = cc + dc * m;
                if (nr < 0 || nc < 0 || nr >= height || nc >= width) break;
                if (map[nr][nc] == '#') break;
                if (visited[nr][nc] > 0 && visited[nr][nc] <= visited[cr][cc]) break;
                if (visited[nr][nc] > 0 && visited[nr][nc] == visited[cr][cc] + 1) continue;
                que.emplace(nr, nc);
                visited[nr][nc] = visited[cr][cc] + 1;
            }
        }
    }
    return -1;
}


int main() {
    init();
    cout << solve();
    return 0;
}