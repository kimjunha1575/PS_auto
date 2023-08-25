#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

struct Bus {
    int id;
    int start;
    int end;
    int pos;
    bool isVertical;
    bool visited;

    Bus(int id, int start, int end, int pos, bool isVertical, bool visited) : id(id), start(start), end(end), pos(pos), isVertical(isVertical), visited(visited) {
    }
};

int height, width, bus;
int ys, xs, yd, xd;
vector<Bus> buses[2][100001];

void input() {
    cin >> width >> height >> bus;
    for (int i = 0; i < bus; i++) {
        int b, x1, y1, x2, y2;
        cin >> b >> x1 >> y1 >> x2 >> y2;
        if (x1 == x2) {
            // vertical
            if (y1 < y2) {
                buses[1][x1].emplace_back(b, y1, y2, x1, true, false);
            }
            else
                buses[1][x1].emplace_back(b, y2, y1, x1, true, false);
        }
        else {
            // horizontal
            if (x1 < x2) {
                buses[0][y1].emplace_back(b, x1, x2, y1, false, false);
            }
            else
                buses[0][y1].emplace_back(b, x2, x1, y1, false, false);
        }
    }
    cin >> xs >> ys >> xd >> yd;
}

int BFS() {
    queue<pair<Bus, int>> que;

    // vertical
    for (int i = 0; i < buses[1][xs].size(); i++) {
        Bus cur = buses[1][xs][i];
        if (cur.start <= ys && ys <= cur.end) {
            // printf("xs:%d\ncur:start:%d\ncur.end:%d\n", xs, cur.start, cur.end);
            cur.visited = true;
            buses[1][xs][i].visited = true;
            // printf("%d is in starting point\n", cur.id);
            que.emplace(cur, 1);
        }
    }
    // horizontal
    for (int i = 0; i < buses[0][ys].size(); i++) {
        Bus cur = buses[0][ys][i];
        if (cur.start <= xs && xs <= cur.end) {
            cur.visited = true;
            buses[0][ys][i].visited = true;
            // printf("%d is in starting point\n", cur.id);
            que.emplace(cur, 1);
        }
    }

    while (!que.empty()) {
        Bus cur = que.front().first;
        int dist = que.front().second;
        que.pop();
        // printf("transferred to %d(%d)\n", cur.id, dist);

        if (cur.isVertical) {
            if (cur.pos == xd && cur.start <= yd && yd <= cur.end) return dist;
        }
        else {
            if (cur.pos == yd && cur.start <= xd && xd <= cur.end) return dist;
        }

        // cur: vertical
        if (cur.isVertical) {
            // next: vertical

            for (int i = 0; i < buses[1][cur.pos].size(); i++) {
                Bus next = buses[1][cur.pos][i];
                if (next.visited) continue;
                if (!(next.start > cur.end || next.end < cur.start)) {
                    next.visited = true;
                    buses[1][cur.pos][i].visited = true;
                    que.emplace(next, dist + 1);
                }
            }
            // next: horizontal
            for (int y = cur.start; y <= cur.end; y++) {
                for (int i = 0; i < buses[0][y].size(); i++) {
                    Bus next = buses[0][y][i];
                    if (next.visited) continue;
                    if (next.start <= cur.pos && cur.pos <= next.end) {
                        next.visited = true;
                        buses[0][y][i].visited = true;
                        que.emplace(next, dist + 1);
                    }
                }
            }
        }
        // cur: horizontal
        else {
            // next: vertical
            for (int x = cur.start; x <= cur.end; x++) {
                for (int i = 0; i < buses[1][x].size(); i++) {
                    Bus next = buses[1][x][i];
                    if (next.visited) continue;
                    if (next.start <= cur.pos && cur.pos <= next.end) {
                        next.visited = true;
                        buses[1][x][i].visited = true;
                        que.emplace(next, dist + 1);
                    }
                }
            }
            // next: horizontal
            for (int i = 0; i < buses[0][cur.pos].size(); i++) {
                Bus next = buses[0][cur.pos][i];
                if (next.visited) continue;
                if (!(next.start > cur.end || next.end < cur.start)) {
                    next.visited = true;
                    buses[0][cur.pos][i].visited = true;
                    que.emplace(next, dist + 1);
                }
            }
        }
    }
    return -1;
}

int main(void) {
    input();
    cout << BFS();
}