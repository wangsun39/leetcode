#include "lc_pub.h"

class Solution {
public:
    bool checkOnesSegment(string s) {
        int n = s.size();
        for (int i=0;i<n-1;i++) {
            if (s[i]=='0'&&s[i+1]=='1') return false;
        }
        return true;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
