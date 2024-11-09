#include <iostream>
#include <queue>
using namespace std;

struct Pos {
    const int r, c, s, d;
    Pos(const int& r, const int& c, const int& s, const int& d): r(r), c(c), s(s), d(d) {}
};

void init();
int solve();
int get_unit(const int& r, const int& c);
vector<Pos> get_next_positions(const int& r, const int& c, const int& cs, const int& d);
pair<int, int> get_rotated_pos(int r, int c, const int& s);

queue<Pos> que;
char map[500][500];
int visited[500][500];
int directions[5][2] = {{0, 0}, {0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int sr, sc;
int map_size;

void init() {
    cin >> map_size;
    for (int r = 0; r < map_size * 4; r++) {
        string tmp;
        cin >> tmp;
        for (int c = 0; c < map_size * 4; c++) {
            if (tmp[c] == 'S') {
                map[r][c] = '.';
                sr = r;
                sc = c;
            } else map[r][c] = tmp[c];
        }
    }
}

int get_unit(const int &r, const int &c) {
    return (r / 4) * map_size + c / 4;
}


pair<int, int> get_rotated_pos(int r, int c, const int& s) {
    const int row_ofs = 4 * (r / 4);
    const int col_ofs = 4 * (c / 4);
    r %= 4;
    c %= 4;
    switch (s) {
        case 0:
            return {r + row_ofs, c + col_ofs};
        case 1:
            return {c + row_ofs, (3 - r) + col_ofs};
        case 2:
            return {(3 - r) + row_ofs, (3 - c) + col_ofs};
        case 3:
            return {(3 - c) + row_ofs, r + col_ofs};
        default:
            return {-1, -1};
    }
}

vector<Pos> get_next_positions(const int& r, const int& c, const int& cs, const int& d) {
    vector<Pos> next_positions;
    const int curr_unit = get_unit(r, c);
    const auto& [cr, cc] = get_rotated_pos(r, c, cs);
    for (const auto& [dr, dc] : directions) {
        const int nr = cr + dr;
        const int nc = cc + dc;
        if (nr < 0 || nc < 0 || nr >= 4 * map_size || nc >= 4 * map_size) continue;
        const int next_unit = get_unit(nr, nc);
        int ns;
        if (next_unit == curr_unit) {
            ns = (cs + 1) % 4;
            const auto& [orig_r, orig_c] = get_rotated_pos(nr, nc, (4 - cs) % 4);
            if (visited[orig_r][orig_c] & 1 << ns) continue;
            if (map[orig_r][orig_c] == '#') continue;
            next_positions.emplace_back(orig_r, orig_c, ns, d + 1);
        } else {
            ns = 1;
            if (visited[nr][nc] & 1 << ns) continue;
            if (map[nr][nc] == '#') continue;
            next_positions.emplace_back(nr, nc, ns, d + 1);
        }
    }
    return next_positions;
}

int solve() {
    que.emplace(sr, sc, 0, 0);
    visited[sr][sc] |= 1 << 0;
    while (not que.empty()) {
        const auto& [cr, cc, cs, cd] = que.front();
        que.pop();
        if (map[cr][cc] == 'E') return cd;
        vector<Pos> next_positions = get_next_positions(cr, cc, cs, cd);
        for (const auto& [nr, nc, ns, nd] : next_positions) {
            que.emplace(nr, nc, ns, nd);
            visited[nr][nc] |= 1 << ns;
        }
    }
    return -1;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    init();
    cout << solve();
    return 0;
}
