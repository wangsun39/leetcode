#include "lc_pub.h"

class Solution {
public:
vector<int> buildArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, 0);
    for (int i=0;i<n;i++)
        ans[i]=nums[nums[i]];
    return ans;
}

};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={0,2,1,5,3,4};

    Solution so;
    auto v = so.buildArray(nums);
    cout << v << endl;
    return 0;
}
