#include <iostream>
using namespace std;

int N, K;
int objects[101][2]; // [0]: 무게, [1]: 가치
int dp[100001];

int main(void) {
    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        int w, v;
        cin >> w >> v;
        for (int j = K; j >= w; j--) {
            dp[j] = max(dp[j-w] + v, dp[j]);
        }
    }
    cout << dp[K];
    return 0;
}
