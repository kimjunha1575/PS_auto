#include <iostream>
#include <queue>
#include <set>
using namespace std;

struct Node {
    int in;
    vector<int> to;
};

vector<Node> nodes;

struct cmp {
    bool operator()(const int& a, const int& b) const {
        if (nodes[a].in < nodes[b].in)
            return true;
        if (nodes[a].in == nodes[b].in)
            return a < b;
        return false;
    } 
};

int N, M;
set<int, cmp> probSet;

void checkSet() {
    for (auto it = probSet.begin(); it != probSet.end(); it++) {
        printf("%d(%d) ", *it, nodes[*it].in);
    }
    cout << "\n";
}

int main(void) {
    // freopen("input.txt", "rt", stdin);
    cin >> N >> M;
    nodes.resize(N + 1);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        nodes[b].in++;
        nodes[a].to.emplace_back(b);
    }
    for (int i = 1; i <= N; i++) {
        probSet.emplace(i);
    }
    while (!probSet.empty()) {
        int curNum = *probSet.begin();
        cout << curNum << " ";
        Node& curNode = nodes[curNum];
        probSet.erase(curNum);
        for (int i = 0; i < curNode.to.size(); i++) {
            int nxt = curNode.to[i];
            probSet.erase(nxt);
            nodes[nxt].in--;
            probSet.emplace(nxt);
        }
    }
    return 0;
}