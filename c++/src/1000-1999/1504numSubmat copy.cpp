#include "lc_pub.h"


class Solution {
    
    public:
    int numSub(string s) {
        int n=s.size(),MOD=1'000'000'007;
        int ans=0,start=0;
        for (int i=0;i<n;i++) {
            if (s[i]=='1') {
                ans+=i-start+1;
                ans%=MOD;
            }
            else {
                start=i+1;
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
