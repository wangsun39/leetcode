#include "lc_pub.h"


class Solution {
    public:
    int countPartitions(vector<int>& nums, int k) {
        int n=nums.size();
        int MOD=1e9+7;
        vector<int>dp(n+1,0);  // 前i个数的最大分割数
        vector<int>s(n+1,0);  // dp的前缀和  s[i]=dp[0]+...+dp[i]
        multiset<int>ms;  // 滑窗内元素的计数
        int j=1; // 滑窗的起点
        dp[0]=s[0]=1;
        for (int i=1;i<=n;i++) {
            ms.insert(nums[i-1]);
            while (true) {
                // 计算区间内的最大最小值的差，要保证<=k
                int mn=*ms.begin();
                int mx=*prev(ms.end());
                if (mx-mn<=k) break;
                ms.erase(ms.find(nums[j-1]));
                j++;
            }
            // dp[i] = dp[j-1]+...+dp[i-1]
            if (j>=2)
                dp[i]=(s[i-1]-s[j-2]+MOD)%MOD;
            else
                dp[i]=s[i-1];
            s[i]=(s[i-1]+dp[i])%MOD;
        }
        return dp[n];
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{9,4,1,3,7};

    Solution so;
    cout<<so.countPartitions(nums, 4)<<endl;
    return 0;
}
