#include <iostream>
#include <stack>
using namespace std;

int board_size;
int region_normal;
int region_colorblind;
int visited_normal[100][100];
int visited_colorblind[100][100];
char board_normal[100][100];
char board_colorblind[100][100];
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};

void init() {
    cin >> board_size;
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            char tmp;
            cin >> tmp;
            board_normal[r][c] = tmp;
            if (tmp == 'R' || tmp == 'G') {
                board_colorblind[r][c] = 'R';
            } else {
                board_colorblind[r][c] = 'G';
            }
        }
    }
}

int bfs_normal(int r, int c) {
    stack<pair<int, int>> stk;
    stk.push(make_pair(r, c));
    visited_normal[r][c] = 1;
    char color = board_normal[r][c];
    while (!stk.empty()) {
        int cr = stk.top().first;
        int cc = stk.top().second;
        stk.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nr = cr + dr[dir];
            int nc = cc + dc[dir];
            if (nr < 0 || nc < 0 || nr >= board_size || nc >= board_size) continue;
            if (visited_normal[nr][nc]) continue;
            if (board_normal[nr][nc] != color) continue;
            visited_normal[nr][nc] = 1;
            stk.push(make_pair(nr, nc));
        }
    }
    return 1;
}

int bfs_colorblind(int r, int c) {
    stack<pair<int, int>> stk;
    stk.push(make_pair(r, c));
    visited_colorblind[r][c] = 1;
    char color = board_colorblind[r][c];
    while (!stk.empty()) {
        int cr = stk.top().first;
        int cc = stk.top().second;
        stk.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nr = cr + dr[dir];
            int nc = cc + dc[dir];
            if (nr < 0 || nc < 0 || nr >= board_size || nc >= board_size) continue;
            if (visited_colorblind[nr][nc]) continue;
            if (board_colorblind[nr][nc] != color) continue;
            visited_colorblind[nr][nc] = 1;
            stk.push(make_pair(nr, nc));
        }
    }
    return 1;
}

int main(void) {
    init();
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            if (visited_normal[r][c]) continue;
            region_normal += bfs_normal(r, c);
        }
    }
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            if (visited_colorblind[r][c]) continue;
            region_colorblind += bfs_colorblind(r, c);
        }
    }
    printf("%d %d\n", region_normal, region_colorblind);
}