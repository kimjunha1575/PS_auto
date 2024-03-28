#include <iostream>
#include <queue>
#include <functional>
using namespace std;

int N;
priority_queue<int, vector<int>, greater<int>> pos_pq; // minimum queue
priority_queue<int> neg_pq; // maximum queue

void pop_que() {
    if (pos_pq.empty() && neg_pq.empty()) {
        cout << "0\n";
        return;
    }
    else if (pos_pq.empty()) {
        cout << neg_pq.top() << "\n";
        neg_pq.pop();
        return;
    }
    else if (neg_pq.empty()) {
        cout << pos_pq.top() << "\n";
        pos_pq.pop();
        return;
    }
    int pos = pos_pq.top();
    int neg = neg_pq.top();
    if (pos + neg >= 0) {
        cout << neg << "\n";
        neg_pq.pop();
        return;
    }
    else {
        cout << pos << "\n";
        pos_pq.pop();
        return;
    }
}

void push_que(int input) {
    if (input > 0) pos_pq.push(input);
    else neg_pq.push(input);
}

int main(void) {
    cin >> N;
    for (int i = 0; i < N; i++) {
        int input;
        cin >> input;
        if (input == 0) {
            pop_que();
        }
        else {
            push_que(input);
        }
    }
    return 0;
}