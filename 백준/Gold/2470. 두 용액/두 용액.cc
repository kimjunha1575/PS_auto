#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[100000];
int main(void) {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + N);
    int left = 0, right = N - 1;

    int best = 2000000000;
    int best_low, best_high;

    while (left < right) {
        int cur_sum = arr[left] + arr[right];
        if (abs(cur_sum) < abs(best)) {
            best = cur_sum;
            best_low = left;
            best_high = right;
        }

        if (cur_sum > 0)
            right--;
        else if (cur_sum < 0)
            left++;
        else
            break;
    }

    printf("%d %d\n", arr[best_low], arr[best_high]);

    // -99 -2 -1 4 98
    // 1 2 3 4 5 6
}