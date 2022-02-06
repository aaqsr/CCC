#include <iostream>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    int M = 0; // rows
    cin >> M;
    int N = 0; // columns
    cin >> N;
    

    int grid[M][N];
    // map<int, int[20][2]> numCoords; // arbitrary numbers, bump up the index 1 if issues

    for (int i; i < M;)
    {
        string row = "";
        cin >> row;
        cout << row;
        stringstream ssin(row);
        int j = 0;
        while (ssin.good() && j < N)
        {
            char digit = '0';
            ssin >> digit;
            grid[i][j] = int(digit);
            ++j;
        }
        ++i;
    }

    cout << endl << grid[0][0];
}
