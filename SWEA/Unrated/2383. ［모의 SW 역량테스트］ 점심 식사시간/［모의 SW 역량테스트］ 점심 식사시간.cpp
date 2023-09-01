#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX_MAP_SIZE 10

struct Person {
    int id;
    int d0;
    int d1;
    pair<int, int> pos;
};

struct Stair {
    int len;
    pair<int, int> pos;
};

bool cmp0(Person a, Person b) {
    return a.d0 < b.d0;  // 오름차순
}

bool cmp1(Person a, Person b) {
    return a.d1 < b.d1;
}

int N;
int cntPeople;
int map[MAX_MAP_SIZE][MAX_MAP_SIZE];
vector<Person> people;
vector<Stair> stairs;
int stairSelection[MAX_MAP_SIZE];
int ans = 0x7FFFFFFF;
int dp[MAX_MAP_SIZE];

void input() {
    cntPeople = 0;
    ans = 0x7FFFFFFF;
    cin >> N;
    int id = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
            if (map[i][j] == 1) people.push_back({id++, 0, 0, {i, j}});
            if (map[i][j] > 1) stairs.push_back({map[i][j], {i, j}});
        }
    }
    cntPeople = people.size();
}

void getDist() {
    for (int i = 0; i < people.size(); i++) {
        for (int st = 0; st < 2; st++) {
            if (st == 0) {
                people[i].d0 = abs(stairs[st].pos.first - people[i].pos.first) + abs(stairs[st].pos.second - people[i].pos.second);
            }
            else {
                people[i].d1 = abs(stairs[st].pos.first - people[i].pos.first) + abs(stairs[st].pos.second - people[i].pos.second);
            }
        }
    }
}

void DFS(int idx) {
    // printf("idx: %d\n", idx);
    if (idx >= people.size()) {
        // 모든 인원의 계단 선택이 완료
        vector<Person> st0, st1;
        int time0, time1;

        // 각 계단으로 배치 후 계단 도착 시간에 대해 오름차순으로 정렬
        for (int i = 0; i < cntPeople; i++) {
            if (stairSelection[i]) {
                st1.push_back(people[i]);
            }
            else
                st0.push_back(people[i]);
        }
        sort(st0.begin(), st0.end(), cmp0);
        sort(st1.begin(), st1.end(), cmp1);
        // printf("sort\n");

        // 각 계단에 대해
        for (int i = 0; i < st0.size(); i++) {
            // 사용자가 3명 이하인 경우 대기시간 고려 없이 계산
            if (i < 3) {
                dp[i] = st0[i].d0 + stairs[0].len + 1;
            }
            // 계단 사용자가 4명 이상인 경우 대기시간 고려하여 계산
            else {
                if (dp[i - 3] <= st0[i].d0)
                    dp[i] = st0[i].d0 + stairs[0].len + 1;
                else
                    dp[i] = dp[i - 3] + stairs[0].len;
            }
        }
        time0 = dp[st0.size()-1];

        // 다른 계단에 대해서 동일과정 수행
        for (int i = 0; i < st1.size(); i++) {
            if (i < 3) {
                dp[i] = st1[i].d1 + stairs[1].len + 1;
            }
            else {
                if (dp[i - 3] <= st1[i].d1)
                    dp[i] = st1[i].d1 + stairs[1].len + 1;
                else
                    dp[i] = dp[i - 3] + stairs[1].len;
            }
        }
        time1 = dp[st1.size()-1];

        // printf("dp\n");
        // 두 계단 중 늦게 완료되는 계단의 최종 완료시간을 기준으로 정답 갱신
        int res = max(time0, time1);
        if (ans > res) ans = res;

        // 작업 완료되면 return
        return;
    }
    // 계단 선택
    for (int st = 0; st < 2; st++) {
        stairSelection[idx] = st;
        DFS(idx + 1);
    }
}

int main(void) {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        input();
        getDist();
        DFS(0);
        printf("#%d %d\n", test, ans);
        people.clear();
        stairs.clear();
    }
}
