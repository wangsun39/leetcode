#include "lc_pub.h"


class Solution {
    public:
    long long maxProduct(vector<int>& nums) {
        int MX = (1 << 20);
        int n = nums.size();
        long long ans = 0;
        if (n < 5000) {
            for (int i=0;i<n;i++) {
                for (int j=i + 1;j<n;j++) {
                    if ((nums[i]&nums[j])==0) {
                        ans = max(ans, (long long)nums[i]*nums[j]);
                    }
                        
                }
            }
            return ans;
        }
        vector<long long> dp(MX, 0);
        for (auto x : nums)
            dp[x] = x;

        for (int i=0;i<20;i++)
            for (int mask=0;mask<MX;mask++)
                if (mask & (1 << i))
                    dp[mask] = max(dp[mask], dp[mask ^ (1 << i)]);

        for (auto x : nums) {
            long long x1 = (MX - 1) ^ x;
            long long y = dp[x1];
            ans = max(ans, x * y);
        }
            
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    cout<<so.maxProduct(nums)<<endl;
    return 0;
}
