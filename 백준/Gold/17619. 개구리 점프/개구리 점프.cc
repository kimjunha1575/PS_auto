#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

// 문제 링크
// https://www.acmicpc.net/problem/17619

// 통나무 N개 (가로 방향)
// 한 통나무에서 다른 통나무로 수직방향으로만 점프 가능
// 다른 통나무 위를 지날 수 없다

// 통나무 개수 N
// 질문의 개수 Q
// N개의 줄에 x1, x2, y
// Q개의 줄에 start, dest

// 통나무 개수 <= 100,000
// 질문 개수 <= 100,000

struct Log {
    int num;
    int x1, x2;

    bool operator<(Log l) const {
        if (x1 <= l.x1) {
            return false;
        }
        else if (x1 == l.x1) {
            return x2 < l.x2;
        }
        return true;
    }
};

int parent[100001];
int start[100001];
int dest[100001];
int N, Q;
priority_queue<Log> logs;

int Find(int n) {
    if (parent[n] == n) {
        return n;
    }
    else {
        return parent[n] = Find(parent[n]);
    }
}

void Union(int n1, int n2) {
    int p1 = Find(n1);
    int p2 = Find(n2);

    if (p1 != p2) {
        if (dest[p1] > dest[p2])
            parent[p2] = p1;
        else
            parent[p1] = p2;
    }
}

int main(void) {
    cin >> N >> Q;
    int num = 1;
    for (int i = 0; i < N; i++) {
        int x1, x2, y;
        cin >> x1 >> x2 >> y;
        parent[num] = num;
        start[num] = x1;
        dest[num] = x2;
        logs.push({num++, x1, x2});
    }

    // Union
    while (logs.size() > 1) {
        Log now = logs.top();
        logs.pop();
        // printf("now: {%d, %d, %d, %d}\n", now.num, now.x1, now.x2, now.y);

        Log next = logs.top();

        if (dest[Find(now.num)] >= start[next.num]) {
            Union(now.num, next.num);
        }
    }

    // Query
    for (int i = 0; i < Q; i++) {
        int start, dest;
        cin >> start >> dest;
        // print result

        if (Find(start) == Find(dest)) {
            cout << 1 << endl;
        }
        else {
            cout << 0 << endl;
        }
    }

    return 0;
}