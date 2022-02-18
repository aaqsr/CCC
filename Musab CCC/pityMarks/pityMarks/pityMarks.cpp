#include <iostream>
#include <cmath>
#include <string>
#include <array>

using namespace std;

int checkMax(int N, int M) {
  int recurPairs;
  recurPairs = M * (N - M) + (M * (M + 1)) / 2;
}

int main(){
  int N, M, K;
  cin >> N >> M >> K;
  int max;
  int altPairs = N / M;
  int nonPairs = 0;
  int rem = N % M;
  int n = N;
  max = checkMax(N, M);

  if (max < K) {
    cout << -1;
  } else if (K < N) {
    cout << -1;
  } else if (K == N) {
    for (int i = 0; i < N; i++) {
      cout << 1 << " ";
    }
  }
  else {
    while (max > K) {
      if (nonPairs == 0 && rem != 0) {
        n -= rem;
        nonPairs += 1;
        max = checkMax(n, M);
        max += rem;
        continue;
      } else {
        altPairs -= 1;
        n -= M;
        nonPairs += 1;
        max = checkMax(n, M);
        max += nonPairs * M + rem;
      }
    }
    int diff=K-max;
    if
  }