// 给你一个长度为 n 的整数数组 nums，其中 nums 是范围 [1, n] 内整数的一个 排列 。

// 同时给你一个长度为 n 的 二进制 数组 locked 和一个整数 k。

// locked[i] = 1 表示下标 i 已锁定。
// locked[i] = 0 表示下标 i 已解锁。
// 你可以按 任意顺序 执行以下操作：

// 交换：选择一个下标 i，需满足下标 i 和 i + 1 当前都处于解锁状态，然后交换 nums[i] 和 nums[i + 1]。
// 解锁：选择一个下标 i，满足 locked[i] = 1，并通过将 locked[i] = 0 来 永久 解锁它。
// 你可以执行任意次数的交换操作，但 最多 只能执行 k 次解锁操作。

// 返回将 nums 整理为 严格递增 顺序所需的 最小总操作次数 。如果不可能，则返回 -1。

// 排列是指数组中所有元素的一个重新排列。

// 二进制数组 是仅包含 0 和 1 的数组。

 

// 示例 1：

// 输入： nums = [2,1,3,4], locked = [0,1,0,1], k = 1

// 输出： 2

// 解释：

// 解锁下标 1。数组 locked 变为 [0,0,0,1]。
// 交换 nums[0] 和 nums[1]。数组 nums 变为 [1,2,3,4]。
// 总操作次数为 1 + 1 = 2。

// 示例 2：

// 输入： nums = [3,1,2], locked = [1,0,1], k = 2

// 输出： 4

// 解释：

// 解锁下标 0 和 2。此时所有下标都已解锁。
// 交换下标 0 和 1。数组 nums 变为 [1,3,2]。
// 交换下标 1 和 2。数组 nums 变为 [1,2,3]。
// 总操作次数为 2 + 2 = 4。

// 示例 3：

// 输入： nums = [2,3,1], locked = [1,0,0], k = 0

// 输出： -1

// 解释：

// 下标 0 被锁定，因此它的值无法被移动。由于 k = 0，无法解锁任何下标。因此，无法对数组进行排序。

 

// 提示：

// 1 <= n == nums.length == locked.length <= 2000
// 1 <= nums[i] <= n
// 0 <= locked[i] <= 1
// nums 是范围 [1, n] 内整数的一个排列。
// 0 <= k <= n


#include "lc_pub.h"

class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& locked, int k) {
        int ans = 0;
        int n=nums.size();
        int mx=0;
        for (int i=0;i<n;i++) {
            // 先考虑必须解锁的位置
            if (locked[i]) {
                if (nums[i]!=i+1) {
                    ans++;
                }
                else if (mx>nums[i]) {
                    // 前面有更大的元素需要跨越 nums[i]
                    ans++;
                }
            }
            mx = max(mx, nums[i]);
        }
        if (ans>k) return -1;
        vector<vector<int>> pp(n, std::vector<int>(2, 0));
        for (int i=0;i<n;i++) {
            pp[i][0]=nums[i];
            pp[i][1]=i;
        }
        ranges::sort(pp);
        for (int i=0;i<n;i++) {
            if (pp[i][1]>i)  // 相邻对换，只需考虑从后面移动到前面的情况，剩下的位置会自动归位
                ans+=pp[i][1]-i;
        }

        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,2,1},locked={0,1,0};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.minOperations(nums,locked,1)<<endl;

    return 0;
}
