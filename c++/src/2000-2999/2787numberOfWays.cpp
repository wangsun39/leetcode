#include "lc_pub.h"

class Solution {
    public:
    int numberOfWays(int n, int x) {
        int MOD=1'000'000'007;
        if (x==1) {

        }
        vector dp(n + 1, vector<long long>(n + 1));  // dp[i][j] 小于i的数组合成j的总数是多少
        int ans = 0;
        for (int i=0;i<=n;i++)
            dp[i][0] = 1;  // 组成0认为是1种
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=n;j++) {
                dp[i][j]=dp[i-1][j];
                long long v = pow(i,x);
                if (v<=j) {
                    dp[i][j]+=dp[i-1][j-v];
                }
                dp[i][j]%=MOD;
            }
        }
        return dp[n][n];
    }
    };


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.numberOfWays(10,2) << endl;
    return 0;
}
