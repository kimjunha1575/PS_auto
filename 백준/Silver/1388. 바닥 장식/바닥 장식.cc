#include <iostream>
#include <string>
using namespace std;

int width, height;
char map[50][50];
int visited[50][50];

void init() {
    cin >> height >> width;
    for (int y = 0; y < height; y++) {
        string tmp;
        cin >> tmp;
        for (int x = 0; x < width; x++) {
            map[y][x] = tmp[x];
            visited[y][x] = 0;
        }
    }

}

void prtMap() {
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            cout << map[y][x];
        }
        cout << "\n";
    }
}

void prtVisited() {
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            cout << visited[y][x];
        }
        cout << "\n";
    }
}

void dfs(int y, int x, char dir) {
    if (visited[y][x] || y >= height || x >= width) {
        return;
    }
    if (dir == '-') {
        visited[y][x] = 1;
        if (map[y][x+1] == '-')
            dfs(y, x+1, '-');
    }
    else {
        visited[y][x] = 1;
        if (map[y+1][x] == '|')
            dfs(y+1, x, '|');
    }
}

int main(void) {
    init();
    int result = 0;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (visited[y][x]) continue;
            result++;
            dfs(y, x, map[y][x]);
        }
    }
    cout << result;
    return 0;
}