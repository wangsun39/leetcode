#include "lc_pub.h"

class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size(),n2=nums2.size();
        vector<vector<int>> dp(n1, vector<int>(n2, 0));
        for (int i=0;i<n1;i++) {
            for (int j=0;j<n2;j++) {
                dp[i][j]=nums1[i] * nums2[j];
                if (i) dp[i][j]=max(dp[i][j],dp[i-1][j]);
                if (j) dp[i][j]=max(dp[i][j],dp[i][j-1]);
                if (i&&j) dp[i][j]=max(dp[i][j],dp[i-1][j-1]+nums1[i] * nums2[j]);
            }
        }
        return dp[n1-1][n2-1];
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    
    Solution so;
    return 0;
}
