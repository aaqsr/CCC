#include <iostream>

using namespace std;

double factorial(int n){
  double product = 1;
  for (int i = 1; i <= n;i++) {
		product *= i;
	}
  return product;
}

int choose(int n,int c){ //n is amount of number and c is number of 4s
  double ans;
  ans = factorial(n) / (factorial(c) * factorial(n - c));
  return ans;
}

int main()
{ 
	int N;
    cin >> N;
	//cout << choose(5, 2);
    int temp5;
    int temp4;
    int ways = 0;
    temp5 = N % 4;
	if (5*temp5<N){
      temp4 = (N - 5 * temp5)/4;
	  while (temp4>=0){
        ways += 1;
            temp4 -= 5;
        temp5 += 4;
	  }
          cout << ways;
	} else if(N%5==0){
          cout << 1;
	} else {
          cout << 0;
	}
}

