#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <unordered_map>
#include <math.h>
#include <cmath>

using namespace std; 

struct Point { 
    int arcLength;
    float xCoord;
    float yCoord;
};

Point midPoint(Point& point1, Point& point2) {
    Point ans{0, 0, 0};
    ans.xCoord = (point1.xCoord + point2.xCoord) / 2;
    ans.yCoord = (point1.yCoord + point2.yCoord) / 2;

    return ans;
}

int main() {
  int numberOfPoints, circumference;
  float radius;
  vector<Point> Points{{0, 0, 0}};

  cin >> numberOfPoints >> circumference;

  radius = circumference / M_PI; 

  for (int i{0}; i < numberOfPoints; i++) {
    int arc{0};
    cin >> arc;

    double angle = double(arc) / radius;

    float xCoord = radius * cosf(float(angle));
    float yCoord = radius * sinf(float(angle));

    Points.push_back({arc, xCoord, yCoord});
  }
  
  for (int i{1}; i <= numberOfPoints; i++) {  // if i = 1
    for (int j{i+1}; j <= numberOfPoints-i; j++) {  // will get point 2 or greater
       for (int k{j+1}; k <= numberOfPoints-i-j; k++) {   // will get point 3 or greater
        Point& point1 = Points[i];
        Point& point2 = Points[j]; 
        Point& point3 = Points[k];


       }
  }
}
}
