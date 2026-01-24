#include "lc_pub.h"

class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int ans=0,n=nums.size();
        for (int i=0;i<n/2;i++) {
            ans=max(ans,nums[i]+nums[n-1-i]);
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    
    return 0;
}
