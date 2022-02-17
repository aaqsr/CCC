// brute force

#include <iostream>

using namespace std;

int main() {
  int N{0}, ans{0};
  cin >> N;

    if (N % 4 == 0) {
      ans += 1;
    }

    if (N % 5 == 0) {
      ans += 1;
    }

    if ((N % 4) % 5 == 0) || ( (N % 5) % 4 == 0) {
        ans += 1;
      }
}