# 给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中 「优美子数组」 的数目。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 示例 2：
#
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 示例 3：
#
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
#
#
# 提示：
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        idx = []
        for i, x in enumerate(nums):
            if x & 1:
                idx.append(i)
        if len(idx) < k: return 0
        n = len(nums)
        idx = [-1] + idx + [n]
        m = len(idx)
        ans = 0
        for i in range(1, len(idx) + 1):
            if i + k - 1 >= m - 1: break
            ans += (idx[i] - idx[i - 1]) * (idx[i + k] - idx[i + k - 1])
        return ans


obj = Solution()
print(obj.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))  # 2

