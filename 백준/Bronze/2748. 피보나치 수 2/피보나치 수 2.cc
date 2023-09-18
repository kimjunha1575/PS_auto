#include <iostream>
using namespace std;

// https://www.acmicpc.net/problem/2748

// 입력받는 n
int n;
// 피보나치 수를 저장할 수열 (일부 초기값 할당)
long long dp[100] = {0, 1, 1, };

long long solve(int n) {
    // 이미 알고있는 값이거나, n이 0인 경우 저장된 값을 반환
    if (dp[n] || n == 0) return dp[n];
    // 처음 계산하는 값의 경우, 재귀적으로 계산하여 배열에 저장 후 반환
    // 배열에 저장해놓음으로써 반복적으로 계산되지 않도록 함(DP)
    return dp[n] = solve(n-1) + solve(n-2);
}

int main(void) {
    cin >> n;
    cout << solve(n);
}