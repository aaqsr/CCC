#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

unordered_map<string, unordered_set<string>> together;
unordered_map<string, unordered_set<string>> separate;

void fill(unordered_map<string, unordered_set<string>> &ref) { 
	int X;
  cin >> X;
string temp1,temp2;
  for (int i=0; i<X;i++){
  cin >> temp1 >> temp2;
    ref[temp1].insert(temp2);
  }
}

void checkErr(string &t1, string &t2, string &t3, int &err) {
  err += (separate[t1].count(t2) + separate[t1].count(t3));
  for (auto &it : together[t1]) {
    if (it != t2 and it != t3) {
      err += 1;
    }
  }
}

int main()
{ 
	fill(together);
  fill(separate);
        int G;
  cin >> G;
        int errors = 0;
        string tempN1, tempN2, tempN3;
	for (int i=0; i < G; i++){
          cin >> tempN1 >> tempN2 >> tempN3;
          checkErr(tempN1, tempN2, tempN3, errors);
          checkErr(tempN2, tempN3, tempN1, errors);
          checkErr(tempN3, tempN1, tempN2, errors);
	}
        cout << errors;
}
