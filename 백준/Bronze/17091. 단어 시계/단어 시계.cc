#include <iostream>
using namespace std;

int H, M;
string minutes[] =
        {"o' clock",
         "one minute",
         "two minutes",
         "three minutes",
         "four minutes",
         "five minutes",
         "six minutes",
         "seven minutes",
         "eight minutes",
         "nine minutes",
         "ten minutes",
         "eleven minutes",
         "twelve minutes",
         "thirteen minutes",
         "fourteen minutes",
         "quarter",
         "sixteen minutes",
         "seventeen minutes",
         "eighteen minutes",
         "nineteen minutes",
         "twenty minutes",
         "twenty one minutes",
         "twenty two minutes",
         "twenty three minutes",
         "twenty four minutes",
         "twenty five minutes",
         "twenty six minutes",
         "twenty seven minutes",
         "twenty eight minutes",
         "twenty nine minutes",
         "half"};
string hours[] = {"twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"};

int main(void) {
    cin >> H >> M;
    string hour;

    if (M > 30) {
        hour = hours[(H + 1) % 12];
    }
    else {
        hour = hours[H % 12];
    }

    if (M > 30) {
        cout << minutes[60 - M] << " to " << hour << "\n";
    }
    else if (M == 0) {
        cout << hour << " o' clock\n";
    }
    else {
        cout << minutes[M] << " past " << hour << "\n";
    }
}