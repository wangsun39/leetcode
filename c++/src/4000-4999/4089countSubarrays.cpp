// 给你一个整数数组 nums 和两个整数 minK 与 maxK。

// 一个宽界子数组 是指满足以下条件的 子数组 ：子数组中的每个元素都 大于或等于 minK 且 小于或等于 maxK。

// 返回 nums 中宽界子数组的 数量 。

// 子数组 是数组中连续的 非空 元素序列。

 

// 示例 1：

// 输入： nums = [1,4,7,3], minK = 1, maxK = 5

// 输出： 4

// 解释：

// 宽界子数组为 [1]、[4]、[3] 和 [1, 4]。这些子数组中的最小值至少为 minK = 1，最大值至多为 maxK = 5。

// 示例 2：

// 输入： nums = [1,1], minK = 1, maxK = 1

// 输出： 3

// 解释：

// 宽界子数组为 [1]、[1] 和 [1, 1]。这些子数组中的最小值至少为 minK = 1，最大值至多为 maxK = 1。

 

// 提示：

// 2 <= nums.length <= 105
// 1 <= nums[i], minK, maxK <= 106


#include "lc_pub.h"

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long ans=0;
        int n=nums.size();
        int pre=-1;
        for (int i=0;i<n;i++) {
            if (nums[i]>=minK&&nums[i]<=maxK) {
                ans+=i-pre;
            }
            else {
                pre=i;
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;

    return 0;
}
