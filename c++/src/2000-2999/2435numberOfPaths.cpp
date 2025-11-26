#include "lc_pub.h"

class Solution {
    public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int r=grid.size(),c=grid[0].size();
        vector<vector<vector<int>>> dp(r, vector<vector<int>>(c, vector<int>(k, 0)));
        dp[0][0][grid[0][0]%k]=1;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                for (int t=0;t<k;t++) {
                    int v=(t+k-grid[i][j]%k)%k;
                    if (i) dp[i][j][t]+=dp[i-1][j][v];
                    if (j) dp[i][j][t]+=dp[i][j-1][v];
                }
            }
        }
        return dp[r-1][c-1][0];
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {4,1,3,3};

    Solution so;
    return 0;
}
