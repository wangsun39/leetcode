// 给你一个整数数组 nums。

// 如果某个下标 i 满足以下条件，则称其为 平衡下标： i 左侧所有元素的总和等于 i 右侧所有元素的乘积。

// 如果左侧没有元素，则总和视为 0。同样，如果右侧没有元素，则乘积视为 1。

// 要求返回最小的 平衡下标，如果不存在平衡下标，则返回 -1。

 

// 示例 1：

// 输入： nums = [2,1,2]

// 输出： 1

// 解释：

// 对于下标 i = 1：

// 左侧总和 = nums[0] = 2
// 右侧乘积 = nums[2] = 2
// 由于左侧总和等于右侧乘积，下标 1 是平衡下标。
// 没有更小的下标满足条件，因此答案是 1。

// 示例 2：

// 输入： nums = [2,8,2,2,5]

// 输出： 2

// 解释：

// 对于下标 i = 2：

// 左侧总和 = 2 + 8 = 10
// 右侧乘积 = 2 * 5 = 10
// 由于左侧总和等于右侧乘积，下标 2 是平衡下标。
// 没有更小的下标满足条件，因此答案是 2。

// 示例 3：

// 输入： nums = [1]

// 输出： -1

// 对于下标 i = 0：

// 左侧为空，因此左侧总和为 0。
// 右侧为空，因此右侧乘积为 1。
// 由于左侧总和不等于右侧乘积，下标 0 不是平衡下标。
// 因此，不存在平衡下标，答案是 -1。

 

// 提示：

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    int smallestBalancedIndex(vector<int>& nums) {
        long long l=0, r=1,n=nums.size();
        for (int i=0;i<n;i++) {
            l+=nums[i];
        }
        for (int i=n-1;i>=0;i--) {
            l-=nums[i];
            if (l==r) return i;
            if ((double)r*nums[i]>1e9*1e5) break;
            r*=nums[i];
        }
        return -1;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
