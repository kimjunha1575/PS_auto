#include <iostream>
using namespace std;

// https://www.acmicpc.net/problem/10971

// 모든 vertex를 순회한 후, 출발지로 돌아오는 경로 중
// 비용이 최소인 경로를 찾아야 한다.

// 전략
// 1. 출발지와 연결된 vertex들에 대해 1번씩의 다익스트라(순회 후 돌아올 수 있어야 하므로)
// 2. 출발지까지 돌아오는 DFS (완전탐색) (~ 브루트 포스)

// 출발지가 조건으로 주어지는 경우, 1번이 훨씬 빠르겠으나,
// 출발지의 조건이 주이지지 않고, 맵 크기도 작으므로
// 평범한 완전탐색으로 작성.

// 도시의 수
int N;
// 인접행렬을 저장할 2차배열
int map[10][10];
// visited
int visited[10] = {0};

void input() {
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> map[i][j];
}

void initVisited() {
    for (int i = 0; i < N; i++)
        visited[i] = 0;
}

// st를 출발지로 하는 경로 중 최소비용을 구하는 dfs
void dfs(int now, int st, int cnt, int acc_cost, int *ans) {
    // printf("visited %d\n", now);
    int res = 0;
    if (now == st) {
        if (cnt == N + 1) {
            if (acc_cost < *ans) *ans = acc_cost;
            // printf("travel finished!\n");
            // printf("ans: %d\n", *ans);
            return;
        }
    }
    for (int i = 0; i < N; i++) {
        if (map[now][i] == 0) continue;
        if (visited[i] && i != st) continue;
        if (i == st && cnt < N) continue;
        if (i != st) visited[i] = 1;
        dfs(i, st, cnt + 1, acc_cost + map[now][i], ans);
        visited[i] = 0;
    }
}

int main(void) {
    input();
    int ans = 0x7FFFFFFF;
    for (int i = 0; i < N; i++) {
        initVisited();
        visited[i] = 1;
        dfs(i, i, 1, 0, &ans);
    }
    cout << ans;
}