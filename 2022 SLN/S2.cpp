#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <unordered_map>
#include <set>

using namespace std;    

void buildMap(int X, unordered_map<string, vector<string>>& map) {
    for (int i{0}; i < X; i++) {
      string key;
      cin >> key;
      string val;
      cin >> val;
    //   if (map.count(val) > 0) { 
    //       if (map.at(val) == key) {} } else {      // prevent duplicates hopefully
    map[key].push_back(val);
    map[val].push_back(key);        // duplicates
            //   }
    }

}

int main() {
    int X, Y, G;
    int ans{0};
    unordered_map<string, vector<string>> mustWork;
    unordered_map<string, vector<string>> notWork;
    vector<array<string, 3>> groups;

    cin >> X;
    buildMap(X, mustWork);
    cin >> Y; 
    buildMap(Y, notWork);
    cin >> G;
    for (int i{0}; i < G; i++) {
      array<string, 3> temp;
      for (int j{0}; j < 3; j++) {
        string name;
        cin >> name;
        temp[j] = name;
      }
      groups.push_back(temp);
    }
    
    set<string> checkedNamesInX;  // has this name already been checked?
    set<string> checkedNamesInY;  // has this name already been checked?
    for (const auto& group: groups) {
        for (const auto& name: group) {     // loops over the group

            if (mustWork.count(name) > 0) { // if name is in map
                    for (int i{0}; i < int(mustWork[name].size()); i++) { //loops over the names arr in map
                    string personMustExist = mustWork[name][i]; // person that must be here
                    checkedNamesInX.insert(name);

                    if (checkedNamesInX.count(personMustExist) == 0) {  // if person has not been checked 
                    bool isPersonXThere{false};
                    for (int i{0}; i < 3; i++) {
                        if (group[i] == personMustExist) {    // is person there?
                            isPersonXThere = true;
                            break;
                        }
                    }
                    if (isPersonXThere == false) {
                        ans += 1;
                    }
                    }
                }
            }

                        if (notWork.count(name) > 0) { // if name is in map
                    for (int i{0}; i < int(notWork[name].size()); i++) { //loops over the names arr in map
                    string personMustNotExist = notWork[name][i]; // person that must not be here
                    checkedNamesInY.insert(name);

                    if (checkedNamesInY.count(personMustNotExist) == 0) {  // if person has not been checked 
                    bool isPersonYThere{false};
                    for (int i{0}; i < 3; i++) {
                        if (group[i] == personMustNotExist) {    // is person there?
                            isPersonYThere = true;
                            break;
                        }
                    }
                    if (isPersonYThere == true) {
                        ans += 1;
                    }
                    }
                }
            }
        }
    }

    cout << ans;
}
