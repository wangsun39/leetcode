# 给你一个整数数组 nums 和两个正整数 m 和 k 。
#
# 请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
#
# 如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
#
# 子数组指的是一个数组中一段连续 非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [2,6,7,3,1,7], m = 3, k = 4
# 输出：18
# 解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
# 示例 2：
#
# 输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
# 输出：23
# 解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
# 示例 3：
#
# 输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
# 输出：0
# 解释：输入数组中不存在长度为 k = 3 的子数组含有至少  m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# 1 <= m <= k <= nums.length
# 1 <= nums[i] <= 109
from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        counter = {}
        for x in nums[:k]:
            if x not in counter:
                counter[x] = 1
            else:
                counter[x] += 1
        s = sum(nums[:k])
        ans = 0
        if len(counter) >= m: ans = s
        for l in range(1, n - k + 1):
            counter[nums[l - 1]] -= 1
            if counter[nums[l - 1]] == 0:
                del(counter[nums[l - 1]])
            if nums[l + k - 1] not in counter:
                counter[nums[l + k - 1]] = 1
            else:
                counter[nums[l + k - 1]] += 1
            s += (nums[l + k - 1] - nums[l - 1])
            if len(counter) >= m:
                ans = max(ans, s)
        return ans


so = Solution()
print(so.maxSum([1,2,1,2,1,2,1],
3,
3))
print(so.maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3))
print(so.maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4))
print(so.maxSum(nums = [1,2,1,2,1,2,1], m = 3, k = 3))




