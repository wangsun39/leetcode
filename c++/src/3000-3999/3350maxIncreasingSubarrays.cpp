#include "lc_pub.h"


class Solution {
    public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n=nums.size();
        int pre=0,cur=1;
        int ans=1;
        for (int i=1;i<n;i++) {
            if (nums[i-1]<nums[i]) {
                cur++;
                ans=max(ans,cur/2);
            }
            else {
                pre=cur;
                cur=1;
            }
            ans=max(ans,min(pre,cur));
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{5,8,-2,-1};

    Solution so;
    cout<<so.maxIncreasingSubarrays(nums)<<endl;
    return 0;
}
