#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
unsigned long long waiting[100000];

bool isPossible(unsigned long long n) {
    unsigned long long sum = 0;
    for (int i = 0; i < N; i++) {
        sum += n / waiting[i];
        // sum의 오버플로우가 일어날 수 있으니 바로바로 체크
        if (sum >= M) return true;
    }
    return false;
}

int main(void) {
    cin >> N >> M;
    for (int i = 0; i < N; i++)
        cin >> waiting[i];
    sort(waiting, waiting + N);

    unsigned long long left = 1;
    unsigned long long right = 1e18;

    while (left <= right) {
        unsigned long long mid = (left + right) / 2;
        if (isPossible(mid))
            right = mid - 1;
        else
            left = mid + 1;
    }
    if (left > 1e18) left = 1e18;
    cout << left;
}