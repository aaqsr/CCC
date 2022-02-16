#include <iostream>
#include <array>
#include <vector>

using namespace std;


struct cords{
  int r, c;
};
array<array<int, 3>, 3> grid;
const int nil = 1000000001;
vector<cords> unknown;


int main()
{
  char temp;

  //take input
  for (int r = 0; r < 3; r++) {
    for (int c = 0; c < 3; c++) {
      cin >> temp;
      if (temp == 'X') {
        grid[r][c] = nil;
        unknown.push_back({r, c});
      }
      else {
          grid[r][c] = (int)temp;
      }
    }
  }


}

