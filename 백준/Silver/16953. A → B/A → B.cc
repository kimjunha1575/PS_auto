#include <iostream>
#include <queue>
using namespace std;

int solve(int start, int target) {
    queue<pair<int, int>> que;
    que.push({start, 1});

    while (not que.empty()) {
        int now = que.front().first;
        int cnt = que.front().second;
        // printf("now: %d\n", now);
        que.pop();

        if (now > target) {
            continue;
        }
        if (now == target) {
            return cnt;
        }

        int next;
        if (next < (0x7FFFFFFF / 2)) {
            next = now * 2;
            que.push({next, cnt + 1});
        }

        if (now < (0x7FFFFFFF / 10)) {
            next = now * 10 + 1;
            que.push({next, cnt + 1});
        }
    }
    return -1;
}

int main(void) {
    int a, b;
    cin >> a >> b;
    cout << solve(a, b);
}