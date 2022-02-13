#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <string_view>
#include <stdio.h>

using namespace std;

void getChars(string &needle, map<char, int> &NcharList, int len) {
	char temp;
	for (int i = 0; i < len; ++i) {
          temp = needle[i];
          if (NcharList.count(temp) == 0) {
            NcharList[temp]=1;
          } else {
            NcharList[temp]+=1;
		  }
	}
}

void parse(string &hay, string &temp, int start, int &len){
  temp = "";
  for (int i = start; i < start + len; i++) {
    temp += hay[i];
  }
}

bool check(string &checkPerm, unordered_set<int> &existPerm, string testStr,int len){
  
    for (const auto &elem : existPerm) {
        if(checkPerm==testStr.substr(elem,len)){
            return false;
        }
    }
    return true;
}

int main() { 
    freopen("s3.4-30.in", "r",stdin);
    string needle, hay;
    cin >> needle;
    cin >> hay;

    map<char, int> NcharList;
    int NLen = needle.length();
    getChars(needle, NcharList, NLen);

    int Hlen = hay.length();
    map<char, int> HcharList;
    char temp;
    string tempPerm;
    //unordered_set<string> existPerms;
    map<size_t, bool> existPer;
    int combs=0;
    int chars = 0;
    //string_view Hview(hay);

    hash<string> h;

    for (int i = 0; i < Hlen; ++i) {
      temp = hay[i];
      chars += 1;
      if (HcharList.count(temp) == 0) {
        HcharList[temp] = 1;
      } else {
        HcharList[temp] += 1;
      }
      if (chars==NLen){
        if (HcharList==NcharList){
          //parse(hay, tempPerm, i + 1 - NLen, NLen);
          tempPerm = hay.substr(i + 1 - NLen, NLen);
          //tempPerm= Hview.substr(i + 1 - NLen, NLen);
          //tempPerm = hay;
          //tempPerm.erase(0, i + 1 - NLen);
          //tempPerm.erase(tempPerm.begin() + NLen, tempPerm.end());
          
          size_t hash = h(tempPerm);
          //if (!existPer[hash]){
              //existPerms.insert(tempPerm);
          //if (check(tempPerm,existPer, hay, NLen)){
            existPer[hash]=true;
              combs += 1;
              //cout << combs << "\n";
          }
          
        }
        HcharList[hay[i + 1 - NLen]] -= 1;
        if (HcharList[hay[i+1-NLen]]==0){
          HcharList.erase(hay[i + 1 - NLen]);
        }
        chars -= 1;
      }
    }
    cout << combs;
    fclose(stdin);
}
