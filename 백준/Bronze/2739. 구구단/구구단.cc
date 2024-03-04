#include <iostream>
using namespace std;

int N;

int main(void) {
    cin >> N;
    for (int i = 1; i <= 9; i++) {
        printf("%d * %d = %d\n", N, i, i * N);
    }
    return 0;
}
