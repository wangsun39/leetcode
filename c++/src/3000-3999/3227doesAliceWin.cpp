#include "lc_pub.h"


class Solution {
    public:
    bool doesAliceWin(string s) {
        int n=s.size();
        int cnt=0;
        for (int i=0;i<n;i++) {
            if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') cnt++;
        }
        if (cnt==0) return false;
        return true;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5};

    Solution so;
    cout << so.doesAliceWin("leetcoder") << endl;
    return 0;
}
