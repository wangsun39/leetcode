#include "lc_pub.h"

using namespace std;

class Solution {
public:

    double new21Game(int n, int k, int maxPts) {
        if (n >= k - 1 +maxPts) return 1;
        vector<double> dp(n + maxPts + 1, 0);
        for (int i=k;i<=n;i++) dp[i] = 1;
        double s = 0; // 区间和
        for (int i=k+1;i<k+maxPts+1;i++) {
            s+=dp[i];
        }
        for (int i=k-1;i>=0;i--) {
            s+=dp[i+1]-dp[i+1+maxPts];
            dp[i]=s/maxPts;
        }
        return dp[0];
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {10,1,10};
    Solution so;
    cout << so.new21Game(10,1,10) <<endl;
    return 0;
}