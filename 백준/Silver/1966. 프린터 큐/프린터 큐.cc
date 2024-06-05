#include <iostream>
#include <queue>
using namespace std;

// https://www.acmicpc.net/problem/1966

// 타겟보다 중요도가 높은 문서의 개수의 총합 = a
// 타겟과 중요도가 같은 문서 중 타겟보다 먼저 출력되는 문서의 개수 = b
// a + b = 정답

struct document {
    int value;
    bool isTarget;
    bool operator< (document O) const {
        return value < O.value;
    }
};

// 문서 개수
int N;
// 타겟 문서의 현재 위치
int M;
// 타겟 문서의 중요도
int P;
// 동일 중요도 문서 중 타겟 문서의 현재 위치
int O;
// 입력된 문서 정보
int documents[100];
// 중요도 별 문서의 개수
int cnt[10];

// 배열 초기화, 입력값 저장
// 타겟 문서의 중요도와 같은 중요도를 가진 문서 중 몇 번째 순서인지 기록
void init() {
    for (int i = 0; i < 10; i++)
        cnt[i] = 0;
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        int tmp;
        cin >> tmp;
        documents[i] = tmp;
        cnt[tmp]++;
        if (i == M) {
            O = cnt[tmp];
            P = tmp;
        }
    }
}
// 각 테스트 케이스에 대해 정답 반환
int solve() {
    int ans = 0;
    queue<document> que;
    priority_queue<document> pq;
    for (int i = 0; i < N; i++) {
        int value = documents[i];
        bool isTarget = (i == M);
        document tmp = {value, isTarget};
        que.push(tmp);
        pq.push(tmp);
    }
    while (!que.empty()) {
        // cout << que.front().value << " " << que.front().isTarget << endl;
        // que.pop();

        if (que.front().value < pq.top().value) {
            que.push(que.front());
            que.pop();
            continue;
        } else {
            if (que.front().isTarget) {
                return ans + 1;
            } else {
                que.pop();
                pq.pop();
                ans++;
            }
        }
    }

    return ans;
}
int main(void) {
    queue<int> answer;
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        init();
        // cout << solve() << endl;
        answer.push(solve());
    }
    while (!answer.empty()) {
        cout << answer.front() << endl;
        answer.pop();
    }
    return 0;
}
