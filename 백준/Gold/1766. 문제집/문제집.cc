#include <iostream>
#include <queue>
#include <set>
using namespace std;

priority_queue<int, vector<int>, greater<int>> cand;
int N, M;
vector<int> cnt;
vector<vector<int>> to;

int main(void) {
    // freopen("input.txt", "rt", stdin);
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M;
    cnt.resize(N + 1, 0);
    to.resize(N + 1);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        cnt[b]++;
        to[a].emplace_back(b);
    }
    for (int i = 1; i <= N; i++) {
        if (cnt[i] == 0) {
            cand.emplace(i);
        }
    }
    while (!cand.empty()) {
        int cur = cand.top();
        cand.pop();
        cout << cur << " ";
        for (int i = 0; i < to[cur].size(); i++) {
            if (--cnt[to[cur][i]] == 0) {
                cand.emplace(to[cur][i]);
            }
        }
    }
    return 0;
}
