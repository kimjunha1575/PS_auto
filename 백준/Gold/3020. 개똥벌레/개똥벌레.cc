#include <iostream>
#include <algorithm>
using namespace std;

int N, H; // N always even | 석순 -> 종유석 반복
int even[100000];
int odd[100000];
int cnt[500001];

int searchOdd(int height) { // height 이상인 모든 원소의 개수
    int left = 0;
    int right = N/2 - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (odd[mid] >= height) right = mid - 1;
        else left = mid + 1;
    }
    if (right < 0) return N/2;
    if (left >= N/2) return 0;
    return N/2 - (right + 1);
}

int searchEven(int height) { // height 이상인 모든 원소의 개수
    int left = 0;
    int right = N/2 - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (even[mid] >= height) right = mid - 1;
        else left = mid + 1;
    }
    if (right < 0) return N/2;
    if (left >= N/2) return 0;
    return N/2 - (right + 1);
}

pair<int, int> solve() {
    pair<int, int> result = {0x7FFFFFFF, 0};
    for (int h = 1; h <= H; h++) { // maximum 500000
        int crush = searchEven(h) + searchOdd(H - h + 1); // maximum < 40
        // cout << "crush(height:" << h << "): " << crush << endl;
        if (crush < result.first) {
            result.first = crush;
            result.second = 1;
        }
        else if (crush == result.first )
            result.second++;
    }
    return result;
}

void init() {
    cin >> N >> H;
    for (int i = 0; i < N; i++) {
        if (i%2 == 0) cin >> even[i/2];
        else cin >> odd[i/2];
    }
    sort(even, even + N/2);
    sort(odd, odd + N/2);
}

int main(void) {
    init();
    pair<int, int> result = solve();
    cout << result.first << " " << result.second << endl;
    return 0;
}

/*
1부터 50만까지의 높이 모두에 대해
10만개의 이분탐색 2번?

50만 * 20 * 2 ~= 2천만
*/

