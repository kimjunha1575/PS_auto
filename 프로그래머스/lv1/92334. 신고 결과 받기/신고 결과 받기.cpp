#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    map<string, set<string>> cntReported;
    map<string, set<string>> reports;
    stringstream stream;
    for (string user_id : id_list) {
        cntReported.insert({user_id, {}});
        reports.insert({user_id, {}});
    }
    for (string report_log : report) {
        stream.str(report_log + "\n");
        string from, to;
        stream >> from >> to;
        reports[from].insert(to);
        cntReported[to].insert(from);
    }
    vector<int> answer;
    for (string user : id_list) {
        int tmp = 0;
        for (string reported_user : reports[user]) {
            if (cntReported[reported_user].size() >= k) tmp++;
        }
        answer.push_back(tmp);
    }
    return answer;
}