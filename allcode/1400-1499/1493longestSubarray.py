# 给你一个二进制数组 nums ，你需要从中删掉一个元素。
#
# 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
#
# 如果不存在这样的子数组，请返回 0 。
#
#
#
# 提示 1：
#
# 输入：nums = [1,1,0,1]
# 输出：3
# 解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
# 示例 2：
#
# 输入：nums = [0,1,1,1,0,1,1,0,1]
# 输出：5
# 解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
# 示例 3：
#
# 输入：nums = [1,1,1]
# 输出：2
# 解释：你必须要删除一个元素。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 要么是 0 要么是 1 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0] * n
        r = [0] * n
        for i in range(1, n):
            if nums[i - 1] == 1:
                l[i] = l[i - 1] + 1
        ans = l[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                r[i] = r[i + 1] + 1
            ans = max(ans, l[i] + r[i])
        return ans

so = Solution()
print(so.longestSubarray([1,1,0,1]))



