/*
    number of gates 1-G
    number of planes 
    the max gate number the plane can dock at

    dock the plane at the max gate
*/

#include <iostream>
#include <set>
#include <vector>

using namespace std;

int planeCheck(int p, set<int>& gates, int& ans) {
    if (p < *gates.rend()) {
        p = *gates.rbegin();
    }
    while (gates.count(p) != 0) {
        p -= 1;
        if (p < 1) {
            cout << ans;
            return 1;
        }
    }
    ans += 1;
    gates.insert(p);
    return 0;
}

int main() {
    int G{0};
    int P{0};
    vector<int> planes;
    set<int> gates;
    int ans{0};

    cin >> G;
    cin >> P;

    for (int i{0}; i < P; i++){
        int temp;
        cin >> temp;
        planes.push_back(temp);
    }

    for (const auto& p : planes) {
      int temp2 = planeCheck(p, gates, ans);
      if (temp2 == 1) {
        break;
      }
    }
}