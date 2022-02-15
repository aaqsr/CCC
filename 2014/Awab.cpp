/*
 * The geneva confection
 * output
 * expected: output + 1
 * if input (stack.pop) is not expected
 * if input is > branch and branch != expected
 * output no
 */

#include <iostream>
#include <queue>
#include <stack>

using namespace std;

void runTest();

int main() {
    int T; cin >> T;
    for (int i{0}; i < T; i++) {
        runTest();
    }
}

void runTest() {
    char ans{'Y'};
    int output{0}, currentIn{0}, expected{0};
    stack<int> input;
    queue<int> branch;

    int N; cin >> N;
    for (int i{0}; i < N; i++) {
        int temp{0}; cin >> temp;
        input.push(temp);
    }

    for (int i{0}; i < N; i++) {
        expected = output + 1;
        currentIn = input.top();

        if (currentIn > branch.front()) {
            ans = 'N';
            break;
        }

        if (currentIn == expected) {
            output = currentIn;
            input.pop();
        } else if (branch.front() == expected) {
            output = branch.front();
            branch.pop();
        } else {
            branch.push(currentIn);
            input.pop();
        }
    }
    cout << ans;
}

