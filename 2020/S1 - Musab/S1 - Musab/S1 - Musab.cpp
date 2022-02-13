#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>

using namespace std;

double findMaxS(map<int, int> &timeDist) {
    double max = 0;
    double temp;
    double temp1;
    double temp2;
    vector <int> keys;
    
    for (const auto &x : timeDist) {
        keys.push_back(x.first);
    }
    
    for (auto it = keys.begin(); it < keys.end()-1; it++) {
         temp1 = abs(timeDist[*it] - timeDist[*(it+1)]);
         temp2 = abs(*it - *(it + 1));
         //cout << temp1 <<" " << temp2 << "\n";
        temp = temp1/temp2;
         //cout << temp;
      if (temp > max) {
        max = temp;
      }
    }

    return max;
}

void takeInp(const int n, map<int, int> &logs) {
    int tempT;
    int tempD;
    for (int i = 1; i <= n; i++) {
        cin >> tempT;
        cin >> tempD;
        logs[tempT] = tempD;
    }
}

int main() {
    int n;
    cin >> n;
    map<int, int> timeDist;
    takeInp(n, timeDist);
    double max = findMaxS(timeDist);
    cout << max;
}

