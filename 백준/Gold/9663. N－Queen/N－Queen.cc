#include <iostream>

using namespace std;

void recursion(int* count, int check_col[15], int check_ru[15], int check_lu[15], int n, int start) {
    if (start == n) (*count)++;
    else {
        for (int i = 0; i < n; i++) {
            if (check_col[i]) continue;
            if (check_ru[ (start + i) ]) continue;
            if (check_lu[ (start - i + 14)]) continue;

            check_col[i] = 1;
            check_ru[start + i] = 1;
            check_lu[start - i + 14] = 1;
            recursion(count, check_col, check_ru, check_lu, n, start + 1);
            check_lu[start - i + 14] = 0;
            check_ru[start + i] = 0;
            check_col[i] = 0;
        }
    }
}

int main() {
    int check_col[15] = {0};
    int check_ru[31] = {0};
    int check_lu[31] = {0};

    int res = 0;
    int n;
    cin >> n;
    recursion(&res, check_col, check_ru, check_lu, n, 0);
    cout << res;

    return 0;
}