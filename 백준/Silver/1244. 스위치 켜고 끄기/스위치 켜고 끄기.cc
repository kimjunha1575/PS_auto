#include <iostream>
using namespace std;

int N;
int switches[101];

int main(void) {
    cin >> N;
    for (int i = 1; i <= N; i++) cin >> switches[i];
    int students;
    cin >> students;
    for (int _ = 0; _ < students; _++) {
        int gender, num;
        cin >> gender >> num;
        if (gender == 1) {
            for (int j = 1; j <= N; j++)
                if (j % num == 0) switches[j] = 1 - switches[j];
        } else {
            switches[num] = 1 - switches[num];
            int idx = 1;
            while (num + idx <= N && num - idx >= 1 && switches[num+idx] == switches[num-idx]) {
                switches[num + idx] = 1 - switches[num + idx];
                switches[num - idx] = 1 - switches[num - idx];
                idx++;
            }
        }
    }
    for (int i = 1; i <= N; i++) {
        printf("%d ", switches[i]);
        if (i % 20 == 0) printf("\n");
    }
    printf("\n");
}


