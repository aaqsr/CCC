#include <iostream>
#include <vector>
#include <unordered_map>
#include <stdio.h>

using namespace std;

struct cords{
  int x, y;
};

//unordered_map<cords,int> grid; 
vector<vector<int>> grid;
int M, N;

void colourCol(int ind){
	for(int i=0; i<M; i++){
    grid[i][ind]*=-1;
	}
}

void colourRow(int ind) {
  for (int i = 0; i < N; i++) {
    grid[ind][i]*=-1;
  }
}

void initGrid(){
  vector<int> temp;
  for (int j = 0; j < N; j++) {
    temp.push_back(-1);
  }
	for(int i=0; i < M; i++){
    grid.push_back(temp);
	}
}

int check(){
  int count = 0;
	for (int i=0; i<M; i++){
		for (int j=0; j<N; j++){
			if (grid[i][j]==1){
                    count += 1;
			}
		}
	}
        return count;
}


int main() { 
	freopen("j5.09.in", "r", stdin);
	cin >> M >> N;
  initGrid();
  int K;
        cin >> K;
  char choiceT;
        int choiceI;
	  for (int i=0; i<K; i++){
          cin >> choiceT >> choiceI;
		  if (choiceT == 'C'){
            colourCol(choiceI-1);
		  } else {
			colourRow(choiceI-1);
		  }
                  cout << i << "\n";
	  }
          cout << check();
          fclose(stdin);
}

