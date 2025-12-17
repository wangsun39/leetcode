#include "lc_pub.h"

long long dp[1000][501][3];  // 对应三种状态的最大收益
class Solution {
    public:
    long long maximumProfit(vector<int>& prices, int k) {
        int n=prices.size();
        for (int i=0;i<n;i++)
            for (int j=0;j<=k;j++)
                 for (int k=0;k<3;k++) {
                    dp[i][j][k]=INT32_MIN;
                 }
        dp[0][0][0] = 0;  // 未交易
        dp[0][0][1] = -prices[0];  // 买入状态
        dp[0][0][2] = prices[0];  // 卖出状态
        long long ans=0;
        for (int i=1;i<n;i++) {
            for (int j=0;j<=k;j++) {
                if (j*2>i+1) break;
                dp[i][j][0]=dp[i-1][j][0];
                dp[i][j][1]=dp[i-1][j][1];
                dp[i][j][2]=dp[i-1][j][2];
                if (j) {
                    dp[i][j][0]=max({dp[i-1][j][0],dp[i-1][j-1][1]+prices[i],dp[i-1][j-1][2]-prices[i]});
                    dp[i][j][1]=max(dp[i-1][j][0]-prices[i],dp[i-1][j][1]);
                    dp[i][j][2]=max(dp[i-1][j][0]+prices[i],dp[i-1][j][2]);
                }
                else {
                    dp[i][j][1]=max({dp[i][j][1],(long long)-prices[i]});
                    dp[i][j][2]=max({dp[i][j][2],(long long)prices[i]});
                }
                ans=max(ans,dp[i][j][0]);
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{12,16,19,19,8};

    Solution so;
    cout<<so.maximumProfit(nums, 2)<<endl;
    return 0;
}
