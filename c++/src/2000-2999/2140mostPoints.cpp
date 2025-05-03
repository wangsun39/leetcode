#include "lc_pub.h"

class Solution {
    public:
    long long mostPoints(vector<vector<int>>& questions) {
        const int n = questions.size();
        std::vector<long long> dp(n + 1, 0);
        if (questions[0][1] + 1 > n) dp[n] = questions[0][0];
        else dp[questions[0][1] + 1] = questions[0][0];
        for (int i=1;i<n;i++) {
            dp[i] = max(dp[i], dp[i-1]);
            if (i + questions[i][1] + 1 > n) dp[n] = max(dp[n], dp[i] + (long long)questions[i][0]);
            else dp[i + questions[i][1] + 1] = max(dp[i + questions[i][1] + 1], dp[i] + (long long)questions[i][0]);
        }
        return dp[n];
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr = parseGrid("[[3,2],[4,3],[4,4],[2,5]]");

    Solution so;
    cout << so.mostPoints(arr) << endl;
    return 0;
}
