#include <iostream>
#include <string>
#include <array>
#include <map>

using namespace std;

// array<int, 127> countChar(string str) {
//     array<int, 127> charArr{0};

//     for (int i = 0; i < str.size(); ++i)
//     {
//         char current = str[i];
//         int temp = int(current);
//         ++charArr[int(current)];
//     }

//     return charArr;
// }

map<char, int> countChar(string str) {
    map<char, int> charMap{};

    for (int i; i < str.size(); i++) {
        if (str[i] != '*') 
            charMap[str[i]]++;
    }

    return charMap;
}

int main() {
    string mainstr{};
    string anagram{};
    bool flag{true};

    cin >> mainstr;
    cin >> anagram;

    map<char, int> mainChars = countChar(mainstr);
    map<char, int> anaChars = countChar(anagram);

    
    if (mainstr.size() == anagram.size()) {
        map<char, int>::iterator iter;
        for (iter = anaChars.begin(); iter != anaChars.end(); iter++) {
            if ( mainChars[iter->first] < anaChars[iter->first] ) {
                flag = false;
                break;
            }
        }
    } else {
        flag = false;
    }

    
    // array<int, 127> mainCount = countChar(mainstr);
    // array<int, 127> anaCount = countChar(anagram);

    // for (int i{97}; i <= 127; i++) {
    //     if (&mainCount[i] < &anaCount[i]) {
    //         flag = !flag;
    //         break;
    //     }
    // }

    flag ? cout << "A" : cout << "N";


}

