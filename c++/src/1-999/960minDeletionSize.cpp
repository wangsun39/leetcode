#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int minDeletionSize(vector<string>& strs) {
        int r=strs.size(),c=strs[0].size(),ans=0;
        vector<int>dp(c, 1);
        int ans=1;
        for (int i=1;i<c;i++) {
            for (int j=0;j<i;j++) {
                bool gt=true;
                for (int k=0;k<r;k++) {
                    if (strs[k][j]>strs[k][i]) {
                        gt=false;
                        break;
                    }
                }
                if (gt) {
                    dp[i]=max(dp[i],dp[j]+1);
                    ans=max(ans,dp[i]);
                }
            }
        }
        return c - ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> strs{"xga","xfb","yfa"};
    Solution so;
    cout<<so.minDeletionSize(strs);
    return 0;
}