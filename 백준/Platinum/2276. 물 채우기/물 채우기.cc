#include <iostream>
#include <queue>
using namespace std;

const int dy[] = {0, 1, 0, -1};
const int dx[] = {1, 0, -1, 0};
int height, width;
int dish[300][300];
int visited[300][300] = {0};
int ans = 0;

struct Point
{
    int y;
    int x;
    bool operator<(Point p) const
    {
        if (dish[y][x] <= dish[p.y][p.x])
            return false;
        return true;
    }
};

priority_queue<Point> pq;

void input()
{
    cin >> width >> height;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            cin >> dish[i][j];
            if (i == 0 || j == 0 || i == height - 1 || j == width - 1)
            {
                // 테두리만 pq에 push!
                pq.push((Point){i, j});
                visited[i][j] = 1;
            }
        }
    }
}

void DFS(int y, int x, int h)
{
    // printf("visited (%d,%d) / h = %d\n", y, x, h);
    // DFS를 pq에서 pop한 위치에서 시작하기 때문에
    // 시작점에서는 아무 작업도 하지 않는다!! (ny, nx로 새롭게 탐색된 점에서만 필요한 작업을 해주면 된다!)
    // (pq에서 pop된 위치는 항상 '테두리'이기 때문에!!!) (애초에 테두리만 push함)
    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= height || nx >= width)
            continue;
        if (visited[ny][nx])
            continue;
        visited[ny][nx] = 1;
        if (dish[ny][nx] > h)
        {
            // printf("pushed (%d,%d) to pq\n", ny, nx);
            // 새로운 테두리 발견하면 pq에 push
            pq.push((Point){ny, nx});
        }
        else
        {
            ans += h - dish[ny][nx];
            // printf("+ %d to ans(%d,%d)\n", h-dish[ny][nx], ny, nx);
            DFS(ny, nx, h);
        }
    }
}

int main(void)
// 가장 바깥쪽부터 테두리를 좁혀가면서 물을 채워나가는 방식!
// 테두리부터 pq에 넣어가면서 진행하기 때문에
// pq에서 pop된 노드보다 더 낮은 테두리는 없다! + 가장 바깥쪽 테두리는 이미 큐에 있기 때문에 visited!
// 따라서 DFS로 탐색했을 때, 탐색 출발점 높이보다 낮지만 물을 채울 수 없는 경우는 있을 수 없다! (가장 낮은 테두리가 pop되기 때문!!!)
//  >> DFS로 현재 노드보다 낮은 곳에 도착하면 그냥 물을 채워도 된다!! (더 높은 곳을 만나면 새로운 테두리로써 pq에 push 해준다!
// visited에는 그냥 물을 채운 곳도, 새롭게 찾은 테두리도 모두 마킹!
// 하지만 pq에는 테두리에 해당되는 곳만 push!
{
    input();
    while (!pq.empty())
    {
        Point now = pq.top();
        pq.pop();
        // printf("DFS started at (%d,%d), height = %d\n", now.y, now.x, dish[now.y][now.x]);
        // 현재 pq에 있는 테두리 노드 중 가장 낮은 노드 pop
        // 해당 노드에서 DFS 출발
        // 새로운 테두리 찾을경우 pq에 push되고
        // 물을 채울 수 있는 경우 채워준다.
        DFS(now.y, now.x, dish[now.y][now.x]);
        // printf("===============================\n\n");
    }
    printf("%d\n", ans);
    return 0;
}