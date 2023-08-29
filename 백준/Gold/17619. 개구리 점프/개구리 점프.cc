#include <iostream>
#include <queue>
using namespace std;

struct Log {
    int start;
    int end;
    int y;
    int id;

    // Log(int start, int end, int y, int id) : start(start), end(end), y(y), id(id) {
    // }

    bool operator<(Log l) const {
        if (start < l.start)
            return false;
        else if (start == l.start && y <= l.y)
            return false;
        return true;
    }
};

int parent[100001];
Log logs[100001];
priority_queue<Log> pq;
int N, Q;

void input() {
    cin >> N >> Q;
    for (int i = 1; i <= N; i++) {
        int start, end, y;
        cin >> start >> end >> y;
        pq.push({start, end, y, i});
        parent[i] = i;
        logs[i].start = start;
        logs[i].end = end;
        logs[i].y = y;
        logs[i].id = i; 
    }
}

int Find(int n) {
    if (parent[n] == n)
        return n;
    else
        return parent[n] = Find(parent[n]);
}

void Union(int n1, int n2) {
    int r1 = Find(n1);
    int r2 = Find(n2);
    parent[r2] = r1;
}

int main(void) {
    input();
    while (pq.size() > 1) {
        Log cur = pq.top();
        pq.pop();

        Log next = pq.top();

        if (logs[Find(cur.id)].end >= next.start /*&& cur.y != next.y*/) {
            if (logs[Find(cur.id)].end > next.end)
                Union(cur.id, next.id);
            else
                Union(next.id, cur.id);
            // printf("can move to %d to %d\n", cur.id, next.id);
            // printf("%d.end: %d\n%d.start: %d\n", cur.id, cur.end, next.id, next.start);
        }
    }
    for (int i = 0; i < Q; i++) {
        int n1, n2;
        cin >> n1 >> n2;
        if (Find(n1) == Find(n2))
            printf("1\n");
        else
            printf("0\n");
    }
}