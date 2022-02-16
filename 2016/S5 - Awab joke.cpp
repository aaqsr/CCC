#include <iostream>
#include <vector>
#include <string>

using namespace std;

/* 
*  only gets 5 marks 
*  rest is too slow
*  the issue is optimisation
*  answers are all correct
*/

string updateStrip(string& strip, int N) {
  string ans = strip;

  for (int i{1}; i < N-1; i++) {
    if ((strip[i - 1] == '1') ^ (strip[i + 1] == '1')) {
      ans[i] = '1';
    } else {
      ans[i] = '0';
    }
  }

  // edge cases, literally
  ((strip[1] == '1') ^ (strip[N-1] == '1')) ? ans[0] = '1' : ans[0] = '0';

  ((strip[N-2] == '1') ^ (strip[0] == '1')) ? ans[N-1] = '1' : ans[N-1] = '0';

  return ans;
}

int main () {
  long long N{0}, T{0};

  // vector<bool> strip{0};
  string strip{"0"};
  strip.reserve(100001);

  cin >> N >> T;
  cin >> strip;
  // for (int i{0}; i < N; i++) {
  //   bool temp;
  //   cin >> temp;
  //   strip.push_back(temp);
  // }
  for (int i{1}; i <= T; i++) {
    strip = updateStrip(strip, N);
  }

  cout << strip;
}