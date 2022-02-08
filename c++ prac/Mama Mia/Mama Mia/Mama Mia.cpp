#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    vector<int> a{};
    int n;
    int q;
    int k;
    int t;
    int temp;
    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        cin >> temp;
        a.push_back(temp);
    }

    for (int j = 1; j <= q; j++) {
        cin >> k;
        cout << a[k];
    }

    cin >> k;   
    return 0;
} 