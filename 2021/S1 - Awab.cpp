#include <iostream>
#include <vector>
using namespace std;



int main() {
    int N{0};
    vector<long> parallelSides;
    vector<long> heights;
    double area{0};

    cin >> N;

    for (int i{0}; i < N+1; i++) {
        long temp{0};
        cin >> temp;
        parallelSides.push_back(temp);   
    }
    for (int i{0}; i < N; i++) {
        long temp{0};
        cin >> temp;
        heights.push_back(temp);
    }

    for (int i{1}; i < N+1; i++) {
        double fenceArea{0.0};
        double sides{0.0};
        long leftSide = parallelSides[i-1];
        long rightSide = parallelSides[i];
        long height = heights[i - 1];

        sides = (double(leftSide) + double(rightSide)) / 2;

        fenceArea =  sides * height;

        // cout << fenceArea << endl;
        area += fenceArea;
    }

    cout << fixed << area;

    // for (const auto& x : heights) {
    //     cout << x;
    // }
}