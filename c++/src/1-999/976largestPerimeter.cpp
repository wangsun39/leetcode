#include "lc_pub.h"


class Solution {
    
    public:
    int largestPerimeter(vector<int>& nums) {
        ranges::sort(nums, {}, [&](int x) {return -x;});
        int n = nums.size();
        for (int i=0;i<n-2;i++) {
            if (nums[i+1]+nums[i+2]>nums[i]) {
                return nums[i+1]+nums[i+2]+nums[i];
            }
        }
        return 0;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
