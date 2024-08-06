#include <iostream>
#include <algorithm>
using namespace std;

int innings;
int predictions[50][9];
int hit_order[9];
int hit[9];
int ans;
int cur_idx;

int calc() {
    int point = 0;
    cur_idx = 0;
    for (int i = 0; i < innings; i++) {
        int out_count = 0;
        int runners[3] = {0, 0, 0};
        while (out_count < 3) {
            int cur_hitter = predictions[i][hit_order[cur_idx]];
            switch (cur_hitter) {
                case 0:
                    out_count++;
                    break;
                case 1:
                    if (runners[2]) {
                        point++;
                        runners[2] = 0;
                    }
                    if (runners[1]) {
                        runners[2] = 1;
                        runners[1] = 0;
                    }
                    if (runners[0]) runners[1] = 1;
                    runners[0] = 1;
                    break;
                case 2:
                    if (runners[2]) {
                        point++;
                        runners[2] = 0;
                    }
                    if (runners[1]) point++;
                    if (runners[0]) runners[2] = 1;
                    runners[1] = 1;
                    runners[0] = 0;
                    break;
                case 3:
                    if (runners[2]) point++;
                    if (runners[1]) point++;
                    if (runners[0]) point++;
                    runners[0] = 0;
                    runners[1] = 0;
                    runners[2] = 1;
                    break;
                case 4:
                    if (runners[2]) point++;
                    if (runners[1]) point++;
                    if (runners[0]) point++;
                    point++;
                    runners[0] = 0;
                    runners[1] = 0;
                    runners[2] = 0;
                    break;
            }
            cur_idx = (cur_idx + 1) % 9;
        }
    }
    return point;
}

void solve(int idx) {
    if (idx == 3) {
        hit_order[idx] = 0;
        solve(idx + 1);
    }
    if (idx == 9) {
        cur_idx = 0;
        ans = max(ans, calc());
        return;
    }
    for (int i = 1; i < 9; i++) {
        if (hit[i]) continue;
        hit[i] = 1;
        hit_order[idx] = i;
        solve(idx + 1);
        hit[i] = 0;
    }
}

int main(void) {
    cin >> innings;
    for (int i = 0; i < innings; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> predictions[i][j];
        }
    }
    solve(0);
    printf("%d\n", ans);
}
