#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

int main(){ 
  int n;
  cin >> n;
  int r;
  unordered_map<int, int> rFreq;
  vector<int> max = {};
  vector<int> prevMax = {};
  for (int i = 0; i < n; i++) {
    cin >> r;
    rFreq[r] += 1;
    if (max.size()==0 || rFreq[r] > rFreq[max[0]] || r==max[0]) {
        if (count(max.begin(),max.end(),r)){
        max.erase(find(max.begin(), max.end(), r));
        }
      prevMax = max;
      max = {r};
    } else if (rFreq[r] == rFreq[max[0]] && r!=max[0]) {
      max.push_back(r);
    } else if (prevMax.size()==0 || rFreq[r] == rFreq[prevMax[0]]) {
        if (prevMax.size() > 0 && r==prevMax[0]){
        prevMax = {};
        }
      prevMax.push_back(r);
    } else if (rFreq[r]>rFreq[prevMax[0]]){
      prevMax = {r};
    }
  }
  int maxDif = 0;
  if (max.size() == 1 and prevMax.size() == 1) {
      maxDif = abs(max[0] - prevMax[0]);
  } else if (max.size() > 1) {
    for (auto &i : max) {
      for (auto &j : max) {
        int temp;
        temp = abs(i - j);
        if (temp > maxDif) {
         maxDif = temp;
          }
        }
      }
    } else {
      for (auto &i : prevMax) {
        int temp;
        temp = abs(max[0] - i);
        if (temp > maxDif) {
          maxDif = temp;
        }
      }
    }
    cout << maxDif;
}