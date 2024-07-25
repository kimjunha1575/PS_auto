#include <iostream>
using namespace std;

int dy[] = {-1, 0, 1, 1};
int dx[] = {1, 1, 1, 0};
int board[19][19];
int win_y;
int win_x;

int successive(int y, int x) {
    int color = board[y][x];
    for (int i = 0; i < 4; i++) {
        int py = y - dy[i];
        int px = x - dx[i];
        if (py >= 0 && px >= 0 && py < 19 && px < 19 && board[py][px] == color) continue;
        int ny = y;
        int nx = x;
        int count = 1;
        for (int j = 0; j < 6; j++) {
            ny += dy[i];
            nx += dx[i];
            if (ny >= 0 && nx >= 0 && ny < 19 && nx < 19) {
                if (board[ny][nx] == color) {
                    count++;
                }
                else break;
            }
        }
        if (count == 5) return color;
        
    }
    return 0;
}

int check() {
    for (int i = 0; i < 19; i++) {
        for (int j = 0; j < 19; j++) {
            int res = successive(i, j);
            if (res) {
                win_y = i;
                win_x = j;
                return res;
            }
        }
    }
    return 0;
}

int main() {
    for (int i = 0; i < 19; i++) for (int j = 0; j < 19; j++) cin >> board[i][j];
    int winner = check();
    if (winner) printf("%d\n%d %d", winner, win_y+1, win_x+1);
    else cout << 0;
    return 0;
}
