#include <iostream>
#include <stack>
using namespace std;

int N;
stack<int> st;

int main(void) {
    string ans = "+\n";
    int cur = 1;
    st.push(cur++);
    cin >> N;
    for (int i = 0; i < N; i++) {
        int tmp;
        cin >> tmp;
        if (st.empty() || tmp > st.top()) {
            do {
                st.push(cur++);
                ans += "+\n";
            } while (tmp > st.top());
            ans += "-\n";
            st.pop();
        } else if (tmp == st.top()) {
            ans += "-\n";
            st.pop();
        } else if (tmp < st.top()) {
            cout << "NO";
            return 0;
        }
    }
    cout << ans;
    return 0;
}