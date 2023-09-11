#include <iostream>
#include <queue>
using namespace std;

// 문제 링크
// https://www.acmicpc.net/problem/17619

// 통나무 N개 (가로 방향)
// 한 통나무에서 다른 통나무로 수직방향으로만 점프 가능
// 다른 통나무 위를 지날 수 없다 << 이걸 모르겠네

// 통나무 개수 N
// 질문의 개수 Q
// N개의 줄에 x1, x2, y
// Q개의 줄에 start, dest

// 통나무 개수 <= 100,000
// 질문 개수 <= 100,000

struct Log {
    int num;
    int x1, x2, y;

    bool operator<( Log l ) const {
        // ascending ordering with x1 (start point)
        if (x1 < l.x1) {
            return false;
        }
        else if (x1 == l.x1) {
            if (x2 < l.x2) {
                return false;
            }
            else if (x2 == l.x2) {
                return y < l.y;
            }
        }
        return true;
    }
};

int parent[100001];

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
        parent[p1] = p2;
    }
}

int N, Q;
priority_queue<Log> logs;

int main(void) {
    cin >> N >> Q;
    int num = 1;
    for (int i = 0; i < N; i++) {
        int x1, x2, y;
        cin >> x1 >> x2 >> y;
        parent[num] = num;
        logs.push({num++, x1, x2, y});
        
    }

    // Union Find task
    while (not logs.empty()) {
        Log now = logs.top();
        logs.pop();

        int num = now.num;
        int x1 = now.x1;
        int x2 = now.x2;
        int y = now.y;

        Log next = logs.top();

        if (next.x1 <= x2 && next.y != y) {
            Union(num, next.num);
            // printf("Union %d, %d\n", num, next.num);
        }
    }


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