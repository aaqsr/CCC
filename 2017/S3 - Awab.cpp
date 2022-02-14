/* 
N pieces of wood
ith piece has size Li

board has 2 pieces of wood of length Li + Lj

fence has boards of same length

number of boards to make fence is length
Li + Lj is height

longest fence
and number of heights of that fence 

in:
N
Lengths of board[]

out: 
max length, the number of heights of fence
*/

/* 
Pick any two integers, calc their length
then find difference with that length using all the other 
*/

#include <iostream>
#include <vector>

using namespace std;

int main() { 
    int N{0};
    vector<int> lengths;
   

    cin >> N;
    for (int i{0}; i < N; i++) {
        int temp;
        cin >> temp;
        lengths.push_back(temp);
    }
    


    return 0;
}