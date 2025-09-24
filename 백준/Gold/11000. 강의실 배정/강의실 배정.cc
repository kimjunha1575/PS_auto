#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N;
vector<pair<int, int>> lectures;
priority_queue<int, vector<int>, greater<int>> rooms;


int cmp(pair<int, int>& a, pair<int, int>& b) {
    if (a.first < b.first)
        return true;
    if (a.first == b.first)
        return a.second < b.second;
    return false;
}

int main(void) {
    // freopen("input.txt", "rt", stdin);
    cin >> N;
    lectures.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> lectures[i].first >> lectures[i].second;
    }
    sort(lectures.begin(), lectures.end(), cmp);
    rooms.emplace(lectures[0].second);
    for (int i = 1; i < N; i++) {
        if (lectures[i].first >= rooms.top())
            rooms.pop();
        rooms.emplace(lectures[i].second);
    }
    cout << rooms.size();
}