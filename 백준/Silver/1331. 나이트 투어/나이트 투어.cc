#include <iostream>
using namespace std;

int board[6][6];
int dr[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dc[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int r, c;
int sr, sc;
int pr, pc;

int main(void) {
    int is_valid_tour = 1;
    string move;
    cin >> move;
    sr = move[0] - 'A';
    sc = move[1] - '1';
    board[sr][sc] = 1;
    pr = sr;
    pc = sc;
    for (int i = 0; i < 35; i++) {
        string move;
        cin >> move;
        r = move[0] - 'A';
        c = move[1] - '1';
        if (board[r][c]) {
            is_valid_tour = 0;
            break;
        }
        for (int j = 0; j < 8; j++) {
            if (r - pr == dr[j] && c - pc == dc[j]) {
                is_valid_tour = 1;
                break;
            } else is_valid_tour = 0;
        }
        if (!is_valid_tour) break;
        board[r][c] = 1;
        pr = r;
        pc = c;
    }
    if (is_valid_tour) {
        for (int i = 0; i < 8; i++) {
            if (r - sr == dr[i] && c - sc == dc[i]) {
                is_valid_tour = 1;
                break;
            } else is_valid_tour = 0;
        }
    }
    if (is_valid_tour) printf("Valid\n");
    else printf("Invalid\n");
}