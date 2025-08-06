# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 示例 2:
#
# 输入：nums = [1,0,1,1,0,1]
# 输出：2
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 不是 0 就是 1.

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre = -1
        ans = 0
        for i, x in enumerate(nums):
            if x == 1:
                if pre != -1:
                    pass
                else:
                    pre = i
                ans = max(ans, i - pre + 1)
            else:
                pre = -1
        return ans



so = Solution()
print(so.findMaxConsecutiveOnes([1,1,0,1,1,1]))

