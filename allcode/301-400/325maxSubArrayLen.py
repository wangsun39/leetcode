# 给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长连续
# 子数组
# 长度。如果不存在任意一个符合要求的子数组，则返回 0。
#
#
#
# 示例 1:
#
# 输入: nums = [1,-1,5,-2,3], k = 3
# 输出: 4
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
# 示例 2:
#
# 输入: nums = [-2,-1,2,1], k = 1
# 输出: 2
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 105
# -104 <= nums[i] <= 104
# -109 <= k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        d = {}  # 记录第一个前缀和为x的下标：d[x] - 1
        for i, x in enumerate(s):
            if x not in d:
                d[x] = i
        ans = 0
        for i, x in enumerate(s):
            if x - k in d and d[x - k] < i:
                ans = max(ans, i - d[x - k])
        return ans


so = Solution()
print(so.maxSubArrayLen(nums = [1,-1,5,-2,3], k = 3))
print(so.maxSubArrayLen(nums = [-2,-1,2,1], k = 1))




