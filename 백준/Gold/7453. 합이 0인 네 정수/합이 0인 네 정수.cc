#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int N;
vector<int> arr[4];
vector<int> v01, v23;

bool cmp(int a, int b) {
    return a > b;
}

void input() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 4; j++) {
            int tmp;
            cin >> tmp;
            arr[j].push_back(tmp);
        }
    }
    for (int i = 0; i < 4; i++)
        sort(arr[i].begin(), arr[i].end());
}


int main(void) {
    input();
    v01.clear();
    v23.clear();
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            v01.push_back(arr[0][i] + arr[1][j]);
            v23.push_back(arr[2][i] + arr[3][j]);
        }
    }
    sort(v01.begin(), v01.end());
    sort(v23.begin(), v23.end(), cmp);

    long long ans = 0;
    auto left = v01.begin();
    auto right = v23.begin();
    while (left != v01.end() && right != v23.end()) {
        if (*left + *right > 0)
            right++;
        else if (*left + *right < 0) {
            left++;
        }
        else {
            long long cnt_left = 0;
            long long value_left = *left;
            long long cnt_right = 0;
            int value_right = *right;
            while (*left == value_left && left != v01.end()) {
                cnt_left++;
                left++;
            }
            while (*right == value_right && right != v23.end()) {
                cnt_right++;
                right++;
            }
            ans += cnt_left * cnt_right;
        }
    }
    cout << ans;
}