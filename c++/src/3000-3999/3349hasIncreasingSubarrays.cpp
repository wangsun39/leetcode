#include "lc_pub.h"


class Solution {
    public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int cnt = k-1,n=nums.size();
        vector<int> dp(n,1);
        for (int i=1;i<n;i++) {
            if (nums[i-1]<nums[i]) {
                dp[i]=dp[i-1]+1;
            }
        }
        for (int i=0;i<n;i++) {
            if (i+k>=n) break;
            if (dp[i]>=k&&dp[i+k]>=k) return true;
        }
        return false;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    return 0;
}
