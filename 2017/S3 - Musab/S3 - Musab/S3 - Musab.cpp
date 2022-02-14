#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

void fillMap(unordered_map<int, int> &lenFreq, int &n){
  int temp;
	for (int i=0; i<n; i++){
    cin >> temp;
	lenFreq[temp] += 1;
	}
}

int calcSize(int height, unordered_map<int, int> lenFreq) { 
	int small=max(1,height-2000);
    int size = 0;
        while (small <= height / 2) {
          if ((double)small == (double)height / 2) {
            size += lenFreq[small] / 2;
          } else {
            size += min(lenFreq[small], lenFreq[height - small]);
          }
          ++small;
        }
        return size;
}

int main()
{
  int n;
  cin >> n;
  unordered_map<int, int> lenFreq;

  fillMap(lenFreq, n);

  int max=0;
  int count = 0;
  for (int i=2; i<=4000; i++){
    int temp = calcSize(i, lenFreq);
    if (temp> max)
	{ 
		max = temp;
        count = 1;
	} else if (temp == max){
      count += 1;
	}
  }
  cout << max << " "<< count;
}
