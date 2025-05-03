#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
bool canPartition(vector<int>& nums) {
    int s = reduce(nums.begin(), nums.end(), 0);
    if (s & 1) return false;
    int half=s/2;
    int n=nums.size();
    vector<bool> dp1(half+1, false);  // dp[i][j] 前i个数组合和为j的是否可能
    vector<bool> dp2(half+1, false);  // dp[i][j] 前i个数组合和为j的是否可能
    if (nums[0]>half) return false;
    // dp1[0]=dp1[nums[0]] = true;
    for (int i=0;i<n;i++) {
        dp2=dp1;
        if (nums[i]>half) return false;
        dp2[nums[i]]=true;
        for (int j=nums[i];j<half+1;j++) {
            if (dp2[j]) continue;
            dp2[j] = dp1[j-nums[i]];
        }
        if (dp2[half]) return true;
        swap(dp1, dp2);
    }
    return false;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3};
    Solution so;
    auto v = so.canPartition(nums);
    cout << v << endl;
    return 0;
}
