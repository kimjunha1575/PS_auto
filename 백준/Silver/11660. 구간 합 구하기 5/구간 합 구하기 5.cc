#include <iostream>
using namespace std;

struct Part {
    int x1, y1, x2, y2;
};

int N, M;
int board[1025][1025];
int acc[1025][1025];
Part queries[100000];

void init() {
    cin >> N >> M;
    for (int r = 1; r <= N; r++) {
        for (int c = 1; c <= N; c++) {
            cin >> board[r][c];
            acc[r][c] = board[r][c] + acc[r-1][c] + acc[r][c-1] - acc[r-1][c-1];
        }
    }
    for (int i = 0; i < M; i++) {
        int x1, y1, x2, y2;
        cin >> y1 >> x1 >> y2 >> x2;
        queries[i] = Part({x1, y1, x2, y2});
    }
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    init();
    for (int i = 0; i < M; i++) {
        Part query = queries[i];
        cout << acc[query.y2][query.x2] - acc[query.y1-1][query.x2] - acc[query.y2][query.x1-1] + acc[query.y1-1][query.x1-1] << '\n';
    }
}
