#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

#define MAX_STAIR_LENGTH 500 

int N;
int score[MAX_STAIR_LENGTH] = {0};
int dp[MAX_STAIR_LENGTH] = {0};

void input() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> score[i];
    }
}

int DFS(int n) {
    if (n < 0) return 0;
    if (n == 0) return score[0];
    if (dp[n]) return dp[n];

    int maxScore = -2e9;
    maxScore = max(DFS(n - 2), maxScore);
    maxScore = max(DFS(n - 3) + score[n - 1], maxScore);

    dp[n] = score[n] + maxScore;
    return dp[n];
}

int main(void) {
    input();
    cout << DFS(N-1);
}