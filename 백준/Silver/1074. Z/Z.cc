#include <iostream>
using namespace std;

int N, r, c;
int ans;
int units[16];

void calc(int N, int r, int c) {
    if (N == 0) {
        ans += 2*r + c;
        return;
    }
    int unit = units[N-1];
    int portion = unit * unit;
    if (r + 1 > unit && c + 1 > unit) {
        ans += 3 * portion;
        calc(N-1, r-unit, c-unit);
    } else if (r + 1 > unit) {
        ans += 2 * portion;
        calc(N-1, r-unit, c);
    } else if (c + 1 > unit) {
        ans += portion;
        calc(N-1, r, c-unit);
    } else {
        calc(N-1, r, c);
    }
}

int main(void) {
    cin >> N >> r >> c;
    int tmp = 1;
    for (int i = 0; i <= N; i++) {
        units[i] = tmp;
        tmp *= 2;
    }
    ans = 0;
    calc(N, r, c);
    printf("%d\n", ans);
}