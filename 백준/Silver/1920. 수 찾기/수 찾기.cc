#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

// // 정수의 개수
// int N;
// // 찾을 수의 개수
// int M;
// // 정수를 저장할 배열
// int arr[100000];

// void input() {
//     cin >> N;
//     for (int i = 0; i < N; i++) cin >> arr[i];
//     cin >> M;
// }

// // binary search
// bool bs(int n) {
//     int left = 0;
//     int right = N-1;

//     while (left <= right) {
//         int mid = (left + right) / 2;
//         if (arr[mid] == n) return true;
//         else if (arr[mid] > n) right = mid - 1;
//         else if (arr[mid] < n) left = mid + 1;
//     }
//     return false;
// }

// int main(void) {
//     input();
//     sort(arr, arr + N);
//     for (int i = 0; i < M; i++) {
//         int target;
//         cin >> target;
//         if (bs(target)) cout << 1;
//         else cout << 0;
//         cout << "\n";
//     }
//     return 0;
// }

int N;
int M;
set<int> s;

int main(void) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int tmp;
        scanf("%d", &tmp);
        s.insert(tmp);
    }
    scanf("%d", &M);
    for (int i = 0; i < M; i++) {
        int tmp;
        scanf("%d", &tmp);
        if (s.find(tmp) != s.end()) {
            printf("1\n");
        }
        else printf("0\n");
    }
    return 0;
}