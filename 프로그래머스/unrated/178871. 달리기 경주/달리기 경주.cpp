#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    unordered_map<string, int> get_rank;
    unordered_map<int, string> get_name;
    
    for (int i = 0; i < players.size(); i++) {
        get_rank.insert({players[i], i});
        get_name.insert({i, players[i]});
    }
    
    for (int i = 0; i < callings.size(); i++) {
        string callee = callings[i];
        int rank = get_rank[callee];
        //cout << rank << '\n';
        get_rank[callee]--;
        get_name[rank] = get_name[rank-1];
        get_rank[get_name[rank-1]]++;
        get_name[rank-1] = callee;
        
    }
    for (int i = 0; i < players.size(); i++) {
        answer.push_back(get_name[i]);
    }
    return answer;
}