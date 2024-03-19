# 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
#
# 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
#
# 请你返回 好 子数组的最大可能 分数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,4,3,7,4,5], k = 3
# 输出：15
# 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
# 示例 2：
#
# 输入：nums = [5,5,4,5,4,1,1,1], k = 0
# 输出：20
# 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 2 * 104
# 0 <= k < nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        def check(nums, p):
            nonlocal ans
            l = r = cur = p
            while True:
                while l >= 0 and nums[l] >= nums[cur]:
                    l -= 1
                while r < n and nums[r] >= nums[cur]:
                    r += 1
                ans = max(ans, nums[cur] * (r - l - 1))
                if l < 0:
                    return
                cur = l
        check(nums, k)
        check(nums[::-1], n - 1 - k)
        return ans




so = Solution()
print(so.maximumScore(nums = [1,4,3,7,4,5], k = 3))
print(so.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0))




