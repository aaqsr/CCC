#include <iostream>
#include <cmath>

using namespace std;

int index = 0;
int arr[3000];

int checkPrime(int x)
{
    for (int i = 2; i <= pow(x, 0.5); i++)
    {
        if (x % i == 0)
        {
            return false;
        }
    }
    return true;
};

void findPair(int p)
{
    int a;
    int b;
    bool val = false;
    while (val == false)
    {
        for (int i = p; i < 2 * p; i++)
        {
            if (checkPrime(i))
            {
                if (checkPrime(2 * p - i))
                {
                    arr[index] = 2 * p - i;
                    index += 1;
                    arr[index] = i;
                    index += 1;
                    val = true;
                    break;
                }
            }
        }
    }
}

int main()
{
    int t;
    cin >> t;
    int temp;
    for (int k = 0; k < t; k++)
    {
        cin >> temp;
        findPair(temp);
    }
    int e = 0;
    for (int k = 0; k < 2*t; k += 2)
    {
        cout << arr[k] << " " << arr[k + 1] << endl;
    }
}