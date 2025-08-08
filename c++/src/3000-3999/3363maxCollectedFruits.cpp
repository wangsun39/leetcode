#include "lc_pub.h"

class Solution {
public:
    int maxCollectedFruits(vector<vector<int>>& fruits) {
        int n=fruits.size();
        vector<vector<int>> dp(n, std::vector<int>(n, INT_MIN));
        int s1 = 0;
        for (int i=0;i<n;i++) s1+=fruits[i][i];

        dp[0][n - 1] = fruits[0][n - 1];
        for (int i=1;i<n;i++) {
            for (int j=i+1;j<n;j++) {
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+fruits[i][j];
                if (j+1<n) dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + fruits[i][j]);
            }
        }
        int s2 = dp[n - 2][n - 1];
        dp[n - 1][0] = fruits[n - 1][0];
        for (int j=1;j<n;j++)
            for (int i=j+1;i<n;i++) {
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + fruits[i][j];
                if (i + 1 < n)
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + fruits[i][j]);
            }
        int s3 = dp[n - 1][n - 2];
        return s1 + s2 + s3;
    }
};


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    // so.addText("leetcode");
    // cout << so.deleteText(10) << endl;
    return 0;
}
