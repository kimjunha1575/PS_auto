#include <iostream>
#include <vector>
using namespace std;

int V;
vector<pair<int, int>> tree[100001];
vector<int> edges[100001];
int visited[100001];

void init() {
    cin >> V;
    for (int i = 0; i < V; i++) {
        int st, en, weight;
        cin >> st;
        while (true) {
            cin >> en;
            if (en > 0) {
                cin >> weight;
                tree[st].push_back(make_pair(en, weight));
            }
            else break;
        }
    }
}

int search(int vertex, int cur_acc, int prev_weight) {
    // printf("visited %d\n", vertex);
    edges[vertex].push_back(cur_acc);
    bool is_edge = true;
    for (int i = 0; i < tree[vertex].size(); i++) {
        pair<int, int> next = tree[vertex][i];
        int next_vertex = next.first;
        int next_weight = next.second;
        if (visited[next_vertex]) continue;
        is_edge = false;
        visited[next_vertex] = 1;
        edges[vertex].push_back(search(next_vertex, cur_acc + next_weight, next_weight));
    }
    if (is_edge) {
        edges[vertex].clear();
        edges[vertex].push_back(prev_weight);
        return prev_weight;
    }
    else {
        // return max value of edges[vertex]
        int max = 0;
        for (int i = 1; i < edges[vertex].size(); i++) {
            int tmp = edges[vertex][i];
            if (tmp > max) max = tmp;
        }
        // printf("vertex: %d, max:%d, prev_weight:%d\n", vertex, max, prev_weight);
        return max + prev_weight;
    }
}


int main(void) {
    init();
    visited[1] = 1;
    search(1, 0, 0);
    int max = 0;
    for (int i = 1; i < V+1; i++) {
        int buf1 = 0;
        int buf2 = 0;
        // printf("%d:", i);
        for (int j = 0; j < edges[i].size(); j++) {
            int tmp = edges[i][j];
            // printf("%d, ", tmp);
            if (tmp > buf1) {
                if (buf1 > buf2) {
                    buf2 = buf1;
                }
                buf1 = tmp;
            } else if (tmp > buf2) {
                buf2 = tmp;
            }
        }
        if ((buf1 + buf2) > max) max = buf1 + buf2;
        // printf("\n");
    }
    printf("%d\n", max);
}