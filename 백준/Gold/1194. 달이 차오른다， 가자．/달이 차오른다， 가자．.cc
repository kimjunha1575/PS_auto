#include <iostream>
#include <queue>
using namespace std;

struct Pos {
    int r;
    int c;
    int d;
    int keys;

    Pos(const int r, const int c, const int d, const int keys): r(r), c(c), d(d), keys(keys) {}
};

constexpr char EMPTY = '.';
constexpr char WALL = '#';
constexpr char EXIT = '1';
constexpr int DIRECTIONS[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int height = 0;
int width = 0;
int sr = 0;
int sc = 0;
char map[50][50] = {};
bool visited[50][50][1<<6] = {};
bool keys[6] = {};

void init() {
    cin >> height >> width;
    for (int r = 0; r < height; r++) {
        string tmp;
        cin >> tmp;
        for (int c = 0; c < width; c++) {
            if (tmp[c] == '0') {
                sr = r;
                sc = c;
                map[r][c] = EMPTY;
            } else {
                map[r][c] = tmp[c];
            }
        }
    }
}

int bfs() {
    int init_key = 0;
    for (int i = 0; i < 6; i++) {
        if (keys[i]) init_key |= 1 << i;
    }
    queue<Pos> que;
    que.emplace(sr, sc, 0, init_key);
    visited[sr][sc][init_key] = true;
    while (not que.empty()) {
        const auto& [cr, cc, cd, ck] = que.front(); que.pop();
        if (map[cr][cc] == EXIT)
            return cd;
        for (const auto& [dr, dc] : DIRECTIONS) {
            const int nr = cr + dr;
            const int nc = cc + dc;
            const int nd = cd + 1;
            int nk = ck;
            if (nr < 0 || nc < 0 || nr >= height || nc >= width) continue;
            if (map[nr][nc] == WALL) continue;
            if (visited[nr][nc][ck]) continue;
            if (map[nr][nc] >= 'a' and map[nr][nc] <= 'f') {
                nk = ck | 1 << map[nr][nc] - 'a';
                que.emplace(nr, nc, nd, nk);
                visited[nr][nc][nk] = true;
                continue;
            }
            if (visited[nr][nc][nk]) continue;
            if (map[nr][nc] == EMPTY or map[nr][nc] == EXIT) {
                que.emplace(nr, nc, nd, ck);
                visited[nr][nc][nk] = true;
            } else if (map[nr][nc] >= 'A' and map[nr][nc] <= 'F') {
                if (ck & 1 << map[nr][nc] - 'A') {
                    que.emplace(nr, nc, nd, ck);
                    visited[nr][nc][nk] = true;
                }
            }
        }
    }
    return -1;
}

int main() {
    init();
    cout << bfs();
    return 0;
}
