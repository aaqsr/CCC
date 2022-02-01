// 2018 S1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string temp;
    int c;
    int position;
    cin >> temp;
    const int n = stoi(temp);
    int villages[101];
    for (int i = 1; i <= 100; i++) {
        villages[i] = 1000000001;
    }
    for (int i = 1;i <= n;i++) {
        cin >> position;
        for (c = 1; c <= i; c++) {
            if (position<villages[c]) {
                for (int k = i; k > c; k--) {
                    villages[k] = villages[k - 1];
                }
                break;
            }
        }
        villages[c] = position;
    }

    /*for (int i = 1; i <= n; i++) {
        cout << villages[i] << endl;
    }*/

    float tempShort, shortest;
    shortest = 2000000000;
    for (int i = 2; i <= n - 1; i++) {
        tempShort = (villages[i + 1] - villages[i - 1])/2;
        //cout << tempShort << endl;
        if (tempShort < shortest) {
            shortest = tempShort;
            //cout << shortest << endl;
        }
    }
    cout << shortest;
}