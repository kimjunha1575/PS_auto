#include <iostream>
using namespace std;

int K, N;
int len[10000];
int longest = 0;

void input() {
    cin >> K >> N;
    for (int i = 0; i < K; i++) {
        cin >> len[i];
        if (len[i] > longest) longest = len[i];
    }
}

bool Possible(int n) {
    int cnt = 0;
    for (int i = 0; i < K; i++) {
        cnt += len[i] / n;
        if (cnt >= N) return true;
    }
    return false;
}

long long binary_search() {
    long long left = 1;
    long long right = 0x7fffffff;

    while (left <= right) {
        long long mid = (left + right) / 2;
        if (Possible(mid)) left = mid + 1;
        else right = mid - 1;
    }

    if (right > 0) return right;
    else return left;
}


int main(void) {
    input();
    cout << binary_search();
}