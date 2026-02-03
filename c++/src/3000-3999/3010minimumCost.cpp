#include "lc_pub.h"


class Solution {
    public:
    int minimumCost(vector<int>& nums) {
        sort(nums.begin() + 1, nums.end());
        return nums[0]+nums[1]+nums[2];
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    return 0;
}
