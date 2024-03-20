#include <iostream>
using namespace std;

int N, K;
int values[10];

void init(void);
int solve();

int main(void) {
    init();
    cout << solve();
}

void init(void) {
    cin >> N >> K;
    for (int i = 0; i < 10; i++) {
        cin >> values[i];
    }
}

int solve() {
    int res = 0;
    while (K) {
        while (K >= values[N-1]) {
            K -= values[N-1];
            res++;
        }
        N--;
    }
    return res;
}