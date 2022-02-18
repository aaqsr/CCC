#include <iostream>
#include <array>
#include <vector>
#include <string>

using namespace std;


struct cords{
  int r, c;
};
array<array<int, 3>, 3> grid;
const int nil = 1000000001;
vector<cords> unknown;
bool stop = false;

bool compute(array<array<int, 3>, 3> tempGrid){ 
    bool noMoreSwaps = false;
    int rowCount;
    int colCount;
    int rowPos;
    int colPos;
    while (noMoreSwaps == false){
      noMoreSwaps = true;
      for (int i = 0; i < 3; i++) {
        rowCount = 0;
        colCount = 0;
        for (int j=0; j<3; j++){
          if (tempGrid[i][j] == nil) {
            rowCount++;
            rowPos = j;
          }
          if (tempGrid[j][i] == nil) {
            colCount++;
            colPos = j;
          }
        }
        if (rowCount==1 || colCount == 1){
          noMoreSwaps = false;
            if (rowCount ==1){
                if (rowPos==0){
                tempGrid[i][rowPos] = tempGrid[i][1] - (tempGrid[i][2] - tempGrid[i][1]);
                } else if(rowPos==1){
                  tempGrid[i][rowPos] = (tempGrid[i][0] + tempGrid[i][2]) / 2;
                } else {
                  tempGrid[i][rowPos] = tempGrid[i][1] + (tempGrid[i][1] - tempGrid[i][0]);
                }
            }
            if (colCount==1) {
              int tempVal = nil;
                if (tempGrid[colPos][i]!=nil){
                tempVal = tempGrid[colPos][i];
                }
                if (colPos == 0) {
                  tempGrid[colPos][i] = tempGrid[1][i] - (tempGrid[2][i] - tempGrid[1][i]);
                } else if (colPos == 1) {
                  tempGrid[colPos][i] = (tempGrid[0][i] + tempGrid[2][i]) / 2;
                } else {
                  tempGrid[colPos][i] = tempGrid[1][i] + (tempGrid[1][i] - tempGrid[0][1]);
                }
                if (tempVal!=nil && tempVal != tempGrid[colPos][i]){
                  return false;
                }
            }
            break;
        }
      }
    }
    bool perfect=true;
    for (int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            if (tempGrid[i][j]==nil){
            perfect = false;
            }
        }
    }
    if (perfect==true){
      stop = true;
      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
          cout << tempGrid[i][j] << " ";
        }
        cout << endl;
      }
    }
    return true;
}

int str_int(string temp){
  int num=0;
  for (int i = 1; i<=temp.size(); i++)  {
    num += ((temp[i-1])-('0')) * pow(10, temp.size() - i);
    }
  return num;
}

int main()
{
  freopen("s3.4-30.in", "r", stdin);
  string temp;
  int tempNum;

  //take input
  for (int r = 0; r < 3; r++) {
    for (int c = 0; c < 3; c++) {
      cin >> temp;
      if (temp == "X") {
        grid[r][c] = nil;
        unknown.push_back({r, c});
      }
      else {
        tempNum = str_int(temp);
          grid[r][c] = tempNum;
      }
    }
  }

  if (unknown.size() > 3) {
    compute(grid);
    while (stop != true) {
      array<array<int, 3>, 3> Tgrid;
      Tgrid = grid;
      int rowPos;
      for (int i = 0; i < 3; i++) {
        int rowCount = 0;
        for (int j = 0; j < 3; j++) {
          if (Tgrid[i][j] == nil) {
            rowCount++;
            rowPos = j;
          }
        }
        if (rowCount > 1) {
          int attempt = -1000000000;
          while (stop != true) {
            Tgrid[i][rowPos] = attempt;
            attempt += 1;
            compute(Tgrid);
          }
        }
      }
    }
  }
  if (unknown.size()==3){
  
  }
    fclose(stdin);
}

