#include "lc_pub.h"

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        ranges::sort(nums);
        int ans=INT_MAX,n=nums.size();
        for (int i=0;i<n-k+1;i++) {
            ans=min(ans,nums[i+k-1]-nums[i]);
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    // vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    // cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    return 0;
}
