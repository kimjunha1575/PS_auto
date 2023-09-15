#include <iostream>
using namespace std;

// https://www.acmicpc.net/problem/2629

// 아래 블로그 게시물 참고하여 풀이하였음.
// https://cocoon1787.tistory.com/360

// 추의 개수 ( <= 30)
int N;
// 추 무게 저장할 배열(오름차순으로 주어진다)(추의 무게 <= 500)
int weights[31];
// 무게를 확인할 구슬의 개수( <= 7)
int Q;
// 구슬들의 무게를 저장할 배열(구슬의 무게 <= 40000)
int marbles[7];
// dp[a][b]: a번까지의 추로 b의 무게를 만들 수 있는 지 여부를 저장.
bool dp[31][40001];

void input() {
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> weights[i];
    cin >> Q;
    for (int i = 0; i < Q; i++)
        cin >> marbles[i];
}

void solve(int cnt, int weight) {
    // cnt가 추의 개수를 넘어가거나 이미 가능한 무게에 대해서는 재귀 중단.
    if (cnt > N || dp[cnt][weight]) return;
    dp[cnt][weight] = true;
    solve(cnt + 1, weight);
    solve(cnt + 1, abs(weight - weights[cnt]));
    solve(cnt + 1, weight + weights[cnt]);
}

// 무게가 n인 구슬의 무게를 확인
bool isPossible(int n) {
    for (int i = 1; i <= N; i++) {
        if (dp[i][n]) return true;
    }
    return false;
}

int main(void) {
    input();
    solve(0, 0);
    for (int i = 0; i < Q; i++) {
        if (isPossible(marbles[i]))
            printf("Y ");
        else
            printf("N ");
    }
    return 0;
}