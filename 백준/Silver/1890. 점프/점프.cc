#include <iostream>
using namespace std;

long long N;
long long board[100][100];
long long dp[100][100];

void init();
long long top_down(long long y, long long x);

int main(void) {
    init();
    cout << top_down(0, 0) << "\n";
    // for (long long i = 0; i < N; i++) {
    //     for (long long j = 0; j < N; j++) {
    //         prlong longf("%2d(%d) ", dp[i][j], board[i][j]);
    //     }
    //     prlong longf("\n");
    // }
            
    return 0;
}

void init() {
    cin >> N;
    for (long long i = 0; i < N; i++) {
        for (long long j = 0; j < N; j++) {
            cin >> board[i][j];
            dp[i][j] = -1;
        }
    }
}

long long top_down(long long y, long long x) {
    // 게임판을 벗어나면 0
    if (y >= N or x >= N) return 0;
    // 종점에 도착하면 1
    if (y == N-1 and x == N-1) return 1;
    // 종점이 아닌 이동거리가 0인 칸에 도착하면 0
    if (board[y][x] == 0) {
        dp[y][x] = 0;
        return dp[y][x];
    }

    // 이미 경로계산이 완료된 위치에서는 그대로 사용
    if (dp[y][x] >= 0) return dp[y][x];

    // 현재 칸에서의 이동거리
    long long value = board[y][x];

    // 현재 칸에서 
    long long down = 0;
    long long right = 0;

    if (y+value >= 0 and y+value < N)
        down = top_down(y+value, x);
    if (x+value >= 0 and x+value < N)
        right = top_down(y, x+value);
    dp[y][x] = down + right;
    return dp[y][x];
}

/*
 3  1  1  0
 3  1  0  0
 2  1  0  1
 1  1  1  0
*/
