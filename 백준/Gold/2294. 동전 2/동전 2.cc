#include <iostream>
using namespace std;

// https://www.acmicpc.net/problem/2294

// 동전의 가지수
int cntCoin;
// 만들어야 할 가치
int target;
// 동전의 종류
int coins[101];
// dp[n]: n원을 최소 몇 개의 동전으로 만들 수 있는지
int dp[200000];

void input() {
    scanf("%d %d", &cntCoin, &target);
    for (int i = 1; i <= cntCoin; i++) {
        scanf("%d\n", &coins[i]);
    }
}

void solve(int cnt, int worth) {
    if (worth > target) return;
    dp[worth] = cnt;
    // printf("dp[%d] = %d\n", worth, cnt);
    for (int i = 1; i <= cntCoin; i++) {
        int next = worth + coins[i];
        if (dp[next] == 0 || (dp[next] && dp[next] > cnt + 1)) solve(cnt + 1, next);
    }
}

int main(void) {
    input();
    solve(0, 0);
    int ans = dp[target];
    if (ans)
        printf("%d", ans);
    else
        printf("-1");
}
