#include <iostream>
#include <map>
#include <vector>

// using std::cout;
// using std::cin;
// using std::endl;
// using std::string;
// using std::map;

using namespace std;

int main() {

    
//     map<int, string> tempMap = {{1, "Apple",},
//                                 {2, "Banana",},
//                                 {3, "Mango",},
//                                 {4, "Raspberry",},
//                                 {5, "Blackberry",},
//                                 {6, "Cocoa",}};

//     for (const auto &item : tempMap) {
//         cout << "[" << item.first << "," << item.second << "]\n";
//     }
//     cout << endl;
//     return 0;
    vector<int> a{};
    a.push_back(2);
    a.push_back(3);
    a.push_back(4);
    a.push_back(5);

    for (auto const& x: a)
        cout << x << std::endl;
}