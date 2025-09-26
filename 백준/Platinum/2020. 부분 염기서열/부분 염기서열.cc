#include <iostream>
#include <map>
#include <vector>
#include <queue>
using namespace std;

int n, m, K;
string order;
map<char, vector<int>> idxMap;


int main(void) {
    // freopen("input.txt", "rt", stdin);
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> K;
    cin >> order;
    for (int i = 0; i < order.length(); i++) {
        idxMap[order[i]].emplace_back(i);
    }
    queue<vector<int>> q;
    for (auto it = idxMap.begin(); it != idxMap.end(); it++) {
        q.emplace(it->second);
    }
    int len = 1;
    int cnt = 0;
    string ans;
    while (!q.empty()) {
        int qSize = q.size();
        for (int i = 0; i < qSize; i++) {
            vector<int> cand = q.front();
            q.pop();
            if (cand.size() < m) continue;
            if (++cnt == K)
                ans = order.substr(cand[0], len);
            map<char, vector<int>> idxMap2;
            for (int j = 0; j < (int)cand.size(); j++) {
                int stIdx = cand[j];
                if (stIdx + len >= n) continue;
                idxMap2[order[stIdx  + len]].emplace_back(stIdx);
            }
            for (auto it = idxMap2.begin(); it != idxMap2.end(); it++) {
                q.emplace(it->second);
            }
        }
        len++;
    }
    cout << cnt << "\n" << ans;
    return 0;
}
