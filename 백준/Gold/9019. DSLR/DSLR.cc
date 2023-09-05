#include <iostream>
#include <queue>
using namespace std;

struct INT {
    int value;
    string path;
};

// 어차피 한번 들른 수는 다시 안가
// visited에 어디서 왔는지, 무슨 연산으로 왔는지 기록하면?
// target > origin 순서로 넘어가면서 기록 복기 가능
// 해보자

struct History {
    int value;
    char command;
};

bool visited[10000];
History visited2[10000];

int D(int n) {
    return (2 * n) % 10000;
}

int S(int n) {
    if (n == 0) return 9999;
    return n - 1;
}

int L(int n) {
    return (n % 1000) * 10 + n / 1000;
}

int R(int n) {
    return (n / 10) + (n % 10) * 1000;
}

int BFS2(int ori, int target) {
    for (int i = 0; i < 10000; i++)
        visited2[i] = {-1, 0};
    queue<int> que;
    que.push(ori);
    visited2[ori] = {ori, 0};

    while (not que.empty()) {
        int now = que.front();
        que.pop();

        if (now == target) {
            return now;
        }

        // DSLR
        int tmp = D(now);
        if (visited2[tmp].value == -1) {
            visited2[tmp] = {now, 'D'};
            que.push(tmp);
        }

        tmp = S(now);
        if (visited2[tmp].value == -1) {
            visited2[tmp] = {now, 'S'};
            que.push(tmp);
        }

        tmp = L(now);
        if (visited2[tmp].value == -1) {
            visited2[tmp] = {now, 'L'};
            que.push(tmp);
        }

        tmp = R(now);
        if (visited2[tmp].value == -1) {
            visited2[tmp] = {now, 'R'};
            que.push(tmp);
        }
    }
    return -1;
}

string BFS(int ori, int target) {
    queue<INT> que;
    que.push({ori, ""});

    while (not que.empty()) {
        INT now = que.front();
        que.pop();
        visited[now.value] = true;

        if (now.value == target) {
            return now.path;
        }

        // DSLR
        int tmp = D(now.value);
        if (not visited[tmp]) que.push({tmp, now.path + "D"});

        tmp = S(now.value);
        if (not visited[tmp]) que.push({tmp, now.path + "S"});

        tmp = L(now.value);
        if (not visited[tmp]) que.push({tmp, now.path + "L"});

        tmp = R(now.value);
        if (not visited[tmp]) que.push({tmp, now.path + "R"});
    }
    return "failed";
}

int main(void) {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int ori, target;
        cin >> ori >> target;
        int ans2 = BFS2(ori, target);
        // cout << ans2 << "\n";
        string ans = "";
        while (ans2 != ori) {
            string tmp = "0";
            tmp[0] = visited2[ans2].command;
            // cout << tmp;
            ans += tmp;
            ans2 = visited2[ans2].value;
        }
        // cout << ans;
        for (int i = 0; i < ans.length(); i++) {
            cout << ans[ans.length()-1-i];
        }
        cout << "\n";
        // string ans = BFS(ori, target);
        // cout << "#" << test << " " << ans << "\n";
        // for (int i = 0; i < 10000; i++)
            // visited[i] = false;
    }
}