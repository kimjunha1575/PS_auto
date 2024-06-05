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
    for (int i = 0; i < 4; i++)
        if (n > tops[i])
            return i;
    return -1;
}
bool solve() {
    for (int i = 0; i < len; i++) {
        int tmp;
        cin >> tmp;
        int idx = findAvailableStack(tmp);
        if (idx >= 0) {
            stacks[idx].push(tmp);
            tops[idx] = tmp;
        } else {
            return false;
        }
    }
    return true;
}
int main(void) {
    init();
    if (solve()) cout << "YES";
    else cout << "NO";
    return 0;
}
