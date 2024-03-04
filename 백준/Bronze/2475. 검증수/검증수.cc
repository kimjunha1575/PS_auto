#include <iostream>
using namespace std;

int main(void) {
    int result = 0;
    for (int i = 0; i < 5; i++) {
        int tmp;
        cin >> tmp;
        tmp %= 10;
        result += (tmp * tmp) % 10;
    }
    cout << result % 10;
    return 0;
}