#include <iostream>
using namespace std;

int N, target;
int board[1000][1000];
int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, 1, 0, -1};
int tr, tc;


int main(void) {
    cin >> N >> target;
    int cur = N * N;
    int r = 0;
    int c = 0;
    int dir = 0;
    while (cur) {
        board[r][c] = cur;
        if (cur == target) {
            tr = r;
            tc = c;
        }
        cur--;
        int nr = r + dr[dir];
        int nc = c + dc[dir];
        if (nr >= 0 && nc >= 0 && nr < N && nc < N && board[nr][nc] == 0) {
            r = nr;
            c = nc;
        } else {
            dir = (dir + 1) % 4;
            r += dr[dir];
            c += dc[dir];
        }
    }
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            printf("%d ", board[r][c]);
        }
        printf("\n");
    }
    printf("%d %d\n", tr + 1, tc + 1);
}