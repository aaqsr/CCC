#include <iostream>
#include <string>
#include <vector>
#include <map>

// athletes want jerseys larger or same size with equal number

// this is a test function
void test() {
    std::map<std::string, bool> testMap{};
    std::unordered_map<std::string, bool> testMap2{};
    testMap["aaaa"] = true;
    testMap2["aaaaaaaa"]= true;
}

int main() {
    int J{0};
    int A{0};

    std::vector<char> shirts{'a'};
    std::cin >> J;
    std::cin >> A;

    test();

    for (int i{1}; i <= J; i++) {
        char temp{'a'};
        std::cin >> temp;
        shirts.push_back(temp);
    }
}
