#include "lc_pub.h"

using namespace std;

class Solution {
public:

int numTilings1(int n) {
    if (n == 1) return 1;
    int MOD = 1'000'000'007;
    vector<vector<long long>> dp(n+1, vector<long long>(n+1, 0LL));  // 第一排长度为i，第二排长度为j的所有可能
    dp[0][0] = 1;
    for (int i=0;i<n+1;i++) {
        for (int j=0;j<n+1;j++) {
            if (i<=0&&j<=0) continue;
            if (i - j >= 2)
                dp[i][j]=dp[i-2][j];
            else if (j - i >= 2)
                dp[i][j]=dp[i][j-2];
            else if (i == j)
                if (i>1)
                    dp[i][j]=dp[i-1][j-1]+dp[i-2][j]+dp[i-2][j-1]+dp[i-1][j-2];
                else
                    dp[i][j]=dp[i-1][j-1];
            else if (i > j){
                if (j > 0)
                    dp[i][j]=dp[i-2][j]+dp[i-2][j-1];
            }
            else
            {
                if (i>0)
                    dp[i][j]=dp[i][j-2]+dp[i-1][j-2];
            }
            dp[i][j]%=MOD;
        }
    }
    return dp[n][n];
    }
int numTilings(int n) {
    if (n == 1) return 1;
    int MOD = 1'000'000'007;
    vector<vector<long long>> dp(n+1, vector<long long>(4, 0LL));  // dp[i][j] 表示处理第i列时，i列的四种情况的所有4种可能
    dp[0][0] = 1;
    for (int i=1;i<n+1;i++) {
        dp[i][0]=(dp[i-1][0]+dp[i-1][1]+dp[i-1][2]+dp[i-1][3])%MOD;  // 两个格子是填满的
        dp[i][1]=(dp[i-1][3]+dp[i-1][2])%MOD;
        dp[i][2]=(dp[i-1][3]+dp[i-1][1])%MOD;
        dp[i][3]=(dp[i-1][0])%MOD;
    }
    return dp[n][0];
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    cout << so.numTilings(4) <<endl;
    return 0;
}