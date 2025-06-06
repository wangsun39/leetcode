# 给你一个整数数组nums 和一个整数k，请你在数组中找出 不同的k-diff 数对，并返回不同的 k-diff 数对 的数目。
#
# k-diff数对定义为一个整数对 (nums[i], nums[j]) ，并满足下述全部条件：
#
# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# 注意，|val| 表示 val 的绝对值。
#
#
#
# 示例 1：
#
# 输入：nums = [3, 1, 4, 1, 5], k = 2
# 输出：2
# 解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
# 示例 2：
#
# 输入：nums = [1, 2, 3, 4, 5], k = 1
# 输出：4
# 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
# 示例 3：
#
# 输入：nums = [1, 3, 1, 5, 4], k = 0
# 输出：1
# 解释：数组中只有一个 0-diff 数对，(1, 1) 。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107


from leetcode.allcode.competition.mypackage import *
import bisect

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i, e in enumerate(nums):
            pos = bisect.bisect_left(nums, e + k, i + 1)
            if pos >= n:
                return ans
            if i > 0 and e == nums[i - 1]:
                continue
            if e + k == nums[pos]:
                ans += 1
        return ans



