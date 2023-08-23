#include <iostream>
using namespace std;

int res[80] = {0};

void prtArray(int arr[80]) {
    int i = 0;
    while (arr[i] && i <= 79) cout << arr[i++];
    cout << endl;
}

int isValid(int path[80], int now) {
    for (int len = 1; len <= (now+1)/2; len++) {
        int count = 0;

        for (int i = 0; i < len; i++) {
            if (path[(now+1)-(len*2)+i] == path[(now+1)-len+i]) count++;
        }
        
        if (count == len) {
            return 0;
        }
    }
    return 1;
}

int recursion(int arr[3], int path[80], int len, int now) {
    if ( now >= len ) { 
        prtArray(path);
        return 1;
    }
    else {
        for (int i = 0; i < 3; i++) {
            path[now] = arr[i];
            if ( isValid(path, now) == 0 ) {
                path[now] = 0;
                continue;
            }
            if (recursion(arr, path, len, now + 1)) return 1;
        }
    }
    return 0;
}


int main() {
    int len;
    int arr[3] = {1, 2, 3};
    int path[80] = {0};
    cin >> len;
    recursion(arr, path, len, 0);
    return 0;
}