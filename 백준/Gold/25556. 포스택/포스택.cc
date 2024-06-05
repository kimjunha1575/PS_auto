#include <iostream>
#include <stack>
#include <string>
using namespace std;

int len;
int tops[4];
stack<int> stacks[4];

void init() {
    for (int i = 0; i < 4; i++) tops[i] = 0;
    cin >> len;
}
int findAvailableStack(int n) {
    for (int i = 0; i < 4; i++) {
        if (n > tops[i])
            return i;
    }
    return -1;
}
int main(void) {
    init();
    int prev;
    int cnt = 0;
    for (int i = 0; i < len; i++) {
        int tmp;
        cin >> tmp;
        if (i) {
            int idx = findAvailableStack(tmp);
            if (idx >= 0) {
                stacks[idx].push(tmp);
                tops[idx] = tmp;
            } else {
                cout << "NO\n";
                return 0;
            }
        } else {
            stacks[0].push(tmp);
            tops[0] = tmp;
            cnt++;
        }
        prev = tmp;
    }
    cout << "YES\n";
    return 0;
}
