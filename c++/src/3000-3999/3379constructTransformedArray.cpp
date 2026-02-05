#include "lc_pub.h"


class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n=nums.size();
        vector<int> ans(n,0);
        for (int i=0;i<n;i++) {
            if (nums[i]>0) {
                ans[i]=nums[(i+nums[i])%n];
            }
            else if (nums[i]<0) {
                ans[i]=nums[((i+nums[i])%n+n)%n];
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{5,2,5,4,5};

    Solution so;
    return 0;
}
