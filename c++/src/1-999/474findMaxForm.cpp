#include "lc_pub.h"

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int N=strs.size();
        vector<vector<vector<int>>>dp(N, vector<vector<int>>(m+1, vector<int>(n+1, 0)));
        for (int i=0;i<N;i++) {
            int c0=std::count(strs[i].begin(), strs[i].end(), '0');
            int c1=std::count(strs[i].begin(), strs[i].end(), '1');

            for (int j=0;j<=m;j++) {
                if (c0+j>m) break;
                for (int k=0;k<=n;k++) {
                    if (c1 + k > n) break;
                    dp[i][j+c0][k+c1]=max(dp[i][j+c0][k+c1],1);
                    if (i)
                        dp[i][j+c0][k+c1]=max(dp[i][j+c0][k+c1], dp[i-1][j][k]+1);
                }
            }
            if (i<N-1) dp[i+1]=dp[i];
        }
        int ans=0;
        for (int j=0;j<=m;j++) {
            for (int k=0;k<=n;k++) {
                ans=max(ans, dp[N-1][j][k]);
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> nums{"00011","00001","00001","0011","111"};
    Solution so;
    cout<<so.findMaxForm(nums, 8, 5);
    return 0;
}
