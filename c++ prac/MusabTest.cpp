#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


int main(){
    std::vector<int> a{};
    int n;
    int q;
    int k;
    int t;
    a.push_back(2);
    // std::cout << a[0];

    std::vector<bool> booltest{0};
    for (int i{0}; i < 5; i++) {
      char temp;
      std::cin >> temp;
      booltest.push_back(bool(temp)); 
    }
    std::cout << std::endl;
    for (const auto& x : booltest) {
      std::cout << x;
    }
    // for (int i=1; i <= n; i++){
    //     cin >> temp;
    //     a.push_back(temp);
    // }
    // for (int j=1; j<=q; j++){
    //     cin >> k;
    //     cout << a[k] << a[t];
    // }
    // cin >> k;
    // return 0;
}