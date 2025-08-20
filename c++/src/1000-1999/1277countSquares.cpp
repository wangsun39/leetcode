#include "lc_pub.h"


class Solution {
    
    public:
    int countSquares(vector<vector<int>>& matrix) {
        int r=matrix.size(),c=matrix[0].size();
        vector dp(r, vector<int>(c,0));
        int ans=0;
        for (int i=0;i<c;i++) 
            ans+=(dp[0][i] = matrix[0][i]);
        for (int i=1;i<r;i++)
            ans+=(dp[i][0]=matrix[i][0]);
        for (int i=1;i<r;i++) {
            for (int j=1;j<c;j++) {
                if (matrix[i][j]==0) continue;
                int mn = min(dp[i-1][j], dp[i][j-1]);
                if (dp[i-mn][j-mn])
                    dp[i][j] = mn+1;
                else
                    dp[i][j]=max(mn,1);
                ans += dp[i][j];
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto arr=parseGrid("[[1,0,1],[1,1,0],[1,1,0]]");
    auto v = so.countSquares(arr);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
