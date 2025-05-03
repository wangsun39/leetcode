#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
int coinChange(vector<int>& coins, int amount) {
    int n = coins.size();
    if (amount==0) return 0;
    // 前i项组成和为j的最少硬币数为dp[i][j]
    std::vector<std::vector<int>> dp(n, std::vector<int>(amount + 1, INT_MAX));
    int i = 0;
    int ans = INT_MAX;
    while (coins[0]*i <= amount) {
        dp[0][coins[0]*i] = i;
        if (coins[0]*i == amount) ans=i;
        i++;
    }
    for (int i=1;i<n;i++) {
        for (int j=0;j<=amount;j++) dp[i][j]=dp[i-1][j];
        if (coins[i]>amount) continue;
        int v = coins[i];
        for (int j=1;j<=amount;j++) {
            int k=0;
            if (j % v == 0) dp[i][j] = j / v;
            while (j>=v*k) {
                if (dp[i-1][j-v*k]<INT_MAX)
                    dp[i][j]=min(dp[i][j],dp[i-1][j-v*k]+k);
                k++;
            }
        }
        if (dp[i][amount] < INT_MAX) ans=min(ans,dp[i][amount]);
    }
    if (ans < INT_MAX)
        return ans;
    return -1;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    vector<int> nums = {1,2147483647};
    auto v = so.coinChange(nums, 2);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
