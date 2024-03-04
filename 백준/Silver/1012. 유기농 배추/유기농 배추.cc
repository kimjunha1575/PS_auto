#include <iostream>
using namespace std;

#define MAX_HEIGHT 50
#define MAX_WIDTH 50



int tc;
int height, width;
int cabbages;
int map[MAX_HEIGHT][MAX_WIDTH];
int visited[MAX_HEIGHT][MAX_WIDTH];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

void init();
void dfs(int y, int x);


int main(void) {
    cin >> tc;
    for (int test = 0; test < tc; test++) {
        init();
        int result = 0;
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                if (map[y][x] && visited[y][x] == 0) {
                    visited[y][x] = 1;
                    dfs(y, x);
                    result++;
                }
            }
        }
        cout << result << '\n';
    }
    return 0;
}

void init() {
    cin >> width >> height >> cabbages;
    for (int y = 0; y < height; y++)
        for (int x = 0; x < width; x++) {
            map[y][x] = 0;
            visited[y][x] = 0;
        }
    for (int i = 0; i < cabbages; i++) {
        int y, x;
        cin >> x >> y;
        map[y][x] = 1;
    }
}

void dfs(int y, int x) {
    for (int dir = 0; dir < 4; dir++) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];
        
        if (ny >= height || nx >= width || ny < 0 || nx < 0) continue;

        if (map[ny][nx] && visited[ny][nx] == 0) {
            visited[ny][nx] = 1;
            dfs(ny, nx);
        }   
    }
}