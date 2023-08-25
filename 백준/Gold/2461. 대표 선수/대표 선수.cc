#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

struct Represent {
    int value;
    int belong;

    bool operator<(Represent r) const {
        if (value <= r.value) return false;
        return true;
    }
};

priority_queue< Represent > pq;
vector< int > students[1000];
int indeces[1000] = {0};
int N, M;

int input() {
    int ans = 1000000000;
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int tmp;
            cin >> tmp;
            students[i].push_back(tmp);
        }
        sort(students[i].begin(), students[i].end());
    }
    int max = 0;
    for (int i = 0; i < N; i++) {
        pq.push((Represent){students[i][0], i});
        if (students[i][0] > max) max = students[i][0];
    }
    return max;
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int max = input();
    int cur;
    int ans = 1000000000;
    while (true) {
        int min = pq.top().value;
        int min_class = pq.top().belong;
        pq.pop();

        cur = max - min;
        if (ans > cur) ans = cur;

        indeces[min_class]++;
        int new_value = students[min_class][indeces[min_class]];
        pq.push((Represent){new_value, min_class});

        // tracking max value
        if (new_value > max) max = students[min_class][indeces[min_class]];
        if (indeces[min_class] >= M) break;
    }
    cout << ans;
}