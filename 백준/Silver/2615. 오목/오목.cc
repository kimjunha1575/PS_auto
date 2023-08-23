#include <iostream>
using namespace std;

int successive(int board[19][19], int y, int x) {
    int dy[] = {-1, 0, 1, 1};
    int dx[] = {1, 1, 1, 0};
    int color = board[y][x];

    // 인수로 받은 칸을 포함해서 오목이 완성되어 있는지 검사
    // 오른쪽, 아래쪽, 오른아래쪽만 검사해도됨 ㅋㅋ
    for (int i = 0; i < 4; i++) {
        if (board[y-dy[i]][x-dx[i]] == color) continue;
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

int check(int board[19][19], int* y, int* x) {
    int res;
    for (int i = 0; i < 19; i++) {
        for (int j = 0; j < 19; j++) {
            res = successive(board, i, j);
            if (res) {
                *y = i;
                *x = j;
                return res;
            }
        }
    }
    return 0;
}

int main() {
    int board[19][19];
    for (int i = 0; i < 19; i++) for (int j = 0; j < 19; j++) cin >> board[i][j];

    int y, x;
    int winner = check(board, &y, &x);

    
    if (winner) printf("%d\n%d %d", winner, y+1, x+1);
    else cout << winner;
    return 0;

}