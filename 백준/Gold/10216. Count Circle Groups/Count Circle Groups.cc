#include <iostream>
#include <algorithm>
using namespace std;

// 통신탑의 커버 범위가 넓은 곳을 부모로 하여 union
// cnt 배열 만들어서 그룹 개수 리턴.
struct Tower
{
    int y;
    int x;
    int range;
    bool operator==(Tower p)
    {
        if (y == p.y && x == p.x)
            return true;
        return false;
    }
};
vector<Tower> towers;
int parent[3001];

int Find(int n)
{
    if (parent[n] == n)
        return n;
    return parent[n] = Find(parent[n]);
}

void Union(int n1, int n2)
{
    int p1 = Find(n1);
    int p2 = Find(n2);
    parent[p2] = p1;
}

bool isReachable(int a, int b, int r)
{
    if (a * a + b * b <= r * r)
        return true;
    return false;
}

int main(void)
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        towers.clear();
        int N;
        cin >> N;
        int ans = 0;
        for (int j = 0; j < N; j++)
        {
            int y, x, r;
            cin >> x >> y >> r;
            Tower new_tower = {y, x, r};
            parent[j] = j;
            towers.push_back(new_tower);
            ans++;
        }
        for (int j = 0; j < N - 1; j++)
        {
            for (int k = j + 1; k < N; k++)
            {
                if (isReachable(abs(towers[j].y - towers[k].y), abs(towers[j].x - towers[k].x), abs(towers[j].range + towers[k].range)))
                {
                    if (Find(j) != Find(k))
                    {
                        // printf("union %d, %d\n", j, k);
                        Union(j, k);
                        ans--;
                    }
                }
            }
        }
        printf("%d\n", ans);
    }
}