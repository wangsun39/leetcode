#include "lc_pub.h"


class Solution {
    public:
    string triangleType(vector<int>& nums) {
        ranges::sort(nums);
        if (nums[0] + nums[1]<=nums[2]) return "none";
        if (nums[0] == nums[2]) return "equilateral";
        if (nums[0] == nums[1] || nums[1]==nums[2]) return "isosceles";
        return "scalene";
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    cout << so.triangleType(nums) << endl;
    return 0;
}
