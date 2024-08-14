#include <iostream>
using namespace std;

int N, M;
int parent[1000001];
int level[1000001];


int Find(int p) {
    if (parent[p] != p) parent[p] = Find(parent[p]);
    return parent[p];
}

void Union(int p, int q) {
    int pp = Find(p);
    int pq = Find(q);
    if (level[pp] <= level[pq]) {
        parent[pq] = pp;
        level[pq]++;
    }
    else {
        parent[pq] = pp;
        level[pp]++;
    }
}

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;
    for (int i = 0; i <= N; i++) {
        parent[i] = i;
        level[i] = 1;
    }
    for (int i = 0; i < M; i++) {
        int command, p, q;
        cin >> command >> p >> q;
        if (command) {
            if (Find(p) == Find(q)) cout << "YES\n";
            else cout << "NO\n";
        } else {
            Union(p, q);
        }
    }
}