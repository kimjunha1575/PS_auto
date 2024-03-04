#include <iostream>

int N;

int main(void) {
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = N-i-1; j > 0; j--) {
            printf(" ");
        }
        for (int k = N-i; k <= N; k++) {
            printf("*");
        }
        printf("\n");
    }


}