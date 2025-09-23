#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

int board[25][25];
int visited[25][25];
int boardSize;
vector<int> houseCnt;

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};


int dfs_stack(int row, int col) {
    int cnt = 0;
    stack<pair<int, int>> st;
    st.emplace(row, col);
    visited[row][col] = 1;
    while (!st.empty()) {
        int cr = st.top().first;
        int cc = st.top().second;
        st.pop();
        cnt++;
        for (int dir = 0; dir < 4; dir++) {
            int nr = cr + dr[dir];
            int nc = cc + dc[dir];
            if (nr < 0 || nr >= boardSize || nc < 0 || nc >= boardSize) continue;
            if (visited[nr][nc]) continue;
            if (board[nr][nc] == 0) continue;
            st.emplace(nr, nc);
            visited[nr][nc] = 1;
        }
    }
    return cnt;
}

int dfs_recursion(int row, int col);


int main(void) {
    // freopen("input.txt", "rt", stdin);
    cin >> boardSize;
    for (int i = 0; i < boardSize; i++) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < boardSize; j++) {
            board[i][j] = tmp[j] - '0';
        }
    }
    int totalCnt = 0;
    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < boardSize; j++) {
            if (visited[i][j]) continue;
            if (board[i][j] == 0) continue;
            // houseCnt.emplace_back(dfs_recursion(i, j));
            totalCnt++;
            houseCnt.emplace_back(dfs_stack(i, j));
        }
    }
    sort(houseCnt.begin(), houseCnt.end());
    cout << totalCnt << endl;
    for (int i = 0; i < houseCnt.size(); i++) {
        cout << houseCnt[i] << endl;
    }
    return 0;
}