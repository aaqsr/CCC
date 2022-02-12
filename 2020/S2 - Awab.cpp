#include <iostream>
#include <map>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <array>
#include <queue>
#include <set>

using namespace std;

struct point
{
    int rowNum{0};
    int colNum{0};
    int val{0};
};

void expand(const map<int, vector<point>> &pointMap, queue<point> &frontier, set<int>& visited, point &goal, bool &flag) {
    point currentPoint = frontier.front();

    int nextPoint = currentPoint.colNum * currentPoint.rowNum;

    if (visited.count(nextPoint) == 0) { // idk if this memoization is done correctly

        if (nextPoint == goal.val) {
            flag = true;
            return;
        }
        if (pointMap.count(nextPoint)) {
            vector<point> coords = pointMap.at(nextPoint); // wrap in throw / catch?

            for(auto const& i : coords)
            {
                frontier.push(i);
            }
            visited.insert(currentPoint.val);
        }
    }

    frontier.pop();
}

int main()
{
    int rowCount{0};
    cin >> rowCount;

    int colCount{0};
    cin >> colCount;

    // array<array<int, 1005>, 1005> gridArr{0};
    map<int, vector<point>> pointMap;
    queue<point> frontier;
    set<int> visited;

    point start{};
    point goal{};

    bool flag{false};

    for (int r{0}; r < rowCount; r++)
    {
        for (int c{0}; c < colCount; c++)
        { // roll credits
            // cin >> gridArr[r][c];

            int num{0};
            cin >> num;

            point currPoint{c + 1, r + 1, num};

            if (r == 0 && c == 0) {
                goal = currPoint;
            }
            if ( (r+1) == rowCount && (c+1) == colCount ) {
                start = currPoint;
            }
            // point curr {c + 1, r + 1};
            // curr.colNum = c + 1;
            // curr.rowNum = r + 1;

            pointMap[num].push_back(currPoint);
        }
    }

    frontier.push(start);
    do {
        if (flag) {
            break;
        }

        expand(pointMap, frontier, visited, goal, flag);
    } while (frontier.size() > 0);

    // for (int r{0}; r < rowCount; r++)
    // {
    //     for (int c{0}; c < colCount; c++)
    //     { // roll credits
    //         cout << gridArr[r][c] << " ";
    //     }
    //     cout << "\n";
    // }

    // for (auto const& [key, val] : pointMap){
    //     for(auto const& i : val)
    //     {
    //         cout << '{' << key << ':';
    //         cout << '[' << i.rowNum << ',' << i.colNum << ',' << i.val << ']' << '}';
    //     }
    // }
    // cout << start.val << " " << goal.val << endl;
    string output = (flag) ? "yes" : "no";
    cout << output;

    return 0;
}
