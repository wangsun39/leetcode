#include "lc_pub.h"

using namespace std;

class Solution {
public:

    bool rotateString(string s, string goal) {
        int n=s.size();
        if (n!=goal.size()) return false;
        for (int i=0;i<n;i++) {
            if (s.substr(i) + s.substr(0, i)==goal) return true;
        }
        return false;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    return 0;
}