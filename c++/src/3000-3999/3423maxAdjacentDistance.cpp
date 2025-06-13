#include "lc_pub.h"


class Solution {
    public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size();
        int ans = abs(nums[0] - nums[n - 1]);
        for (int i=0;i<n - 1;i++) {
            ans = max(ans, abs(nums[i+1]-nums[i]));
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,4};

    Solution so;
    cout << so.maxAdjacentDistance(nums) << endl;
    return 0;
}
