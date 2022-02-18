#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int findMax(unordered_map<int, unordered_set<int>> &intersections) {
  int tempMax=0;
  int tempSize = 0;
    for (auto &pointSet:intersections){
        if (pointSet.second.size()>tempSize){
        tempSize = pointSet.second.size();
        tempMax = pointSet.first;
        }
    }
    return tempMax;
}

void adjust(unordered_map<int, unordered_set<int>> &intersections, int &max){
  for (auto &point : intersections) {
    if (point.first == max) {
      continue;
    }
    for (auto &house : intersections[max]) {
      auto it = point.second.find(house);
      if (it!=point.second.end()){
        point.second.erase(it);
      }
    }
  }
  intersections[max].erase(intersections[max].begin(), intersections[max].end());
}

bool check(unordered_map<int, unordered_set<int>> &intersections, int &houseCount, int &hoses){ 
    int max;
    bool validity = false;
    max = findMax(intersections);
    int tempHouse = houseCount;
    int tempHose = hoses;
    while (intersections[max].size() >= tempHouse/tempHose){
      tempHouse -= intersections[max].size();
      if (tempHouse==0){
        validity = true;
        break;
      }
      tempHose -= 1;
      adjust(intersections, max);
      max = findMax(intersections);
    }
    return validity;
}


int main(){ 
	int houseCount;
    unordered_set<int> houseList;
    unordered_map<int, unordered_set<int>> pointIntersections;
    cin >> houseCount;
		for (int i=0; i < houseCount; i++){
          int temp;
          cin >> temp;
          houseList.insert(temp);
		}
    int hoses;
    cin >> hoses;


    bool accepted = false;
    int dist = -1;
    while (accepted == false){
      dist++;
      for (auto &house : houseList) {
        pointIntersections[(house + dist) % 1000000].insert(house);
        int tempBound = house - dist;
        if (tempBound<0){
          tempBound = 1000000 + tempBound;
        }
        pointIntersections[(tempBound) % 1000000].insert(house);
      }
      unordered_map<int, unordered_set<int>> tempIntersections;
      tempIntersections = pointIntersections;
      accepted = check(tempIntersections,houseCount, hoses);
    }
    cout << dist;
}

