#include "lc_pub.h"


class Solution {
    public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n=nums.size();
        long long s = 0,ans=0;
        vector<long long> mn_sum(k, 0);        
        mn_sum[0]=0;
        for (int i=0;i<k-1;i++) {
            s+=nums[i];
            mn_sum[i+1]=s;
        }
        if (n==k) return s+nums[n-1];
        s+=nums[k-1];
        ans=s;
        mn_sum[0]=min(mn_sum[0],s);
        for (int i=k;i<n;i++) {
            s+=nums[i];
            ans=max(ans, s-mn_sum[(i+1)%k]);
            mn_sum[(i+1)%k]=min(mn_sum[(i+1)%k], s);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-1,-2,-3,-4,-5};

    Solution so;
    cout << so.maxSubarraySum(nums, 4) << endl;
    return 0;
}
