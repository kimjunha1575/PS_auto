#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int tree_size;
vector<int> tree[100001];
int parents[100001];
int visited[100001];

void recursion(int idx) {
    for (int i = 0; i < tree[idx].size(); i++) {
        int node = tree[idx][i];
        if (visited[node]) continue;
        visited[node] = 1;
        parents[node] = idx;
        recursion(node);
    }
}

void loop(int root) {
    queue<int> que;
    que.push(root);
    while (!que.empty()) {
        int node = que.front();
        que.pop();
        visited[node] = 1;
        for (int i = 0; i < tree[node].size(); i++) {
            int next_node = tree[node][i];
            if (visited[next_node]) continue;
            que.push(next_node);
            parents[next_node] = node;
        }
    }
}

void init() {
    cin >> tree_size;
    for (int i = 0; i < tree_size - 1; i++) {
        int from, to;
        cin >> from >> to;
        tree[from].push_back(to);
        tree[to].push_back(from);
    }
}


int main(void) {
    init();
    // recursion(1);
    loop(1);
    for (int i = 2; i <= tree_size; i++) {
        printf("%d\n", parents[i]);
    }
    return 0;
}
