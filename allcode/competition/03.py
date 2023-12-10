# 给你一个整数数组 nums 和一个 正整数 k 。
#
# 请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。
#
# 子数组是数组中的一个连续元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,2,3,3], k = 2
# 输出：6
# 解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
# 示例 2：
#
# 输入：nums = [1,4,2,1], k = 3
# 输出：0
# 解释：没有子数组包含元素 4 至少 3 次。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        idx = [i for i, x in enumerate(nums) if x == mx]
        if len(idx) < k:
            return 0
        m = len(idx)
        ans = 0
        for i in range(k - 1, m):  # 最左侧的下标为 i - k + 1
            l = i - k + 1
            if l > 0:
                left = idx[l] - idx[l - 1] - 1
            else:
                left = idx[0]
            right = n - (idx[i] + 1)
            ans += (left + 1) * (right + 1)

        return ans


so = Solution()
print(so.countSubarrays([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], 2))
print(so.countSubarrays(nums = [1,3,2,3,3], k = 2))
print(so.countSubarrays(nums = [1,4,2,1], k = 3))




