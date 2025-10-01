#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool isPrime(long long target) {
    if (target == 1) return false;
    for (long long i = 2; i * i <= target; i++) {
        if (target % i == 0) return false;
    }
    return true;
}

int solution(int n, int k) {
    int answer = 0;
    
    vector<int> target;
    target.resize(20, 0);
    while (n > 0) {
        int power = 0;
        int tmp = 1;
        while (n >= tmp * k) {
            power++;
            tmp *= k;
        }
        n -= tmp;
        target[power]++;
    }
    
    string targetString;
    for (int i = 0; i < (int)target.size(); i++) {
        int curDigit = target[i];
        targetString.insert(0, to_string(curDigit));
    }
    
    int len = 0;
    vector<pair<int, int>> candidates;
    for (int i = 0; i < targetString.length(); i++) {
        if (targetString[i] == '0') {
            if (len) {
                candidates.emplace_back(i - len, len);
                len = 0;
            }
        } else {
            len++;
        }
    }
    if (len) {
        candidates.emplace_back(targetString.length() - len, len);
    }
    
    for (int i = 0; i < candidates.size(); i++) {
        int targetIndex = candidates[i].first;
        int length = candidates[i].second;
        string tmp = targetString.substr(targetIndex, length);
        if (isPrime(stoll(tmp))) answer++;
    }
    
    return answer;
}