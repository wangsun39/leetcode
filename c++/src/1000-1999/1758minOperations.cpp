#include "lc_pub.h"

class Solution {
public:
    int minOperations(string s) {
        int n=s.size();
        int cnt1=0,cnt2=0;
        for (int i=0;i<n;i++) {
            if (i&1)cnt1+=s[i]=='0';
            else cnt1+=s[i]=='1';
        }
        for (int i=0;i<n;i++) {
            if ((i&1)==0)cnt2+=s[i]=='0';
            else cnt2+=s[i]=='1';
        }
        return min(cnt1,cnt2);
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
