#include "lc_pub.h"


class Solution {

public:
    int minimumDeletions(vector<int>& nums) {
        int mx=0, mn=0, n=nums.size();
        for (int i=0;i<n;i++) {
            if (nums[i]<nums[mn]) mn=i;
            if (nums[i]>nums[mx]) mx=i;
        }
        int ans=max(mn,mx)+1;
        ans=min(ans,n-min(mn,mx));
        ans=min(ans,n-(max(mn,mx)-min(mn,mx)-1));
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
