#include <iostream>
using namespace std;

int N, M;
int board[1025][1025];
int acc[1025][1025];
pair<pair<int, int>, pair<int, int>> queries[100000];

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
        cin >> x1 >> y1 >> x2 >> y2;
        queries[i] = make_pair(make_pair(x1, y1), make_pair(x2, y2));
    }
}

int main(void) {
    init();
    for (int i = 0; i < M; i++) {
        pair<pair<int, int>, pair<int, int>> query = queries[i];
        printf("%d\n", acc[query.second.first][query.second.second] - acc[query.first.first-1][query.second.second] - acc[query.second.first][query.first.second-1] + acc[query.first.first-1][query.first.second-1]);
    }
}
