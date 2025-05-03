#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    public:
    int palindromePartition(string s, int k) {
        int n = s.size();
        vector<vector<int>> steps(n, vector<int>(n, -1));  // steps[i][j] 记忆化区间[i,j]变成区间需要修改的最少次数
        auto chg = [&](this auto && chg, int l, int r) -> int {  // [l, r]
            if (steps[l][r] > -1) return steps[l][r];
            if (l + 1>=r) return steps[l][r] = s[l] == s[r] ? 0 : 1;
            if (s[l] == s[r]) return steps[l][r] = chg(l+1,r-1);
            return steps[l][r] = chg(l+1,r-1) + 1;
        };
        vector<vector<int>> dp(n, vector<int>(k+1, n));  // dp[i][j] 表示前i项，分割成j个回文，需要的最少修改
        dp[0][1] = 0;
        for (int i=1;i<n;i++) {
            dp[i][1] = chg(0, i);
            for (int j=2;j<=min(i+1,k);j++) {
                for (int t=0;t<i;t++) {
                    int v = chg(t+1,i);
                    dp[i][j] = min(dp[i][j],dp[t][j-1]+v);
                }
            }
        }
        return dp[n-1][k];

    };
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    // auto v = so.palindromePartition("le",2);
    auto v = so.palindromePartition("abc",2);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
