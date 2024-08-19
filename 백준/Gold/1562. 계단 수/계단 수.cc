#include <iostream>
using namespace std;

int N;
int dp[100][10][1 << 10];

int main(void) {
    cin >> N;
    for (int i = 0; i < 10; i++) {
        dp[0][i][1 << i] = 1;
    }
    for (int n = 0; n < N-1; n++) {
        for (int i = 0; i < 10; i++) {
            for (int used = 0; used < 1 << 10; used++) {
                if (i < 9) {
                    dp[n+1][i+1][used | (1 << (i+1))] += dp[n][i][used];
                    dp[n+1][i+1][used | (1 << (i+1))] %= 1000000000;
                }
                if (i > 0) {
                    dp[n+1][i-1][used | (1 << (i-1))] += dp[n][i][used] % 1000000000;
                    dp[n+1][i-1][used | (1 << (i-1))] %= 1000000000;
                }
            }
        }
    }
    int ans = 0;
    for (int i = 1; i < 10; i++) {
        ans += dp[N-1][i][(1 << 10) - 1];
        ans %= 1000000000;
    }
    printf("%d\n", ans);
}