#include <iostream>
using namespace std;

int M, n;
int y, x, dir;
pair<int, int> dirs[4] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};

int main(void) {
    cin >> M >> n;
    y = 0;
    x = 0;
    dir = 0;
    bool valid_command_set = true;
    for (int i = 0; i < n; i++) {
        string command;
        int param;
        cin >> command >> param;
        if (command == "MOVE") {
            y += param * dirs[dir].first;
            x += param * dirs[dir].second;
        } else if (param == 1) {
            dir = (dir + 1) % 4;
        } else {
            dir = (dir + 3) % 4;
        }
        if (y < 0 || x < 0 || y >= M || x >= M) {
            valid_command_set = false;
            break;
        }
    }
    if (valid_command_set) printf("%d %d\n", x, y);
    else printf("-1\n");
}