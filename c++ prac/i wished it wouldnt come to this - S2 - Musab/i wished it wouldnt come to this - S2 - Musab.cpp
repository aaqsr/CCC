#include <map>
#include <iterator>
#include <cmath>
#include <array>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct Cords {
	int xPos;
	int yPos;
};

void takeInp(int &m, int &n, map<int, vector<Cords>> &grid) {
	int tempVal;
	Cords tempCords;
	for (int i = 1; i <= m; i++) {
		for (int k =1; k<= n; k++){
			cin >> tempVal;
			tempCords.xPos = k;
			tempCords.yPos = i;
			grid[tempVal].push_back(tempCords);
		}
	}
}

bool search(Cords tempCords, map<int, vector<Cords>>& grid, queue<Cords>& front, map<int, bool>& vis) {
	front.pop();
	int tempVal = tempCords.xPos * tempCords.yPos;
	if (vis.count(tempVal) > 0) {
		return false;
	}
	else{
		vis[tempVal] = true;
		if (tempVal == 1) {
			return true;
		}
		else if (grid.count(tempVal) > 0) {
			for (const auto& xy : grid[tempVal]) {
				front.push(xy);
			}
		}
		return false;
	}
}



int main()
{
	int m,n;
	cin >> m;
	cin >> n;
	map<int, vector<Cords>> grd;
	takeInp(m, n, grd);
	queue<Cords> frontier;
	map<int, bool> visited;
	frontier.push({m,n});
	bool curState = false;
	while (!frontier.empty() && curState==false) {
		curState = search(frontier.front(), grd, frontier, visited);
	}
	cout << (curState ? "yes" : "no");


	/*for (const auto &x : grd) {
		cout << "[" << x.first << ",";
		for (const auto& i : x.second) {
			cout << i.xPos << " " << i.yPos << " | ";
		}
		cout << "]";
	}*/
}
