#include <cstdio>
using namespace std;

// https://www.acmicpc.net/problem/2606

int map[101][101];
int visited[101];
int N;
int M;
int ans = 0;

void input() {
    scanf("%d%d", &N, &M);
    for (int i = 0; i < M; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        map[a][b] = 1;
        map[b][a] = 1;
    }
}

void dfs(int now) {
    for (int i = 1; i <= N; i++) {
        if (i == now) continue;
        if (visited[i]) continue;
        if (map[now][i] == 0) continue;
        visited[i] = 1;
        ans++;
        dfs(i);
    }
}

int main(void) {
    input();
    visited[1] = 1;
    dfs(1);
    printf("%d\n", ans);
}