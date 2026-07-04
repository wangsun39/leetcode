// 给你一个整数数组 nums，以及两个整数 k 和 mul。

// 从 nums 中选出 恰好 k 个元素。你可以按照任意顺序逐个处理这些元素。

// 对于每个被选择的元素，都可以 独立地 选择以下两种操作之一：

// 将该元素的值 加 到总和中；或
// 将该元素乘以 mul 的 当前 值，并将结果 加 到总和中。
// 每处理一个被选择的元素后，无论选择哪种操作，mul 都会 减少 1。mul 的当前值可能变为 0 或负数。

// 返回一个整数，表示可能得到的 最大 总和。

 

// 示例 1：

// 输入： nums = [6,1,2,9], k = 3, mul = 2

// 输出： 26

// 解释：

// 一种最优方式如下：

// 一种最优选择是 nums[3] = 9、nums[0] = 6 和 nums[2] = 2。
// 先处理 nums[3] = 9：选择乘法，因此贡献 9 * 2 = 18。此时，mul 变为 1。
// 接着处理 nums[0] = 6：选择乘法，因此贡献 6 * 1 = 6。此时，mul 变为 0。
// 最后处理 nums[2] = 2：选择直接相加，因此贡献 2。
// 总和为 18 + 6 + 2 = 26。
// 示例 2：

// 输入： nums = [3,7,5,2], k = 2, mul = 4

// 输出： 43

// 解释：

// 一种最优方式如下：

// 一种最优选择是 nums[1] = 7 和 nums[2] = 5。
// 先处理 nums[1] = 7：选择乘法，因此贡献 7 * 4 = 28。此时，mul 变为 3。
// 接着处理 nums[2] = 5：选择乘法，因此贡献 5 * 3 = 15。
// 总和为 28 + 15 = 43。
// 示例 3：

// 输入： nums = [4,4], k = 1, mul = 1

// 输出： 4

// 解释：

// 一种最优方式如下：

// 一种最优选择是 nums[0] = 4。
// 处理 nums[0] = 4：选择乘法，因此贡献 4 * 1 = 4。
// 总和为 4。
 

// 提示：

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 105
// 1 <= k <= nums.length
// 1 <= mul <= 105

#include "lc_pub.h"

class Solution {
public:
    long long maxSum(vector<int>& nums, int k, int mul) {
        ranges::sort(nums,greater<int>());
        long long ans = 0;
        for (int i=0;i<k;i++) {
            if (mul>0) {
                ans+=(long long)nums[i]*mul;
                mul--;
            }
            else {
                ans+=nums[i];
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
