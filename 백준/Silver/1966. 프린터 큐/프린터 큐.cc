#include <iostream>
#include <queue>
using namespace std;

struct document {
    int value;
    bool isTarget;
    bool operator< (document O) const {
        return value < O.value;
    }
};

int N;
int M;
queue<document> que;
priority_queue<document> pq;

void init() {
    cin >> N >> M;
    que = queue<document>();
    pq = priority_queue<document>();
    for (int i = 0; i < N; i++) {
        int value;
        cin >> value;
        bool isTarget = (i == M);
        document tmp = {value, isTarget};
        que.push(tmp);
        pq.push(tmp);
    }
}
int solve() {
    int ans = 0;
    while (!que.empty()) {
        if (que.front().value < pq.top().value) {
            que.push(que.front());
            que.pop();
        } else {
            ans++;
            if (que.front().isTarget) {
                return ans;
            } else {
                que.pop();
                pq.pop();
            }
        }
    }
    return ans;
}
int main(void) {
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        init();
        cout << solve() << endl;
    }
    return 0;
}
