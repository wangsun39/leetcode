# 给你一个整数数组 nums ，该数组具有以下属性：
#
# nums.length == 2 * n.
# nums 包含 n + 1 个 不同的 元素
# nums 中恰有一个元素重复 n 次
# 找出并返回重复了 n 次的那个元素。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,3]
# 输出：3
# 示例 2：
#
# 输入：nums = [2,1,2,5,3,2]
# 输出：2
# 示例 3：
#
# 输入：nums = [5,1,5,2,5,3,5,4]
# 输出：5
#
#
# 提示：
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums 由 n + 1 个 不同的 元素组成，且其中一个元素恰好重复 n 次


from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mn = inf
        ans = 0
        for i, x in sorted(enumerate(nums), key=lambda x: x[1]):
            ans = max(ans, i - mn)
            mn = min(mn, i)
        return ans


so = Solution()
print(so.maxWidthRamp([6,0,8,2,1,5]))

