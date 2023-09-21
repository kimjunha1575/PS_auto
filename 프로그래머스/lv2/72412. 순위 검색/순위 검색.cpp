#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> answer;
set<string> keys;
unordered_map<string, vector<int>> db;
void addParticipant(string);
int searchParticipant(string);
stringstream stream;

vector<int> solution(vector<string> info, vector<string> query) {
    answer.clear();
    db.clear();
    for (string i : info) 
        addParticipant(i);
    for (string key : keys)
        sort(db[key].begin(), db[key].end());
    for (string q : query) 
        answer.push_back(searchParticipant(q));
    return answer;
}

int searchParticipant(string str) {
    string lang, major, career, food;
    string dummy;
    int score;
    stream.str(str + "\n");
    stream >> lang >> dummy >> major >> dummy >> career >> dummy >> food >> score;
    string key = "";
    dummy = "-";
    if (lang != dummy) key += lang;
    if (major != dummy) key += major;
    if (career != dummy) key += career;
    if (food != dummy) key += food;
    if (db.find(key) == db.end()) return 0;

    vector<int> scores = db[key];
    int len = scores.size();
    
    int left = 0;
    int right = len - 1;

    if (scores[left] >= score) return len;
    if (scores[right] < score) return 0;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        if (scores[mid] < score) left = mid + 1;
        else right = mid - 1;
    }
    return len - left;
}

void addParticipant(string str) {
    string lang, major, career, food;
    int score;
    stream.str(str + "\n");
    stream >> lang >> major >> career >> food >> score;
    for (int l = 0; l < 2; l++) {
        for (int m = 0; m < 2; m++) {
            for (int c = 0; c < 2; c++) {
                for (int f = 0; f < 2; f++) {
                    string key = "";
                    if (l) key += lang;
                    if (m) key += major;
                    if (c) key += career;
                    if (f) key += food;
                    db[key].push_back(score);
                    keys.insert(key);
                }
            }
        }
    }
}
