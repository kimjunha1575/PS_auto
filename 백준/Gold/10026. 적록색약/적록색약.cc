#include <iostream>
#include <stack>
using namespace std;

int board_size;
int region_normal;
int region_colorblind;
int visited[100][100];
int board[100][100];
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};

void init() {
    cin >> board_size;
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            char tmp;
            cin >> tmp;
            if (tmp == 'R') board[r][c] = 2;
            else if (tmp == 'G') board[r][c] = 1;
            else if (tmp == 'B') board[r][c] = 0;
        }
    }
}

void clean() {
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            visited[r][c] = 0;
        }
    }
}

int bfs(int r, int c, int mode) {
    stack<pair<int, int>> stk;
    stk.push(make_pair(r, c));
    visited[r][c] = 1;
    while (!stk.empty()) {
        int cr = stk.top().first;
        int cc = stk.top().second;
        stk.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nr = cr + dr[dir];
            int nc = cc + dc[dir];
            if (nr < 0 || nc < 0 || nr >= board_size || nc >= board_size) continue;
            if (visited[nr][nc]) continue;
            if (mode) {
                if (board[nr][nc] != board[r][c]) continue;
            } else {
                if ((board[nr][nc] > 0) != (board[r][c] > 0)) continue;
            }
            visited[nr][nc] = 1;
            stk.push(make_pair(nr, nc));
        }
    }
    return 1;
}

int main(void) {
    init();
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            if (visited[r][c]) continue;
            region_normal += bfs(r, c, 1);
        }
    }
    clean();
    for (int r = 0; r < board_size; r++) {
        for (int c = 0; c < board_size; c++) {
            if (visited[r][c]) continue;
            region_colorblind += bfs(r, c, 0);
        }
    }
    printf("%d %d\n", region_normal, region_colorblind);
}
