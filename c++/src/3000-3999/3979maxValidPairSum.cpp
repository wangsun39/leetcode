// 给你一个长度为奇数 n 的整数数组 nums 。

// 如果 nums 的下标中间元素在数组中 恰好 出现一次，返回 true 。否则返回 false 。

 

// 示例 1：

// 输入： nums = [1,2,3]

// 输出： true

// 解释：

// nums 的中间元素是 2 ，它恰好出现一次。

// 因此，答案为 true 。

// 示例 2：

// 输入： nums = [1,2,2]

// 输出： false

// 解释：

// nums 的中间元素是 2 ，它出现了两次。

// 因此，答案为 false 。

 

// 提示：

// 1 <= n == nums.length <= 100
// n 是奇数。
// 1 <= nums[i] <= 100

#include "lc_pub.h"


class Solution {
public:
    int maxValidPairSum(vector<int>& nums, int k) {
        int n=nums.size();
        int mx=0;
        int ans=0;
        for (int j=0;j<n;j++) {
            if (j-k>=0) {
                mx=max(mx, nums[j-k]);
                ans=max(ans, nums[j]+mx);
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
