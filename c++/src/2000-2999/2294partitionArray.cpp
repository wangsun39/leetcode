#include "lc_pub.h"

class Solution {
    public:
    int partitionArray(vector<int>& nums, int k) {
        ranges::sort(nums);
        int n=nums.size(),ans=1;
        int first=nums[0];
        for(int i=1;i<n;i++) {
            if (nums[i]-first<=k) continue;
            ans++;
            first=nums[i];
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    vector<int> nums{3,6,1,2,5};
    auto v = so.partitionArray(nums, 2);
    cout << v << endl;
    return 0;
}
