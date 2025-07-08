#include "lc_pub.h"

class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        ranges::sort(events, [](const vector<int>& a, const vector<int>& b) {
                        if (a[1]==b[1]) return a[0] < b[0];
                        return a[1] < b[1];
                    });
        int n = events.size();
        vector<int>ends(n, 0);
        for (int i=0;i<n;i++)
            ends[i]=events[i][1];
        std::vector<std::vector<int>> dp(n, std::vector<int>(k+1, 0));  // dp[i][j] 表示前i个会议参加j个的最大价值
        for (int j=1;j<=k;j++) {
            for (int i=0;i<n;i++) {
                int start=events[i][0];
                if (i==0) {
                    if (j==1) dp[i][j]=events[0][2];
                    continue;
                }
                dp[i][j]=max(dp[i-1][j],events[i][2]);
                auto p=ranges::lower_bound(ends,start);
                if (p==ends.begin()) continue;
                int pre=p-1-ends.begin();
                if (dp[pre][j-1])
                    dp[i][j]=max(dp[i][j],dp[pre][j-1]+events[i][2]);
            }
        }
        int ans=0;
        for (int j=1;j<=k;j++) ans=max(ans,dp[n-1][j]);
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    // vector<vector<int>> grid = {{1,1,1,-1,-1},{1,1,1,-1,-1},{-1,-1,-1,1,1},{1,1,1,1,-1},{-1,-1,-1,-1,-1}};
    vector<vector<int>> grid = parseGrid("[[19,42,7],[41,73,15],[52,73,84],[84,92,96],[6,64,50],[12,56,27],[22,74,44],[38,85,61]]");
    cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    auto v = so.maxValue(grid, 5);
    cout << v << endl;
    return 0;
}
