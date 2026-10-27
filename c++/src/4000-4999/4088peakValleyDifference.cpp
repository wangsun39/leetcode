// 给你一个长度为 n 的整数数组 nums。

// 如果满足以下 所有 条件，则下标志 i 被称为 峰值 ：

// 0 < i < n - 1
// nums[i] > nums[i - 1]
// nums[i] > nums[i + 1]
// 如果满足以下 所有 条件，则下标志 i 被称为 谷值 ：

// 0 < i < n - 1
// nums[i] < nums[i - 1]
// nums[i] < nums[i + 1]
// 返回一个整数，表示所有峰值之和与所有谷值之和的 差值 。

 

// 示例 1：

// 输入： nums = [1,5,2,4,1,3,0]

// 输出： 9

// 解释：

// 峰值分别是 nums[1] = 5、nums[3] = 4 和 nums[5] = 3。
// 谷值分别是 nums[2] = 2 和 nums[4] = 1。
// 峰值之和与谷值之和的差值为 (5 + 4 + 3) - (2 + 1) = 9。因此，答案是 9。
// 示例 2：

// 输入： nums = [-5,-6,-1,-2,5,3,2]

// 输出： 12

// 解释：

// 峰值分别是 nums[2] = -1 和 nums[4] = 5。
// 谷值分别是 nums[1] = -6 和 nums[3] = -2。
// 峰值之和与谷值之和的差值为 (-1 + 5) - (-6 + (-2)) = 12。因此，答案是 12。
// 示例 3：

// 输入： nums = [6,5,2,5,5,3,6]

// 输出： -5

// 解释：

// 数组中没有峰值。
// 谷值分别是 nums[2] = 2 和 nums[5] = 3。
// 峰值之和与谷值之和的差值为 (0) - (2 + 3) = -5。因此，答案是 -5。
 

// 提示：

// 3 <= n == nums.length <= 100
// -100 <= nums[i] <= 100


#include "lc_pub.h"

class Solution {
public:
    int peakValleyDifference(vector<int>& nums) {
        int n=nums.size();
        int a=0,b=0;
        for (int i=1;i<n-1;i++) {
            if (nums[i-1]<nums[i]&&nums[i]>nums[i+1]) a+=nums[i];
            if (nums[i-1]>nums[i]&&nums[i]<nums[i+1]) b+=nums[i];
        }
        return a-b;
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
