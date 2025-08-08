#include "lc_pub.h"

using namespace std;

class Solution {
public:

    double soupServings(int n) {
        if (n>4451) return 1;
        n = (n + 24) / 25;
        vector<vector<double>> dp(n+1, std::vector<double>(n+1, 0));  // 初值分别为a,b时最终结果
        for (int i=1;i<=n;i++) {
            dp[0][i]=1;
            dp[i][0]=0;
        }
        dp[0][0]=0.5;
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=n;j++) {
                dp[i][j]=(dp[max(i-4,0)][j]+dp[max(i-3,0)][max(j-1,0)]+dp[max(i-2,0)][max(j-2,0)]+dp[max(i-1,0)][max(j-3,0)])*0.25;
            }
        }
        return dp[n][n];
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    cout << so.soupServings(25) <<endl;
    return 0;
}