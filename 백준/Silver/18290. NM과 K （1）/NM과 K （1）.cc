#include <iostream>
#include <vector>
using namespace std;

int N, M, K;
int board[10][10];
int visited[10][10];
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};
int ans = 0x80000000;

void init() {
    cin >> N >> M >> K;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cin >> board[r][c];
        }
    }
}

void solve(int acc, int cnt, int row, int col) {
    if (cnt == K) {
        if (acc > ans) {
            ans = acc;
        }
        return;
    }
    for (int r = 0; r < N; r++) {
        if (r < row) continue;
        for (int c = 0; c < M; c++) {
            if (r == row && c < col) continue;
            if (visited[r][c]) continue;
            vector<pair<int, int>> tmp;
            for (int dir = 0; dir < 4; dir++) {
                int nr = r + dr[dir];
                int nc = c + dc[dir];
                if (nr < 0 || nc < 0 || nr >= N || nc >= M) continue;
                if (visited[nr][nc] == 0) tmp.push_back({nr, nc});
                visited[nr][nc] = 1;
            }   
            visited[r][c] = 1;
            solve(acc + board[r][c], cnt + 1, r, c);
            visited[r][c] = 0;
            for (int i = 0; i < (int)tmp.size(); i++) {
                visited[tmp[i].first][tmp[i].second] = 0;
            }
        }
    }
}

int main(void) {
    init();
    solve(0, 0, 0, 0);
    printf("%d\n", ans);
}