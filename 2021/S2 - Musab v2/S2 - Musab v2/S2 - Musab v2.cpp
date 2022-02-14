#include <iostream>;
#include <unordered_map>;

using namespace std;

unordered_map<int, int> rowLog;
unordered_map<int, int> colLog;
int M, N, K;

int check() {
  int count = 0;
  for (int i = 1; i <= M; i++) {
    for (int j = 1; j <= N; j++) {
      count += (rowLog[i] + colLog[j]) % 2;
    }
  }
  return count;
}

int main() {
  char choice;
  int ind;
  cin >> M >> N >> K;
  for (int i = 0; i < K; i++) {
    cin >> choice >> ind;
    if (choice == 'R') {
      rowLog[ind] += 1;
    } else {
      colLog[ind] += 1;
    }
  }
  cout << check();
}