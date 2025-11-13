#include "lc_pub.h"


class Solution {
    public:
    int maxOperations(string s) {
        int n=s.size(),ans=0;
        int c1=ranges::count(s, '1');
        for (int i=n-1;i>=0;i--) {
            if (s[i]=='1') {
                c1--;
                continue;
            }
            if (i==n-1||s[i+1]=='1')
                ans+=c1;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5};

    Solution so;
    cout << so.maxOperations("1001101") << endl;
    return 0;
}
